#align module
import os
import sys
import bz2
import sys
sys.path.append('X:\\projects\\bysms1\\stylegan2\\encoder')
from keras.utils import get_file
from ffhq_dataset.face_alignment import image_align
from ffhq_dataset.landmarks_detector import LandmarksDetector

#encode module
import argparse
import pickle
from tqdm import tqdm
import PIL.Image
import numpy as np
import dnnlib
import dnnlib.tflib as tflib
import pretrained_networks
from encoder.generator_model import Generator
from encoder.perceptual_model import PerceptualModel

img_path = 'raw_images/testa.jpg'

###################### align_image ######################
LANDMARKS_MODEL_URL = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'


def unpack_bz2(src_path):
    data = bz2.BZ2File(src_path).read()
    dst_path = src_path[:-4]
    with open(dst_path, 'wb') as fp:
        fp.write(data)
    return dst_path

def split_to_batches(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def preprocess(img_path): 
    """
    Extracts and aligns all faces from images using DLib and a function from original FFHQ dataset preparation step
    python align_images.py /raw_images /aligned_images
    """

    landmarks_model_path = unpack_bz2(get_file('shape_predictor_68_face_landmarks.dat.bz2',
                                               LANDMARKS_MODEL_URL, cache_subdir='temp'))
    #RAW_IMAGES_DIR = sys.argv[1]
    ALIGNED_IMAGES_DIR = 'aligned_images/'
    (filepath, tempfilename) = os.path.split(img_path)
    (filename, extension) = os.path.splitext(tempfilename)

    landmarks_detector = LandmarksDetector(landmarks_model_path)
    #for img_name in [f for f in os.listdir(RAW_IMAGES_DIR) if f[0] not in '._']:
    
    raw_img_path = img_path
    for i, face_landmarks in enumerate(landmarks_detector.get_landmarks(raw_img_path), start=1):
        face_img_name = '%s.png' % (os.path.splitext(tempfilename)[0])
        aligned_face_path = os.path.join(ALIGNED_IMAGES_DIR, face_img_name)
        #print(aligned_face_path)
        os.makedirs(ALIGNED_IMAGES_DIR, exist_ok=True)
        image_align(raw_img_path, aligned_face_path, face_landmarks)

#align_image(img_path)


###################### encode image code ####################################

    parser = argparse.ArgumentParser(description='Find latent representation of reference images using perceptual loss')
    parser.add_argument('--src_dir', default = 'aligned_images/', help='Directory with images for encoding')
    parser.add_argument('--generated_images_dir', default = 'generated_images/', help='Directory for storing generated images')
    parser.add_argument('--dlatent_dir', default = 'latent_representations/', help='Directory for storing dlatent representations')

    parser.add_argument('--network_pkl', default='gdrive:networks/stylegan2-ffhq-config-f.pkl', help='Path to local copy of stylegan2-ffhq-config-f.pkl')

    # for now it's unclear if larger batch leads to better performance/quality
    parser.add_argument('--batch_size', default=1, help='Batch size for generator and perceptual model', type=int)

    # Perceptual model params
    parser.add_argument('--image_size', default=256, help='Size of images for perceptual model', type=int)
    parser.add_argument('--lr', default=1., help='Learning rate for perceptual model', type=float)
    parser.add_argument('--iterations', default=1000, help='Number of optimization steps for each batch', type=int)

    # Generator params
    parser.add_argument('--randomize_noise', default=False, help='Add noise to dlatents during optimization', type=bool)
    args, other_args = parser.parse_known_args()

    #ref_images = [os.path.join(args.src_dir, x) for x in os.listdir(args.src_dir)]
    #ref_images = list(filter(os.path.isfile, ref_images))
    ref_images = []
    ref_images.append(aligned_face_path)
    #ref_images = aligned_face_path
    
    if len(ref_images) == 0:
        raise Exception('%s is empty' % args.src_dir)

    os.makedirs(args.generated_images_dir, exist_ok=True)
    os.makedirs(args.dlatent_dir, exist_ok=True)

    # Initialize generator and perceptual model
    tflib.init_tf()
    generator_network, discriminator_network, Gs_network = pretrained_networks.load_networks(args.network_pkl)

    generator = Generator(Gs_network, args.batch_size, randomize_noise=args.randomize_noise)
    perceptual_model = PerceptualModel(args.image_size, layer=9, batch_size=args.batch_size)
    perceptual_model.build_perceptual_model(generator.generated_image)

    # Optimize (only) dlatents by minimizing perceptual loss between reference and generated images in feature space
    for images_batch in tqdm(split_to_batches(ref_images, args.batch_size), total=len(ref_images)//args.batch_size):
        names = [os.path.splitext(os.path.basename(x))[0] for x in images_batch]

        perceptual_model.set_reference_images(images_batch)
        op = perceptual_model.optimize(generator.dlatent_variable, iterations=args.iterations, learning_rate=args.lr)
        pbar = tqdm(op, leave=False, total=args.iterations)
        for loss in pbar:
            pbar.set_description(' '.join(names)+' Loss: %.2f' % loss)
        print(' '.join(names), ' loss:', loss)

        # Generate images from found dlatents and save them
        generated_images = generator.generate_images()
        generated_dlatents = generator.get_dlatents()
        for img_array, dlatent, img_name in zip(generated_images, generated_dlatents, names):
            img = PIL.Image.fromarray(img_array, 'RGB')
            img.save(os.path.join(args.generated_images_dir, f'{img_name}.png'), 'PNG')
            np.save(os.path.join(args.dlatent_dir, f'{img_name}.npy'), dlatent)

        generator.reset_dlatents()
