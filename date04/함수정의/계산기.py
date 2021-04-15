# 함수의 입력값과 리턴값에 대한 타입은 지정하지 않는다!
# java와 다른 차이점

def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


if __name__ == '__main__':
    print('더한 결과>> ', add(1000, 200))
