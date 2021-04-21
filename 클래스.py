class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FoulCal:
    #여기서 init 은 클래스를 만들때 바로 실행하게 해주는 아두이노의 setup
    # 같은 함수이다.
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, fisrt, second):
        self.first = fisrt
        self.second = second
        self.anggimotti = 33

    def add(self):
        result = self.first + self.second
        return result

#클래스 안에 있는 함수를 method 라고 부른다.
a= FoulCal(2,3)
print(type(a))

#아래와 같이 할 경우 a 는 self 에 2,3 은 first, second 에 들어간다.
print(a.add())
print(a.first)
print(a.second)

