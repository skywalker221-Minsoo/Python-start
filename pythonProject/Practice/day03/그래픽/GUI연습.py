from tkinter import *
import tkinter.messagebox

def login():
    id2 = id_entry.get()
    print('입력한 id는 ', id2)
    pw2 = pw_entry.get()
    print('입력한 pw는 ', pw2)
    if id2 == 'root' and pw2 == '1234':
        print('로그인 되었습니다.')
    else:
        print('정보를 다시 확인하시기 바랍니다.')

w = Tk()
w.geometry("300x500")

sub = Label(w, text='항목', font=('바탕', 10), bg='green', fg='white', width=9)
sub.grid(row=0, column=0)

ent_entry = Label(w, text='입력', font=('바탕', 10), bg='green', fg='white', width=17) # 아래에 창 만들기
ent_entry.grid(row=0, column=1)

number = Label(w, text='번호', font=('바탕', 10), bg='white', fg='blue', width=9)
number.grid(row=1, column=0)
number_entry = Entry(w, font=('바탕', 10), bg='pink') # 아래에 창 만들기
number_entry.grid(row=1, column=1)

subject = Label(w, text='제목', font=('바탕', 10), bg='white', fg='blue', width=9)
subject.grid(row=2, column=0)
subject_entry = Entry(w, font=('바탕', 10), bg='pink') # 아래에 창 만들기
subject_entry.grid(row=2, column=1)

content = Label(w, text='내용', font=('바탕', 10), bg='white', fg='blue', width=9)
content.grid(row=3, column=0)
content_entry = Entry(w, font=('바탕', 10), bg='pink') # 아래에 창 만들기
content_entry.grid(row=3, column=1)

writer = Label(w, text='작성자', font=('바탕', 10), bg='white', fg='blue', width=9)
writer.grid(row=4, column=0)
writer_entry = Entry(w, font=('바탕', 10), bg='pink') # 아래에 창 만들기
writer_entry.grid(row=4, column=1)

writing = Label(w, width=10, bg='yellow')
writing.grid(row=5, column=0)
writer = Label(w, width=20, bg='yellow')
writer.grid(row=5, column=1)

# b = Button(w, text='글쓰기 완료', font=('바탕', 10), bg='white', fg='green', command=login) # 로그인 버튼 누르면 login 함수가 작동
# b.grid(row=5, column=1)

w.mainloop()