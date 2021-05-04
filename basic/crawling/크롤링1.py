from tkinter import messagebox
from urllib import request

import requests
from bs4 import BeautifulSoup

con = request.urlopen('http://www.naver.com')
# print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')
# print('2. 받은 것을 프린트', doc)
# doc 안에는 navercom의 첫페이지인 index.html파일의 소스가 통째로 들어있다.
a_nav = doc.select('a.nav')
for i in range(7,10):
    print(a_nav[i].text, end = ' ')