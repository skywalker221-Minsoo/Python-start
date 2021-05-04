from date05.상속모듈.사람모듈 import *

# 상속할 때는 생성자를 생성해 주면 많이 피곤해진다... 일단은 밑에다가 입력을 하는것으로 익숙해지자!
class Student(Person):
    subject = None
    score = 0

    def study(self):
        return self.name + '가 ' + str(self.age) + \
               '살이기 때문에 개빡세게 공부해서 ' + self.subject + '과목에서 ' + \
               str(self.score) + '점을 맞았다.'

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + str(self.subject) + ' ' + str(self.score)

class Worker(Person):
    major = None

    def work(self):
        return self.name + '는 ' + str(self.age) + \
               '살 즈음에 ' + self.major + '으로 먹고살 궁리를 했다.'

    def __str__(self):
        return '이름 : ' + self.name + \
               ' 나이 : ' + str(self.age) + \
               ' 전공 : ' + self.major

    company = None

    def destination(self):
        return self.name + '는 ' + self.company + '에 결국 입사하지 못했다.'

if __name__ == '__main__':
    student1 = Student()
    student1.name = '민수'
    student1.age = 28
    student1.subject = '데이터분석'
    student1.score = 80
    print(student1)

    print(student1.study())

    worker1 = Worker()
    worker1.name = '민수'
    worker1.age = 26
    worker1.major = '전자공학'
    print(worker1)

    print(worker1.work())

    worker1.company = 'CJ'
    print(worker1.company)
    print(worker1.destination())