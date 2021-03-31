#Hash, Map, Object, JSON 이 딕셔너리 형태이다
''' 이런 방식을 JSON 객체라고 한다. 이는 API 에서 자주 사용된다.
{
    "이름" : 신인우
    "대학교" : 명지대학교
    "취미" : 농구
}
'''

dic = {'name' : '신인우', 'age' : 15}

print(dic['name'])

a = {1 : 'a'}
# 이렇게 map 형식으로 값 추가 가능 근데 이전에 있던 키의 형식 값의 형식 쌍이 달라도
# 추가가 가능하다
a['name'] = "익명"

print(a)

del a['name']

print(a)

a = {1 : '잉' , 1 : 'twice...!', '뭐라고?' : 1, "이게 된다고?" : '대박'}

print(a[1])

print(a.keys())

print(a.values())

#튜플 형태로 쌍을 담을 수 있음
print(a.items())

#대박입니다.
for k in a.keys():
    print(k)

a['말도 안돼'] = 200.22

for k in a.keys():
    print(k)

for k in a.values():
    print(k)

b = {1 : "사과", 2 : '귤', 3 : '파인애플'}
for k, v in b.items():
    print("키 : " + str(k))
    print("밸루 : " + v)

# a.clear() 초기화 하기
# print(a[33]) 이거는 에러가 남 그런데 get 으로 접근하면 없으면 None 을 출력
print(a.get(33))
print(a.get(3, '없어용..★'))
print(b.get(3, '없어용..★'))

# bool 을 리턴하게 함, 4가 a 안에 있니..? 있으면 true 없으면 false 리턴해주라.
print(4 in a)

