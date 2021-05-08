# 집합은 파이썬에서만 있는 자료형이다.
# 중복을 허용하지 않는다.
# 순서가 없다.

#set 이 집합이라는 뜻이다.
s1 = set([1,2,3])
print(s1)
s1 = {1,2,3}
print(s1)

print(type(s1))

#list를 중복을 없애고 다시 리스트로 만들어 주는 방법
l = [1,2,3,3,3,4]
newList = list(set(l))

print(newList)

s = set("abc")
print(s)

# set 집합을 이렇게 설정해 놓을 때 중복을 알아서 없애준다.
s1 = {1,2,3,4,5,6,6}
s2 = {4,5,6,7,8,9,9}

print(s1)
print(s2)
print(s1 & s2)
print(s1.union(s2))
print(s1 | s2)
print(s1 ^ s2)

print("\n차집합")
print(s1 - s2)
print(s2 - s1)

print()
s1.add(99)
s1.update([7,8,9])
print(s1)

s1.remove(1)
print(s1)

