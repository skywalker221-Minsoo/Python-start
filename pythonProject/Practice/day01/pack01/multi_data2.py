hobby = []
# hobby.append('축구')
# print('갯수 :', len(hobby))
# hobby.append('코딩')
# print('갯수 :', len(hobby))

for i in range(0, 3): # 3번 입력 받아서 출력 하도록 함.
    data = input('당신이 하고싶은 취미는? ') # 취미 입력
    hobby.append(data) # append를 통해 원소 한개씩 추가
    print('취미의 갯수는? ', len(hobby)) # 배열의 갯수 출력
    print('취미는? ', str(hobby), end = ' ') # 배열의 원소 출력, 마찬가지로 옆으로 출력하기 위한 end
    print('취미는? ', list(hobby)) # str과 list 차이를 알아보기 위해 임의로 진행, append 이용 시 원소가 마지막 순번에
                                  # 추가되는지 궁금하여 진행

for x in hobby:
    print(x) # 입력받은 hobby 리스트 기본 출력