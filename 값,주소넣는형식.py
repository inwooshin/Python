# Immutable, Mutable 형식이 있다
# Immutable 은 정수 실수 문자열 튜플이 이에 해당한다.
#   - 이것은 아래와 같이 해도 a 의 값이 변하지 않는 값을 넘기는 경우이다.

# Immutable
a = 1
b = 1.0
c = "string"
d = (1,2,3)

def vartest(a,b,c,d):
    a = a + 1
    b = b + 1.0
    c += " is so dif"
    d = d * 3

vartest(a,b,c,d)

# 이렇게 값을 넘기기 때문에 변수의 값이 다들 변하지 않는다.
print(a,b,c,d)

#Mutable은 리스트 딕셔너리 집합이 이에 해당한다.
#Mutable
a = [1,2,3]
b = {1 : 'name', 2 : 'what?'}
c = {1,2,3,4}

def var(a,b,c):
    a.append(3)
    b[1] = 'other'
    c.add(5)

var(a,b,c)
#이렇게 여러가지 정보를 담고있는 경우 변수의 형을 넘기기 위해서 주소를 넘긴다
#튜플은 단 자물쇠를 건것으로 예외적으로 값을 넘긴다.

#그렇게 해서 값이 변화한다. 
print(a,b,c)