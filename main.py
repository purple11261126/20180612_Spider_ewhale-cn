# encoding: utf-8
'''
Created on 2018年6月12日

@author: Iris
'''


import requests  # requests 比 urllib 好用多了感觉，http://blog.csdn.net/gyq1998/article/details/78583841
import re
from lxml import etree  # XPATH
import numpy as np
import sqlite3
 
url = 'http://www.ewhale.cn/app-info/page/{}/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0', 
    'Accept-Encoding': 'gzip, deflate', 
    'Cookie': 'tencentSig=5878733824; IESESSION=alive; pgv_pvi=4979104768; pgv_si=s9902063616; _qddaz=QD.5w4en4.7gq81o.jibsjoug; _qdda=3-1.1; _qddab=3-ro9285.jibsjouj; _qddamta_4000600366=3-0', 
    'Connection': 'keep-alive'
    }
num_start = 2
num_end = 3  # 499

for num in np.arange(num_start, num_end):
    '''
        遍历所有文章列表页
    '''
    title_lis = []  # 存放标题
    content_lis = []  # 存放内容
    
    url_temp = url.format(num)  # 拼接 URL
    r = requests.get(url=url_temp, headers=header)  # 获取 HTML
    r.encoding = 'utf-8' # 设置编码，纠正乱码
    text_url_lis = re.findall('<li class="post-item">[\s\S]*?<a href="([\s\S]*?)">', r.text)  # 正则获取文章列表页中文章 URL
    for text_url in text_url_lis:
        '''
                遍历列表页中所有文章
        '''
        r_text = requests.get(url=text_url, headers=header)
        r_text.encoding = 'utf-8'
        
        # 使用正则获取标题和内容
#         title_lis.append(re.findall(pattern='<h1 class="post-title">([\s\S]*?)</h1>', string=r_text.text))
#         content_lis.append(re.findall(pattern='<article class="post-content">([\s\S]*?)<p class="tag-block">', string=r_text.text))
         
        # 使用 XPath 获取标题和内容
        html = etree.HTML(r_text.text)
        title_lis.append(html.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[1]/h1/text()'))
        '''
                现在缺少文章中 URL 里的文字，获取内容时，怎么用 XPATH 获取所有子节点（包括嵌套的）？？string()。
        | 符号只能连接两个条件？？
        '''
        content_lis.append(html.xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[1]/article/p[not(@class='tag-block')]/text() | /html/body/div[1]/div[3]/div[2]/div/div/div[1]/article/ul/li/text()"))
    
    # 写入SQLite
    conn = sqlite3.connect('./ewhale.db')  # 连接、创建数据库
    cur = conn.cursor()  # 创建游标
    for title, content in zip(title_lis, content_lis):
        '''
                    现在写入的都是列表，怎么转成 string 写入？？
        '''
        cur.execute('INSERT INTO text(title, content) VALUES ("{}", "{}")'.format(title, content))  # 写入变量
        conn.commit()
    
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接




    
    

