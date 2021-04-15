from tkinter import messagebox
from urllib import request

import requests
from bs4 import BeautifulSoup

name_list = ['삼성전자', '카카오', '현대자동차']
code_list = ['005930', '035720', '005380']
for index in range(len(code_list)):
    con = request.urlopen('https://finance.naver.com/item/main.nhn?code=' + code_list[index])

    doc = BeautifulSoup(con, 'html.parser')

    span_code = doc.select('span.code')
    code = span_code[0].text
    # print('코드 :', code)

    span_blind = doc.select('span.blind')  # doc에서 div ㅡ> today 속성을 가진 단일 개체를 뽑아옴. select는 단일 개체를 선택하는것.

    # print(span_blind)

    yes = span_blind[15].text
    print('전일 :', yes)
    #
    high = span_blind[16].text
    print('고가 :', high)

    low = span_blind[19].text
    print('저가 :', low)

    start = span_blind[20].text
    print('시가 :', start)

    file = open(name_list[index] + '.txt', 'w')
    file.write(high + '\n')
    file.write(low + '\n')
    file.write(start + '\n')
    file.write(yes + '\n')
    file.write(code + '\n')
    file.close()
    print(name_list[index])
    print()
    print('--------------------------------')