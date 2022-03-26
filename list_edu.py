#리스트 컴프리헨션!
a = [i for i in range(100)]

print('기본 : ', a, '\n')

a = [i for i in range(100) if i % 2 == 1]

print('홀수 : ', a, '\n')

a = [i for i in range(100) if i % 2 == 0 and i != 0]

print('짝수 : ', a, '\n')

#리스트 그냥 대입하기
b = a
print('대입한 b : ', b, '\n')

#2차원 리스트!
#이렇게 할 경우에는 10개의 배열 10개가 이중으로 쭈욱 만들어진다
m, n = (10, 10)
#for _ in range(100) 은 앞서 있는 변수를 사용하겠다는 말이다!
array = [[0] * m for _ in range(n)]

#밑처럼 해줄 경우에도 리스트가 잘 선언이 되지만
arrayFault = [[0] * m] * n

#print('2차원 리스트 : ', array)
#print('2차원 리스트 Fault : ', arrayFault)

#이런식으로 할경우 fault 식으로 선언한 경우는 내부의 10개의 리스트가 다 바뀐다.
#그래서 사용에 유의해야한다!
array[0][1] = 1
arrayFault[0][1] = 1
#print('2차원 리스트 : ', array)
#print('2차원 리스트 Fault : ', arrayFault)

#응용!
#만약에 행이 4, 열이 3인경우의 2차원 리스트를 만들라고 한다면
a = [[0] * 3 for _ in range(4)]
print('4 * 3 - 2차원 리스트 \n', a)

#요런식으로 i 를 사용하지 않을 수 있다!
for _ in range(5):
    print('hello')

a = [1,2,3]

#요럴 경우에는 첫번째 인덱스로 호출하게 되는 a[1] 에 들어가게 되는것이다
#따라서 a == [1,10,2,3] 이 된다.
a.insert(1,10)

if a == [1,10,2,3]:
    print(True)
else :
    print(False)
    
#특정 값 리스트에서 삭제!
a = [1,2,3,3,3,4,5,5,5]
b = [1,2]
c = {3,5}

#해당 c에 없는 원소이면서 b에는 있는 요소일 경우에만 남겨놔라!
a_remove = [i for i in a if i not in c and i in b] #b 또는 c 둘다 사용가능!

print(a_remove)