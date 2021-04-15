import date05.SQL모듈.MySQL_BBSmodule as db

bbsid = input('아이디를 입력하세요. ')

db.delete(bbsid)