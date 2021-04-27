import tkinter
from tkinter import *
import threading
import time
import random

# 스레드 클래스
class Thread:
    # car, thread 타입은 상관없이 오도록 None으로 선언
    car = None
    thread = None

    def __init__(self, w, img, x1, y1): #생성자
        # 이미지 할당
        self.car = Label(w) # car에 입력된 변수들이 tk창에 뜨도록 함.
        icon1 = PhotoImage(file=img) # 폴더 아래 이미지 파일들을 가져옴.
        icon2 = PhotoImage(file=img)
        icon3 = PhotoImage(file=img)
        self.car.configure(image=icon1) # 경기 시작을 눌렀을 때 자동차 이미지를 tkinter 상자 내에 바뀌도록 한다.
        self.car.configure(image=icon2)
        self.car.configure(image=icon3)
        self.car.image = icon1 # 자동차의 image는 Cars 메서드에서 가져온 이미지를 생성자 안에 넣어준다.
        self.car.image = icon2
        self.car.image = icon3
        # 스레드 설정
        self.thread = threading.Thread(target=self.run, args=(self.car, x1, y1))
        # 스레드 실행 함수인 run을 사용한다. 그리고 run에 사용되는 변수들을 입력.
        # tkinter를 이용해서 스레드 기능을 이용함. run 함수를 이용해서 그림이 움직이도록 함.
        # Cars 함수에서 이미지, x좌표, y좌표를 가져온다. 그리고 입력된 이미지, x좌표, y좌표를 생성자함수안에 필요한 곳에 변수를 받아준다.
        # 스레드 함수안에도 target을 이용해 run함수를 불러오고, 거기에 필요한 변수들을 args로 받아줌.
        self.thread.start() # 스레드 시작

    # 스레드 실행 함수
    def run(self, car, x1, y1):
        speed = 0
        while True:
            speed = random.randrange(10, 50)  # 한 번에 10~50 사이로 움직임
            if x1 >= 500:  # 골인 지점
                break
            x1 = x1 + speed #이동한 거리 누적
            self.car.place(x=x1, y=y1)  # 자동차 이미지의 초기 위치 설정.
            time.sleep(0.5)  # 대기시간 0.5초마다 speed거리 만크뭉ㅁ직인다.


# 자동차 배치
def Cars():
    # 창, 파일명, x좌표, y좌표
    car1 = Thread(w, 'carimage1.png', 10, 70)
    car2 = Thread(w, 'carimage2.png', 10, 180)
    car3 = Thread(w, 'carimage3.png', 10, 300)


# 메인코드
if __name__ == '__main__':
    # 윈도우 배치
    w = Tk()
    w.title('자동자 경주')
    w.geometry('900x600')
    # 버튼 배치
    startbutton = Button(w, text='경기 시작', command=Cars) # 경기시작 버튼 생성. Tkinter 박스 안에.
    startbutton.pack(side=TOP, fill=X, ipadx=3, ipady=3, padx=5, pady=5)
    #pack(윈도우 창 위로 정렬, X축으로 start button을 가득 채움, 내부padding(ipadx,y) 3px, 외부padding(padx,y) 5px씩)
    w.mainloop()
