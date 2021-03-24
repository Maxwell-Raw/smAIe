import os
import pickle
import io
import base64
from PIL import Image
import PIL.Image
from django.http.response import JsonResponse
import numpy as np
import sys
sys.path.append('X:\\projects\\bysms1\\stylegan2\\encoder')
import dnnlib
import dnnlib.tflib as tflib
import config
from encoder.generator_model import Generator
import matplotlib.pyplot as plt
import glob
import keras
from . import *

dlatents_dir = 'latent_representations'
generated_dir = 'generated_images'
result_dir = 'results'

class config:
    def __init__(self,dlatents_dir,generated_dir, result_dir):
        self.dlatents_dir = dlatents_dir
        self.generated_dir = generated_dir
        self.result_dir = result_dir
config = config('latent_representations','generated_images', 'results')

# 预训练好的网络模型，来自NVIDIA
Model = 'X:\projects\\bysms1\\stylegan2\\encoder\\models\\stylegan2-ffhq-config-f.pkl'
_Gs_cache = dict()
 
# 加载StyleGAN已训练好的网络模型
def load_Gs(model):
    if model not in _Gs_cache:
        model_file = glob.glob(Model)
        if len(model_file) == 1:
            model_file = open(model_file[0], "rb")
        else:
            raise Exception('Failed to find the model')
 
        _G, _D, Gs = pickle.load(model_file)
        # _G = Instantaneous snapshot of the generator. Mainly useful for resuming a previous training run.
        # _D = Instantaneous snapshot of the discriminator. Mainly useful for resuming a previous training run.
        # Gs = Long-term average of the generator. Yields higher-quality results than the instantaneous snapshot.
 
        # Print network details.
        # Gs.print_layers()
 
        _Gs_cache[model] = Gs
    return _Gs_cache[model]
 
# 使用generator生成图片
def generate_image(generator, latent_vector):
    latent_vector = latent_vector.reshape((1, 18, 512))
    generator.set_dlatents(latent_vector)
    img_array = generator.generate_images()[0]
    img = PIL.Image.fromarray(img_array, 'RGB')
    return img.resize((256, 256))
 
# 将真实人脸图片对应的latent与改变人脸特性/表情的向量相混合，调用generator生成人脸的变化图片

 
 
