'''
Hit = 0
gi = 0
while Hit < 10:
    Hit += 1
    # 한 꺼번에 넣으려면 튜플을 써주면 된다!!
    print("나무를 %d, %d 번 찍었습니다" % (Hit, gi))
    if(Hit == 10):
        print("나무가 넘어갑니다!")
'''

test = ['one', 'two', 'three']
for i in test:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    # 이렇게 기본 디폴트를 변경할 수 있..?
    print("%d번 학생은 합격입니다." % number, end = " * ")

# a 안의 num 을 for 문에 따라 하나씩 돌면서 if 조건을 만족하는 애들을 num * 3 해서 
# result 에 append 해준다.
a = [1,2,3,4,5,6,7]
result = [num * 3 for num in a if num % 2 == 0]

print()
print(result)

result = [i + j for i in range(1,10) for j in range(1, 10)]
print(result)