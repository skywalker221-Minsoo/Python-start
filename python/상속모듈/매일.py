class Day:
    program = None
    study_time = 0
    place = None
    count = 0

    def __init__(self, program, study_time, place):
        self.program = program
        self.study_time = study_time
        self.place = place
        Day.count += 1 # static 변수
        print(str(Day.count) + '개 객체가 생성됨')

    def study(self):
        return self.program + '를 ' + str(self.study_time) + '시간 하다.'
    def where(self):
        return self.place + '에서 ' + self.program + '를 하다.'
    def __str__(self):
        return 'study의 속성값들 : ' + self.program + ' ' + str(self.study_time) + '시간 ' + self.place


if __name__ == '__main__':
    day1 = Day('파이썬공부', 10, '강남')
    print(day1.study())
    print(day1.where())
    print(day1)
    day2 = Day('자바공부', 11, '신촌')
    print(day2.study())
    print(day2.where())
    print(day2)