a = [1,2,3]

#여기서 a가 할당되어있는 실질적인 값의 주소를 b에 넣어준 것이기 때문에
# a의 값을 바꿈은 주소로 들어가서 값을 바꾸는 것이라 b 또한 바뀐다.
b = a

print(a)
print(b)

a[1] = 55

print(a)
print(b)

b[1] = 44

print(a)
print(b)

print(id(a))
print(id(b))

# 같은 곳을 바라보고 있니? bool 로 리턴함
print(a is b)

#이렇게 각각으로 주면 새로운 리스트가 생겨서 들어간다.
#b = a[:]

# 이렇게도 가능하다
from copy import copy
b = copy(a)

print(a)
print(b)

a[1] = 55

print(a)
print(b)

b[1] = 33

print(a)
print(b)

print(id(a))
print(id(b))
print(a is b)

#공간 할당 하는 법
a,b = ('python', 'life')

print(a)
print(b)

a,b = ['python', 'life']

print(a)
print(b)

a, b = 'python', 'life'

print(a)
print(b)

[a,b] = ['python', 'life']

print(a)
print(b)

a = b = 'hello'

print(a)
print(b)

#일반적으로 값을 치환하는 과정
a = 3
b = 5

tmp = b
b = a
a = tmp
print(a)
print(b)

#파이썬 방식
a = 3
b = 5
a, b = b, a
print(a)
print(b)