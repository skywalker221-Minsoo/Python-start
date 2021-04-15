food = ['아이스크림', '아이스아메리카노', '생수'] # 목록(list)
# hobby = []

for i in range(0, len(food)): # food 라는 list에 대해 list 원소 갯수만큼 반복
    print(food[i], end = ' ') # 아래로 내려가는 결과 출력이 아래로 내려가기 때문에 옆으로 가기 위해 end 처리

print() # end 처리때문에 다음 출력이 옆으로 되지만 print 출력을 해줌으로써 다음 결과물은 아랫줄에 출력

for x in food: # for-each, food 라는 원소 갯수만큼 반복
    print(x, end = ' ') # 첫번째 원소부터 차례로 출력, end는 옆으로 출력

print() # 위의 print 와 동 사유
print('목록의 갯수는', len(food)) # list 원소 갯수만큼 출력
################
Have_To_Do = ['운동', 'ADsP', 'SQLD', '복습', '일본어'] # list 설정
for i in range(0, 5): # 5개 이므로 5번 반복
    print(Have_To_Do[i], end = ' ') #

print()

for x in Have_To_Do: # for-each
    print(x, end = ' ')

print()
print('목록의 갯수는', len(Have_To_Do))
