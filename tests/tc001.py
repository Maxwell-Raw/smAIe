import json
import os
import  requests,pprint

# 构建添加 客户信息的 消息体，是json格式
payload = {
    "Angry":0,          
    "Easy":0,
    "Disgusted":0,
    "Fearful":0,
    "Happy":0,
    "Sad":0,
    "Surprised":0,
    "ex13_Face":0,              
    "ex13_Face2":0,             
    "Facew":0,                  
    "Faceh":0,
    "Beauty":0,
    "Eyeo":0,
    "Age":0,
    "Sex":0
    
}

# 发送请求给web服务
response = requests.post('http://127.0.0.1:81/api/Test/setvalue',
              json=payload)
#response = requests.post('http://127.0.0.1:81/api/Test/GetEnglishName',
#              data=json.dumps(payload))
print(response.status_code)

obj = response.json()
print(obj)

#pprint.pprint(data)

