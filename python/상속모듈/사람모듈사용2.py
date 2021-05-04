from date05.상속모듈.사람모듈 import *
import date05.상속모듈.매일 as my

class WomanDay(Person, my.Day): #다중상속 가능, 다만 멤버변수가 기하급수적으로 늘어날 수도 있다.
# 파이썬: 클래스간 다중 상속이 가능하다.
# 자바: 클래스간 단일상속만 가능하다.

    def __init__(self, program, study_time, place):
        my.Day.__init__(self, program, study_time, place)

    def free(self):
        print('쉬다!')

    def __str__(self):
        return self.program + ', ' + str(self.study_time) + ', ' + self.place
if __name__ == '__main__':
    woman_day1 = WomanDay('진짜 놀기', 20, '마포구')
    print(woman_day1)
    # woman_day1.free()
    # woman_day1.eat()