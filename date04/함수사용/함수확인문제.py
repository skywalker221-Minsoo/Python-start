from date04.함수정의.문제함수 import *

id = input('id 입력 ' )
name = input('이름 입력 ')
login(id, name)

x = int(input('숫자1: '))
y = int(input('숫자2: '))
cal(x, y)

name2 = input('이름: ')
now_age = input('나이: ')
age(name2, now_age)

for _ in range(2):
    money = int(input('하우 머치 유 테이크 머니? '))
    allowance(money)

for _ in range(2):
    num = int(input('숫자 입력: '))
    odd(num)

target = int(input('실적을 입력하세요>> '))
task(target)

name3 = input('미사일 이름은: ')
start_num = int(input('미사일 시작값은: '))
move_num = float(input('미사일 움직이는 값은: '))
missile(name3, start_num, move_num)

money2 = int(input('받은 돈: '))
buy = int(input('상품의 총액: '))
receipt(money2, buy)

thousand_star()