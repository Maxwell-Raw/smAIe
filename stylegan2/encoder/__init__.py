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
dir = os.path.dirname(os.path.dirname(__file__))
dir2=os.path.join(dir,'encoder')
dir3=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(dir3)
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
print('models init complete!')
__all__ = ["age_direction", "angle_direction", "gender_direction", "eyes_direction", "glasses_direction", "smile_direction", "beauty_direction", "angry_direction", "disgust_direction", "easy_direction", "fear_direction", "happy_direction", "sad_direction", "suprise_direction", "face_shape_direction", "face_height_direction", "face_width_direction",'person','generator']