#!/usr/bin/python
# coding=utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://172.16.213.46:8080/pictureupload'
    t1 = "'1234567890','mix_0.jpg','mix_1.jpg','mix_2.jpg',{'Container': '1234567890','Matteral': [1], 'Quality': 0.8, 'plate': 11}"
    data = {'mykey': t1}
    files = {'myfile':open(r'D:\ftp\CVIS_SW_IREC\picture\2020-03-03-BGV7100\bgp_png_V7100\202002220023600002S.png','rb')}
##    response = requests.request("POST",url,files=files)
    
##    response = requests.request("POST",url,data=data,files=files)

    response = requests.request("POST",url,data=data,files=files)
    

    print(response.text)
    

