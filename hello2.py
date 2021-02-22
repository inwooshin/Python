a = 1

print(type(a))
#타입에 대해서 나오게 하는 함수 type()

a= 1.23

print(type(a))

b = 4

print(a + b)
print(a * b)
print(a / b)

# 몫을 표현하려면 //, 나머지는 %!
print(a // b)

c = "hello python..!"
print(type(c))
print(c)

d = "python\"s favorite.."
print(d)

e = """와
이게
인식이
되네..?"""

print(e)

print(c + d)
print(d * 10)
print(d[0])
print(d[1])
print(d[2])
print(d[-1])
print(d[-2])
print(d[-3])

print(d[:8])
# 이상:미만:간격 이상에 안쓰면 처음, 미만에 안쓰면 끝까지
# 간격 안쓰면 default 1
print(d[:8:2])
print(d[::2])
print(d[::])
print(d[::-1])
print(d[::-2])

number = 10
day = "3일"
textAdd = "나는 %d일 째 다이어트를 진행중이고 현재 %s 째 아프고 있다." % (number, day)

print(textAdd)

test = "나는 {number2}일 째 다이어트를 진행중이고 현재 {day2} 째 아프고 있다.".format(number2 = 10, day2 = "3일")
print(test)

#몇번 째 인덱스에 째가 있는지 알 수 있음, 처음에 있는 것으로!
print(test.count("째"))

#없으면 -1 을 리턴함

a = ",".join('abcd')
print(a)

a = 1
print(a)