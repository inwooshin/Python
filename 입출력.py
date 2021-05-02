#입력을 받는 함수이다.
#a = input()
#a = input("여기에 숫자를 넣어주세요 : ")

print("life " "is " "short")

a = "life"
b = "is"
c = "short"

# sep 를 없애주면 기존의 변수를 분별하기 위한 default 값인 띄어쓰기 말고
# 다른 것으로 설정해 줄 수 있다.
print(a,b,c, sep = '')

# w 쓰기 r 읽기 a 뒤에 덧붙이는 add 모드
# 맨뒤에서는 encoding 을 이렇게 찾아도 상관이 없음 이전거에서 이렇게 하면
# 안됨
f = open("새파일.txt", 'w', encoding = "UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

def a(man, write, encoding):
    return man, write, encoding

#print(a('string', 'w', encoding = "UTF-8"))
#print(a('string', write = 'w', "UTF-8")) 이렇게하면 에러남

f = open("새파일.txt", 'r', encoding= "UTF-8")
line = f.readline()
line2 = f.readline()
print(line,line2, end = "", sep = "")
f.close()

#모든 줄을 읽어오려고 할 때 쓰는 코드
f = open("새파일.txt", 'r', encoding= "UTF-8")
while True:
    r = f.readline()
    if not r: break
    print(r, end = "", sep = "")

f.close()

# 줄을 리스트 형식으로 readlines 함수는 리턴한다. 그래서 for 문으로 일일이
# 출력해주는 방법도 있다.
f = open("새파일.txt", 'r', encoding= "UTF-8")
r  = f.readlines()
for line in r:
    #strip 함수는 없애주는 함수이다.
    print(line.strip('\n'))
    
f.close()

# 이렇게 하면 read 로 한번에 다 읽어올 수 있다.
f = open("새파일.txt", 'r', encoding= "UTF-8")
r  = f.read()
print(r)    
f.close()

f = open("새파일.txt", 'a', encoding= "UTF-8")
f.write("앙앙앙 난 니가 정말좋아 도라에몽")
f.close()

with open("새파일.txt", "w") as f:
    f.write("Life is too short, you need to learn about python")