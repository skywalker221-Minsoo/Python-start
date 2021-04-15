me = {'이름':'hong', 'age':100, 'height':180.5} # 딕셔너리{키:값}
you = {'이름':'kim', 'age':90, 'height':170.5}

print(me['이름'])
print(me['age'])
print(me)
print(you)

he = dict()
he['name'] = 'song' # 빈 딕셔너리에 키:값 입력
he['age'] = 200
he['height'] = 130.4
he['weight'] = 100.5
print(he)

del he['height']
print(he)
print(len(he))

print(he.keys())
print(he.values())

for x in he:
    print(x, he[x])