def move(angry,easy,disgusted,fearful,happy,sad,surprised,face,face2,facew,faceh,beauty,eyeo,age,sex):
    # 初始化
    
    dir = os.path.dirname(os.path.dirname(__file__))
    dir2=os.path.join(dir,'encoder')
    dir3=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    print(dir3)
    """
    tflib.init_tf()
    # 调用预训练模型
    Gs_network = load_Gs(Model)
    generator = Generator(Gs_network, batch_size=1, randomize_noise=False)
 
    # 读取对应真实人脸的latent，用于图像变化，qing_01.npy可以替换为你自己的文件名
    os.makedirs(config.dlatents_dir, exist_ok=True)
    #person = np.load(os.path.join(config.dlatents_dir, 'test_01.npy'))
    
    person = np.load(dir2+'/latent_representations'+'/test_01.npy')

    # 读取已训练好的用于改变人脸特性/表情的向量
    # 包括：改变年龄、改变水平角度、改变性别、改变眼睛大小、是否佩戴眼镜、改变笑容等
    age_direction = np.load(dir2+'/ffhq_dataset/latent_directions/age.npy')
    angle_direction = np.load(dir2+'/ffhq_dataset/latent_directions/angle_horizontal.npy')
    gender_direction = np.load(dir2+'/ffhq_dataset/latent_directions/gender.npy')
    eyes_direction = np.load(dir2+'/ffhq_dataset/latent_directions/eyes_open.npy')
    glasses_direction = np.load(dir2+'/ffhq_dataset/latent_directions/glasses.npy')
    smile_direction = np.load(dir2+'/ffhq_dataset/latent_directions/smile.npy')
    beauty_direction = np.load(dir2+'/ffhq_dataset/latent_directions/beauty.npy')
    angry_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_angry.npy')
    disgust_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_disgust.npy')
    easy_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_easy.npy')
    fear_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_fear.npy')
    happy_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_happy.npy')
    sad_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_sad.npy')
    suprise_direction = np.load(dir2+'/ffhq_dataset/latent_directions/emotion_surprise.npy')
    face_shape_direction = np.load(dir2+'/ffhq_dataset/latent_directions/face_shape.npy')
    face_height_direction = np.load(dir2+'/ffhq_dataset/latent_directions/height.npy')
    face_width_direction = np.load(dir2+'/ffhq_dataset/latent_directions/width.npy')
"""
 
    directions = [age_direction, angle_direction, gender_direction, eyes_direction, glasses_direction, smile_direction, beauty_direction, angry_direction, disgust_direction, easy_direction, fear_direction, happy_direction, sad_direction, suprise_direction, face_shape_direction, face_height_direction, face_width_direction]
    # 混合人脸和变化向量，生成变化后的图片
    
    flag=6
    latent_vector=person
    
    '''
    fig,ax = plt.subplots(1, len(coeffs), figsize=(15, 10), dpi=80)
    # 调用coeffs数组，生成一系列的人脸变化图片
    for i, coeff in enumerate(coeffs):
        new_latent_vector = latent_vector.copy()
        # 人脸latent与改变人脸特性/表情的向量相混合，只运算前8层（一共18层）
        new_latent_vector[:8] = (latent_vector + coeff*(direction1 + direction2))[:8]
        ax[i].imshow(generate_image(generator, new_latent_vector))
        ax[i].set_title('Coeff: %0.1f' % coeff)
    [x.axis('off') for x in ax]
    # 显示
    plt.show()
    '''
    
    # 根据看到的人脸变化的效果，输入一个你认为合适的浮点数
    age_coeff = age
    angle_coeff = 0
    gender_coeff = sex
    eyes_coeff = eyeo
    smile_coeff = 0
    beauty_coeff = beauty
    angry_coeff = angry
    disgust_coeff = disgusted
    easy_coeff = easy
    fear_coeff = fearful
    happy_coeff = happy
    sad_coeff = sad
    suprise_coeff = surprised
    face_shape_coeff = 0
    face_height_coeff = faceh
    face_width_coeff = facew
    

    new_latent_vector = latent_vector.copy()
    # 用输入的浮点数控制生成新的人脸变化
    new_latent_vector[:7] = (latent_vector + age_coeff * directions[0] + 
                                             angle_coeff * directions[1] +
                                             gender_coeff * directions[2] +
                                             eyes_coeff * directions[3]+
                                            # glasses_coeff * directions[4]+
                                             smile_coeff * directions[5]+
                                             beauty_coeff * directions[6]+ 
                                             angry_coeff * directions[7]+ 
                                             disgust_coeff * directions[8]+ 
                                             easy_coeff * directions[9]+ 
                                             fear_coeff * directions[10]+ 
                                             happy_coeff * directions[11]+
                                             sad_coeff * directions[12]+ 
                                             suprise_coeff * directions[13]+ 
                                             face_shape_coeff * directions[14]+ 
                                             face_height_coeff * directions[15]+ 
                                             face_width_coeff * directions[16]
                                             )[:7]
    # 增加一个维度，以符合generator对向量的要求
    new_latent_vector = new_latent_vector.reshape((1, 18, 512))
    # 将向量赋值给generator
    generator.set_dlatents(new_latent_vector)
    # 调用generator生成图片
    new_person_image = generator.generate_images()[0]
    # 画图，1024x1024
    canvas = PIL.Image.new('RGB', (1024, 1024), 'white')
    canvas.paste(PIL.Image.fromarray(new_person_image, 'RGB'), ((0, 0)))
    # 根据不同的标志，存入不同的文件名
    if flag == 0:
        filename = 'new_age.png'
    if flag == 1:
        filename = 'new_angle.png'
    if flag == 2:
        filename = 'new_gender.png'
    if flag == 3:
        filename = 'new_eyes.png'
    if flag == 4:
        filename = 'new_glasses.png'
    if flag == 5:
        filename = 'new_smile.png'
    if flag == 6:
        filename = 'combined_16.png'
    # 将生成的图像保存到文件
    canvas.save(os.path.join(dir2,config.generated_dir, filename))
    canvas.save(os.path.join(dir3,'smAIe','images', filename))


    #img=Image.open('X:/stylegan/aligned_images/test_01.png')
    #buf=io.BytesIO()
    #img.save(buf,format='PNG')
    #image_stream=buf.getvalue()
    #heximage=base64.b64encode(image_stream)
    #url=os.path.join(os.path.join(dir3,'smAIe','images', filename))
    url=os.path.join(os.path.join('images', filename))
    print(url)
    
    keras.backend.clear_session()
    data={
        "ret": 0,
        #"code": heximage,
        "url":url
        }
    return JsonResponse(data)

