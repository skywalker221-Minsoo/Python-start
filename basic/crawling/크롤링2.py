from tkinter import messagebox
from urllib import request

import requests
from bs4 import BeautifulSoup

con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930')
# print('1. 연결 성공', con)

doc = BeautifulSoup(con, 'html.parser')
# print('2. 받은 것을 프린트', doc)
# doc 안에는 navercom의 첫페이지인 index.html파일의 소스가 통째로 들어있다.
# span_code = doc.select('span.blind')
# print('span의 갯수 : ', len(span_code))
#
# for i in range(len(span_code)):
#     code = span_code[i]
#     print('code: ', code.text)

div_code = doc.select('div.today') # doc에서 div ㅡ> today 속성을 가진 단일 개체를 뽑아옴. select는 단일 개체를 선택하는것.
print('div의 갯수 : ', len(div_code))
print(div_code)

today1 = div_code[0].select('span.blind') # div_code에서 span ㅡ> blind 속성을 가진 단을 개체를 뽑아옴.
print(today1)    # [<span class="blind">83,800</span>, <span class="blind">100</span>, <span class="blind">0.12</span>]
print(today1[0]) # <span class="blind">83,800</span>

span_blind = doc.select('span.blind')

for i in range(len(span_blind)):
    code = span_blind[i]
    print(i+1, ':', code)