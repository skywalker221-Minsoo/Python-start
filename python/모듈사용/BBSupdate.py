import date05.SQL모듈.MySQL_BBSmodule as db

bbsid = input('아이디를 입력하세요. ')
writer = input('작가를 입력하세요. ')

db.update(bbsid, writer)