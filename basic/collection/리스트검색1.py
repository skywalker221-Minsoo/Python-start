# special_no = '940221-1410923'
# year = special_no[0:2]
# year2 = int(year)
# age = 2021-(1900+year2)
# print(age)
#
# gender = special_no[7]

# say = '시작은 미미했으나 끝은 창대하리라'.split() # say = ['시작은', '미미했으나', '끝은', '창대하리라']
# i = say.index('미미했으나')
# n = say.count('창대하리라')
# print(say, i, n)
# 순차문의 구조 : 입력 > 처리 > 출력
# 입력
# 들여쓰기 : indent
while True:
    code = input('본인의 사원번호를 입력하세요. 종료)x>> ')
    if code == 'x':
        print('시스템을 종료합니다.')
        break
    dept = code[0]
    roll = code[1]
    my_no = code[2:]
    result = ''

    if dept == 'a':
        result = '기획부'
    elif dept == 'b':
        result = '개발부'
    elif dept == 'c':
        result = '인사부'
    else:
        print('\n해당 부서가 존재하지 않음.')

    if roll == '1':
        result = result + " " + "사장"
    elif roll == '2':
        result = result + " " + "팀장"
    elif roll == '3':
        result = result + " " + "사원"
    else:
        print('\n해당 부서가 존재하지 않음.')

    print('당신은', result)
