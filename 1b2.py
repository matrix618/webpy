#!/usr/bin/python
# coding=utf-8

import requests
import json

if __name__ == '__main__':
    url = 'http://172.16.213.46:8080/picturepath/'
    
    t1 = "'1234567890','mix_0.jpg','mix_1.jpg','mix_2.jpg',{'Container': '1234567890','Matteral': [1], 'Quality': 0.8, 'plate': 11}"
    t2 = "1"

    #
    strid=''
    pic1=''
    pic2=''
    pic3=''
    picjson=''

    tt1=t1
    
    f1 = tt1.find(',')
    strid = tt1[:f1]
    tt1=tt1[f1+1:]
    
    f1 = tt1.find(',')
    pic1 = tt1[:f1]
    tt1=tt1[f1+1:]

    f1 = tt1.find(',')
    pic2 = tt1[:f1]
    tt1=tt1[f1+1:]

    f1 = tt1.find(',')
    pic3 = tt1[:f1]
    
    picjson=tt1[f1+1:]

    print(strid)
    print(pic1)
    print(pic2)
    print(pic3)
    print(picjson)



    test = '?picpath=' + t1 + '&pictype=' + t2
    r = requests.get(url+test)
    print(r.status_code)
##    print(r.encoding)
##    print(r.apparent_encoding)
    r.encoding = 'utf-8'
    print(r.text)
