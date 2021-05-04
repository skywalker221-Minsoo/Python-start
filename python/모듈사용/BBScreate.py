import date05.SQL모듈.MySQL_BBSmodule as db

bbsid = input('아이디를 입력하세요. ')
title = input('패스워드를 입력하세요. ')
content = input('이름을 입력하세요. ')
writer = input('전화번호를 입력하세요. ')

data = (int(bbsid), title, content, writer)

db.create(data)