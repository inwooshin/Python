import sys
# 어느 argv 가 들어왔는지 출력 int main (argc, argv) 의 argv 를 출력해줌
print(sys.argv)

import pickle
f = open("test.txt", "wb")
data = {1: "python", 2 : "that you need"}
#딕셔너리 형태의 데이터를 f의 파일에 딕셔너리 형태로 넣어준다.
pickle.dump(data, f)
f.close()

f = open("test.txt", "rb")
#그렇게 해서 pickle 에서 load 하면 딕셔너리가 나온다!
data = pickle.load(f)
print(data)

import time
print(time.localtime(time.time()))

#1초 쉰다.
time.sleep(1)

import random
lotto = sorted(random.sample(range(1,46), 6))
print(lotto)

import webbrowser
webbrowser.open("www.naver.com")