#tuple, 소괄호로 되어있음 const 의 배열이라고 생각하면됨!
t1 = (1,2,3,4)
#del t1[0] 이렇게 지우기 불가
#t1[0] = 2 이것도 안됨

print(t1[0:2] )
print(t1[0:2] * 3)

t2 = (5,6,7,8)

print(t1 + t2)

#변화하지는 않고 따로 따로 나눌 수 있음
print(t1)
print(t2)

t1 = t1 * 3
print(t1)