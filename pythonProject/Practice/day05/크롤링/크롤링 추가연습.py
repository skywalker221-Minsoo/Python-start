from bs4 import BeautifulSoup
from urllib import request

def crawl(code):
    target = request.urlopen('https://finance.naver.com/item/main.nhn?code={0}'.format(code))
    document = BeautifulSoup(target, 'html.parser', from_encoding='euc-kr')

    company = document.select('div.wrap_company > h2 > a')
    price = document.select('em.no_up > span.blind')
    price2 = []
    ex_price = document.select('td.first > em > span.blind')
    ex_price2 = []

    for i in company:
        print("회사 : ", i.text)
        file = open(i.text + '.txt', 'w', encoding='utf-8')
        file.write(i.text + '\n')

    for j in price:
        price2.append(j.text)
    file.write(price2[0] + '\n')
    print("현재가 : ", price2[0])

    for k in ex_price[0]:
        ex_price2.append(k)
    file.write(ex_price2[0] + '\n')
    file.close()
    print('전일가 : ', ex_price2[0])

code = ['005930', '323990', '068270', '066570', '009900']

for i in code:
    crawl(i)
#
#
# con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930') #연결부품획득
# # print('1. 연결 성공', con)
# name = '삼성전자'
#
# doc = BeautifulSoup(con, 'html.parser')
# # print('2. 받은 것을 프린트 >> ', doc)
# #doc안에는 naver.com의 첫페이지인 index.html파일의 소스가 통째로 들어있음.
# span_code = doc.select('span.code') #검색의 결과를 리스트!!!
# # print('code의 개수>> ', len(span_code))
# code = span_code[0].text
# print('코드: ', code)
#
# # div_today = doc.select('div.today') #검색의 결과를 리스트!!!
# # # print(div_today[0])
# # today1 = div_today[0].select('span.blind') #검색의 결과는 리스트!!
# # print(today1[0])
# # print(today1[0].text)
#
# span_blind = doc.select('span.blind')
# #print(len(span_blind))
#
# # for index in range(len(span_blind)):
# #     print(index ,': ' , span_blind[index].text)
#
# # 전일, 고가, 시가, 저가
# # yes, high, low, start
# yes = span_blind[15].text
# print('전일: ', yes)
# high = span_blind[16].text
# print('고가: ', high)
# start = span_blind[19].text
# print('시가: ', start)
# low = span_blind[20].text
# print('저가: ', low)
#
# # all = doc.select('div.today span.blind')
# # print(len(all))
# # print(all[0])
#
# file = open(name + '.txt', 'w')
# file.write(code + '\n')
# file.write(yes + '\n')
# file.write(high + '\n')
# file.write(start + '\n')
# file.write(low + '\n')
# file.close()
