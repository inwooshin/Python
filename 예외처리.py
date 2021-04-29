try:
    #오류가 발생할 수 있는 구문
    #4 / 0
    a = [1,2,3]
    a[3]
    #밑은 오류의 이름이다
    #Exception 은 모든 오류를 다 잡을 수 있음
except ZeroDivisionError as e:
    #오류가 발생했을 때 실행하는 구문
    #pass 로 넣어서 지나가게도 할 수 있음
    print("0으로 나누면 안됩니다...!")
except IndexError:
    print("인덱스 에러가 났습니다. 세그먼트 폴트!")
else :
    #오류 발생하지 않으면 실행하는 구문
    pass
finally:
    #무조건 마지막에 실행하는 구문
    print("-the end-")

class Bird :
    def fly(self):
        #fly 를 상속한 class 가 오버라이딩을 안하면 err 가 나니 무조건
        #오버라이딩 하세요 의 의미이다.

        #일부로 에러를 띄움
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()