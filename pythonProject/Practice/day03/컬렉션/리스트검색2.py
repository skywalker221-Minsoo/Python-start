member = ['a110', 'b230', 'c340']

for code in member:
    print('code: ', code)
    dept = code[0]
    roll = code[1]
    result = ''

    for i in range(len(code)):

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
