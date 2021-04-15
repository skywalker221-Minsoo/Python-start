def login(id, name):
    print('아이디가 ' + id + '인 ' + name + '님이 로그인되었습니다.')

def cal(x, y):
    print('-----------------')
    print('두 수의 합은', x + y)
    print('두 수의 차는', x - y)
    print('두 수의 곱은', x * y)
    print('두 수의 나눗셈은', x / y)
    print('나누고서의 나머지는', x % y)

def age(name, age):
    age2 = int(age) + 10
    print(name + '의 10년 후의 나이는 ' + str(age2) + '세입니다.')

def allowance(money):
    if money >= 10000:
        print('엄마 너무 용돈이 많아요.')
    else:
        print('엄마 너무 용돈이 적어요.')

def odd(num):
    if num % 2 != 0:
        print('홀수입니다.')
    else:
        print('짝수입니다.')

def task(target):
    if target > 1000:
        print('축하합니다. 실적을 달성하셨습니다.!')
        print('당신의 이번달 보너스는 ' + str(int(target * 0.2)) + '만원입니다.')

def missile(name3, start_num, move_num):
    print('------------------------------')
    last_num = start_num + move_num
    print(name3 + ' 미사일이 ' + str(last_num) + '로 이동되었습니다.')

def receipt(money2, buy):
    print('받은 돈: ', money2)
    print('상품의 총액: ', buy)
    print('부가세: ', int(buy * 0.1))
    print('잔돈: ', money2 - buy)

def thousand_star():
    for x in range(20):
        print()
        for y in range(50):
            print('*', end='')