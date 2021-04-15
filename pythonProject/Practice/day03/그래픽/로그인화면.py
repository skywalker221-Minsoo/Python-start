from tkinter import *
from tkinter import messagebox



# 버튼을 눌렀을 때 로그인 기능을 처리해야함.
# 특정한 기능은 하나의 함수로 만들어주면 됨:
# 버튼 눌렀을 때 처리하고자 하는 기능 하나는 함수 하나가 됨:
# 함수를 만드는 것을 함수를 정의한다 라고 함.
# 기능을 프로그래머가 정의하기 때문에 함수를 정의한다 라고 표현함.


def login():

    id2 = id_entry.get()
    print('입력한 id는 ', id2)
    pw2 = pw_entry.get()
    print('입력한 pw는 ', pw2)
    if id2 == 'root' and pw2 == '1234':
        messagebox.showinfo('로그인성공', '축하합니다.')
        y = Tk()
        y.geometry("500x250")
        id = Label(y, text='로그인을 축하합니다.', font=('바탕', 10))
        id.pack()
    else:
        y = Tk()
        y.geometry("500x250")
        id = Label(y, text='다시 정보를 확인해주세요.', font=('바탕', 10))
        id.pack()

w = Tk()
w.geometry("500x250")

id = Label(w, text='ID입력', font=('궁서', 20))
id.pack()

id_entry = Entry(w, font=('바탕', 10), bg='blue', fg='white')  # 위에 창 만들기, bg=면색, fg=글자색
id_entry.pack()

pw = Label(w, text='PW입력', font=('궁서', 20))
pw.pack()

pw_entry = Entry(w, font=('바탕', 10), bg='blue', fg='white') # 아래에 창 만들기
pw_entry.pack()

b = Button(w, text='로그인', font=('궁서', 20), bg='yellow', command=login) # 로그인 버튼 누르면 login 함수가 작동
b.pack()

w.mainloop()