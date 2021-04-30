def sum(a,b):
    result = a + b
    return result

def say():
    print("say!")

#이렇게 하면 몇개든 상관 없이 한번에 다 받을 수 있다.
def sum_many(*a):
    sum = 0
    for i in a:
        sum = i + sum
    return sum

# 이렇게 설정해주면 키워드와 동시에 value 를 입력해줄 수 있다.
# 이는 dict 형태이다.
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 : " + k)

#이렇게 리턴 값이 여러가지일 경우에는 tuple 형식으로 return 한다.
def sum_and_mul(a, b):
    return a + b, a * b, a -b
print(sum(33,55))

say()

l1 = [1,2,3]
# 어펜드 함수는 return 이 없기 때문에 출력이 안됨
print(l1.append(4))

# pop 함수는 return이 있기 때문에 출력이 가능
print(l1.pop())

#이렇게 하면은 
print(sum_many(1,2,3,4))

print_kwargs(name = "in's my name")

print(sum_and_mul(2,3))

#더한 값만 쓸 경우
print(sum_and_mul(2,3)[0])
#곱한 값만 쓸 경우
print(sum_and_mul(2,3)[1])
#뺀 값만 쓸 경우
print(sum_and_mul(2,3)[2])

#디폴트로 설정 가능
def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다" % name)
    print("나이는 %d 입니다" % old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")

say_myself("신인우", 26)
#이렇게 밑에 처럼 따로 설정가능
say_myself("신인우", 26, False)

#이렇게 매개변수의 순서를 바꿔서 넣어줄 수도 있음
say_myself(old = 26, name = "신인우", man = False)
#대신 아래와 같이하면 err 가 날 수 있다. 다른 것들은 뒤죽박죽되서 변수 가이드를
#넣었는데 man 만 안넣어줘서 그렇다.
#say_myself(old = 26, name = "신인우", False)

a = 1
#여기서 변수는 새로운 메모리 공간을 만들어서 함수안에서만 쓴다.
def var():
    # 이렇게 하면 전역변수를 가져올 수 있다.
    # 여기서 매개변수랑 global 변수랑 이름이 겹치면 err 난다 조심!
    global a
    a += 1
    return a

print(var())
print(a)

# lambda 를 사용해서 축약해서 함수를 표현할 수 있다.
a = lambda a, b : a + b

print(a(3,4))

#이렇게 하면 함수를 list 형식으로 가질 수 있다.
mlist = [lambda a, b : a+ b, lambda a, b : a - b]

#호출 시에 이렇게 쓸 수 있다.
print(mlist[0](3,4))
print(mlist[1](3,4))