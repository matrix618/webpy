#!/usr/bin/python
# coding=utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/picturepath/'
    test = '?picpath=444&pictype=yyy'
    r = requests.get(url+test)
    print(r.status_code)
##    print(r.encoding)
##    print(r.apparent_encoding)
    r.encoding = 'utf-8'
    print(r.text)

    

