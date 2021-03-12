money = "string"
#not 을 사용하면 반전을 시킴 not True 면 False 이면 실행하셈
#not False 이면 True 이면 실행하셈 이다.
if not money :
    print("택시를 타고 가라")
    print("aa")
else :
    print("걸어 가라")
#밑과 같이 쓸 경우 expected an indented block(들여쓴 불록이 필요하다) 
# 라는 에러가 나온다.
#print("걸어 가라")

if True | False :
    print("출력!")
# | 는 or 와 같다!, || 는 안된다.
# & 는 and 와 같다, 마찬가지로 && 는 안된다.

# 1 이 있으면(in) True
if 1 in [1,2,3]:
    print("1이 있다!")

# 4가 없으면(not in) True
if 4 not in [1,2,3]:
    print("4가 없다")

if 1 in [1,2,3]:
    print("1이 리스트에 있어서 패스 ㅎㅎ")
    pass
elif 2 in [1,2,3]:
    print("앙!")

score = 70
if score >= 60 :
    message = "success"
else:
    message = 'fail'
print(message)

#조건부 표현식 중간 게 맞으면 success 아니면 failure 넣어줌
# else 가 없으면 에러가 난다!
message = "success" if score >= 60 else 'failure'
print(message)


