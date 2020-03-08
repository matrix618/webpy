#!/usr/bin/python
# coding=utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/upload'
    data = {'mykey': 'xxxxx'}
    files = {'myfile':open(r'D:\temp\abct.png','rb')}
##    response = requests.request("POST",url,files=files)
    response = requests.request("POST",url,data=data,files=files)
##    response = requests.post('http://127.0.0.1:8080/upload',files=files)
    print(response.text)
    

