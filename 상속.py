class FoulCal:
    #여기서 init 은 클래스를 만들때 바로 실행하게 해주는 아두이노의 setup
    # 같은 함수이다.
    # 이는 self.first 를 정의해 준것과 같다!
    first = 2
    second = 3
    # def __init__(self, first, second):
    #     self.first = first
    #     self.second = second
    
    def setdata(self, fisrt, second):
        self.first = fisrt
        self.second = second
        self.anggimotti = 33

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class SafeDiv(FoulCal):
    #동일한 이름의 함수를 재정의하면 자식의 함수가 호출된다!
    #메서드 오버라이딩 덮어쓴것이다!
    def div(self):
        if self.second == 0:
            return 0
        else :
            return self.first / self.second

a = SafeDiv()
b = SafeDiv()
print(a.first)
print(a.second)
print(a.div())
print(b.first)
print(b.second)
print(b.div())

class Family:
    lastname = "김"

#이렇게 해서 클래스의 구조 자체를 변경할 수 있다.
Family.lastname = "박"
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)