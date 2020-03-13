#!/usr/bin/python
# coding=utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/pictureupload'
    t1 = "'1234567890','mix_0.jpg','mix_1.jpg','mix_2.jpg',{'Container': '1234567890','Matteral': [1], 'Quality': 0.8, 'plate': 11}"
    data = {'mykey': t1}

    pa1 =r'\202002220023600002S.png'
    pa2 =r'\202002220023600003S.png'
    pa3 =r'\202002220023600004S.png'
    
    files = {'myfile':open(pa1,'rb'),'myfile1':open(pa2,'rb'),'myfile2':open(pa3,'rb')}
##    response = requests.request("POST",url,files=files)
    
##    response = requests.request("POST",url,data=data,files=files)

    response = requests.request("POST",url,data=data,files=files)
    
    print(response.text)
    
