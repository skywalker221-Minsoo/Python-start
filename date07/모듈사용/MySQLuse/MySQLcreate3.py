import date05.SQL모듈.MySQL연결모듈 as db

# id = input('아이디를 입력하세요. ')
# pw = input('패스워드를 입력하세요. ')
# name = input('이름을 입력하세요. ')
# tel = input('전화번호를 입력하세요. ')

data1 = ("data1","data1","data1","data1") #vo역할
data2 = ("data2","data2","data2","data2") #vo역할
datas = (data1, data2) #tuple의 tuple을 만들어준다.
print('입력된 데이터들', datas)
db.create3(datas)