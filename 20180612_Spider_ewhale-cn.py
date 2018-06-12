# encoding: utf-8
'''
Created on 2018年6月12日

@author: Iris
'''

import urllib
import requests

# # 爬取一个 URL 
# url = 'http://www.ewhale.cn/app-info/'
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0', 
#     'Accept-Encoding': 'gzip, deflate', 
#     'Cookie': 'tencentSig=5878733824; IESESSION=alive; pgv_pvi=4979104768; pgv_si=s9902063616; _qddaz=QD.5w4en4.7gq81o.jibsjoug; _qdda=3-1.1; _qddab=3-ro9285.jibsjouj; _qddamta_4000600366=3-0', 
#     'Connection': 'keep-alive'
#     }
# request = urllib.request.Request(url=url, headers=header)
# response = urllib.request.urlopen(url=request)
# print(response.read())