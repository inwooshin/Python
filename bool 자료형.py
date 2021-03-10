a = 2

if a == 3 :
    print(a)
else :
    print("응?")

while a != 10:
    a += 1
    print(a)

a = True

if a :
    print(a)
else :
    print("오오옹...?")

# 문자열이 있으면 참인 속성을 가지고 있다. 비어있으면 거짓이다.
# 문자열이 있으면 참, 리스트 튜플 집합이 있으면 참
# none 이면 거짓이고, 리스트나 튜플 집합이 비어있으면 거짓이다.

#집합 시
s1 = {1,2,3}
s2 = {}
if s1 :
    print(s1)
if s2 :
    print(s1)
else :
    print('false')

#튜플 시
s1 = (1,2,3)
s2 = ()
if s1 :
    print(s1)
if s2 :
    print(s1)
else :
    print('false')

#리스트 시
s1 = [1,2,3]
s2 = []
if s1 :
    print(s1)
if s2 :
    print(s1)
else :
    print('false')

#문자열 시
str1 = "string"
str2 = ""
if str1 :
    print(str1)
if str2 :
    print(str2)
else :
    print('false')

# 이렇게 빌때까지 true 조건문으로 사용할 수 있음
a = [1,2,3,4]
print(a)
while a :
    print(a.pop())
    print(a)