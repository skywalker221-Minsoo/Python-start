# # 일단 목표는 단순 입력 보다 반복문을 이용해서 여러번 넣어볼수 없나 생각해서 인터넷 참고해가면서 해봤습니다.
#
dict_dict = [] # 비어있는 리스트 안에다가 딕셔너리 값을 계속 넣을수 있도록 합니다. append를 이용해보려고함.
while True:
    sel = int(input('1번은 딕셔너리 생성, 2번은 종료: '))
    if sel == 1:
        print("====딕셔너리 요소 추가중====")
        my_dict = {} # 이게 딕셔너리 요소를 추가하려는 공간
        while True:
            key = input('키 입력: ')
            value = input('밸류 입력: ')
            my_dict[key] = value # 키:값 대응
            con = int(input('1번은 딕셔너리 생성, 2번은 종료: ')) # 추가로 딕셔너리 안에 요소를 더 넣을건지?
            if con == 2:
                print('종료합니다.')
                break
        dict_dict.append(my_dict) # 지금까지 저장된 딕셔너리 요소 저장
    elif sel == 2:
        print('종료합니다')
        break
    else:
        print('잘못 선택하셨습니다.')
        break
print('리스트 :', dict_dict)
