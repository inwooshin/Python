a = 'what is \'result\'??'

print(a)
#문자열은 변경할 수 없는 값으로 이루어져있다!

print('Hello' + ' ' + 'World')

print('String' * 3)

#튜플! 리스트와 유사하지만 변경 불가능!
a = dict()

a['사과'] = 'apple'
a['바나나'] = 'banana'

print(a)

#이런식으로 하면 검사가 가능하다
if '사과' in a:
    print('사과의 데이터가 존재합니다!')

#but 이런식으로 하면 검사가 불가능하다!
if 'apple' in a:
    print('사과의 데이터가 있')

#요렇게 키만 뽑아서 values 만 뽑아서 사용할 수 있다.
print(a.keys())
print(a.values())

#이렇게 사전은 변경이 가능한 자료 구조이다!
#a['사과'] = 1
#print(a)

#요런식으로 사전 자료형의 key 값을 받아와서 쭈욱 넣을 수 있다! 그것도 순서대로!
for key in a.keys():
    print(a[key])

#이런식으로도 사전 자료형을 선언할 수 있다!
b = {
    '사과' : 'apple',
    '바나나' : 'banana'
}
print(b)

#이렇게 하면 list의 형태로 나타난다.
print(list(b))

print(b['사과'])

#집합 자료형! 밑의 두개로 생성이 가능하다!
data = set({1,2,3,4,4,5})
print(data)

data = {1,2,3,4,4,5}
print(data, '\n')

data2 = {3,4,5,6,7}

#배열 a b
print('배열 a : ', data, ', 배열 b : ', data2, '\n')
#합집합
print('합집합 : ', data | data2)
#교집합
print('교집합 : ', data & data2)
#차집합
print('차집합(a - b) : ', data - data2)