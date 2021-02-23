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

print(a)

a = 'abcd'
print(a.upper())

# 이렇게 할 경우에는 변수에 다른게 저장이 된다.
a = "life is too short".replace("life", "Your dog")
print(a)

# 이렇게 할 경우는 변수에 저장되지는 않는다 그래서
a = "life is too short"
# a = 을 추가해주면 바뀐 것이 변수에 할당된다.
a.replace("life", "Your dog");
print(a)

#default 짜르는 문자는 스페이스바, 그러나 다른걸로 변경가능
print(a.split())
b = a.split()
a = "l.o.v.e"

print(a.split('.'))

#이렇게 분리된 리스트를 받아서 출력할 수 있다.
print(b[:])

#list
a = ['신인우', '문채원', ['1', '2']]

print(a[0])
print(a[1])
print(a[2])
print(a[2][0])
print(a[2][1])

a = [1,2,3]
b = 4
b += a[0]
print(b)

a = [1,2,3]
b = [4,5,6]

#이렇게 하면 이어붙이기다!
print(a + b)

a += b
print(a)

# 0이상 3 미만!!!! 까지 인거 유의!
a[0:3] = [7,7,7]
print(a)
del a[0:3]
print(a)

#이거는 리스트의 주소를 넘기는 함수인가보다 리스트 변수가 바뀌어있다.
a.append(8)
a.append(8)
a.append(8)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

#첫번째로 8을 갖는 리스트 a 에 대한 인덱스를 반환한다.
print(a.index(8))

#0번째 인덱스에 4를 추가하자
a.insert(0,4)
print(a)

a.remove(8)
print(a)

# pop 은 맨 뒤의 인덱스부터 제거해줌
a.pop()
print(a)

a.pop()
print(a)

#4가 이 리스트에 몇개있는지
print(a.count(4))

#맨뒤에 추가
a.extend([1,2,3,4])
print(a)