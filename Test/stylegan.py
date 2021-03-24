from django.http import JsonResponse
import json
from stylegan2.encoder.move_and_show import move
from stylegan2.encoder.preprocess import preprocess
import tensorflow as tf

def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数 在 request 对象的 GET属性中
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    """angry = 0
    easy=0
    disgusted=0
    fearful=0
    happy=0
    sad=0
    surprised=0
    face=0
    face2=0
    facew=0
    faceh=0
    beauty=0
    eyeo=0
    age=0
    sex=0"""
    print(request.params)


    angry = request.params['Angry']
    easy=request.params['Easy']
    disgusted=request.params['Disgusted']
    fearful=request.params['Fearful']
    happy=request.params['Happy']
    sad=request.params['Sad']
    surprised=request.params['Surprised']
    face=request.params['ex13_Face']
    face2=request.params['ex13_Face2']
    facew=request.params['Facew']
    faceh=request.params['Faceh']
    beauty=request.params['Beauty']
    eyeo=request.params['Eyeo']
    age=request.params['Age']
    sex=request.params['Sex']
    print(age)
    #sess=tf.Session()
    return move(angry,easy,disgusted,fearful,happy,sad,surprised,face,face2,facew,faceh,beauty,eyeo,age,sex)

def geturl(request):
    if request.method == 'GET':
        request.params = request.GET
    elif request.method in ['POST','PUT','DELETE']:
        request.params = json.loads(request.body)
    imgpath=request.params['imgpath']
    return preprocess(imgpath)




