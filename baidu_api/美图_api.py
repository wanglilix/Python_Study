# -*- coding: utf-8 -*-

import requests,json

url = 'http://apis.baidu.com/txapi/mvtp/meinv?'
headers = {'apikey':"a79124c4594c2e5a0799a39ea8f64c87"}
params = {'num':'10'}
r = requests.get(url,params = params,headers = headers)
r = r.json()

def saveImage(imgUrl,imgName= 'default.jpg'):
    response = requests.get(imgUrl,stream = True)
    image = response.content
    dst = "k:\\baidu_img\\"
    path = dst+imgName
    print ('save the file:'+path+'\n')
    with open(path,'wb') as img:
       img.write(image)
    img.close()


def run():
    for line in r['newslist']:
        title = line['title']
        picUrl = line['picUrl']
        saveImage(picUrl,imgName = title+'.jpg')

run()