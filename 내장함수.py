print(abs(-3))

#모두 참인지 검사하는 함수
print(all([1,2,3]))

#하나라도 참이 있는지 확인하는 함수
print(any([1,2,3,0]))

#33부터 아스키코드는 문자가 있음
for i in range(33,128):
    print(chr(i))

# 이러한 리스트 형식에서 어떠한 함수를 사용할 수 있는지 알려줌
print(dir([1,2,3]))
a = 1
print(dir(a))

#몫과 나머지를 튜플 형태로 return
print(divmod(7,3))

#인덱스랑 같이 열거해주는 함수
for i, name in enumerate(['body','all','82bars']):
    print(i, name)

#eval 함수는 string으로 되어있는 명령어를 실행하고 결과값을 돌려준다.
print(eval('3 + 5'))

#filter 함수는 함수를 통과하여 참인 것 만을 돌려줌
a = [1,2,3,4,5,6,0,0,2,2,3]
a = list(filter(lambda x : x > 0, a))
print(a)

# map 함수는 각 요소가 수행한 결과를 돌려준다.
a = list(map(lambda x : x * 2, [1,2,3,4]))
print(a)

# max, min 함수는 문자열 또한 인덱스로 하나하나 비교해가면서 
# 최대, 최소값을 구해준다.

print(pow(2,4))

#round 는 반올림 함수이다.
print(round(2.5))
