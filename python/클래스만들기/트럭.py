class Truck:

    ton = None
    company = None

    def move(self):
        print(str(self.ton) + '톤의 짐을 실어나르다.')
    def own(self):
        print(self.company + '회사 소속의 트럭입니다.')
    def __str__(self):
        return str(self.ton) + ', ' + self.company

print('---------------------------------')

if __name__ == '__main__':
    truck1 = Truck()
    truck1.ton = 3
    truck1.company = 'mega'
    truck1.move()
    truck1.own()
    print(truck1.ton)
    print(truck1.company)