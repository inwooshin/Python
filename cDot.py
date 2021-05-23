import numpy as np
import matplotlib.pyplot as plt
 
#선을 그릴 수 있는 변수를 할당시켜준다.
fig, ax = plt.subplots(figsize=(15, 8))

#grid 마다 격자를 넣는다. x축의 라벨, y축의 라벨의 이름을 정하고 제목을 정한다.
#x축과 y축의 구간을 (0,2) 로 설정한다.
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interactive Plot')
 
ax.set(xlim=[0, 2], ylim=[0, 2])
ax.set_aspect('auto', adjustable='box')
 
xdata = []
ydata = []
line, = ax.plot(xdata, ydata)
 
#12_test.txt 파일에서 line의 값을 읽을 수 있도록 부르고, 각 좌표의 값을 
#xdata, ydata 에 저장해서 선을 그린다.
f = open("12_test.txt", "r")

all = f.readlines()

for i in all:
    tmp = i.split()
    xdata.append(float(tmp[0]))
    ydata.append(float(tmp[1]))

line.set_data(xdata, ydata)

f.close()

#in_and_out.txt 에서 점을 찍는 좌표와 1인지 0 값인지를 우선 읽어온다.
f = open("in_and_out.txt", "r")

all = f.readlines()

#각 좌표에 해당하는 값이 1인지 0인지를 읽어와서 그래프에 점을 띄운다.
#1이면 cyan 0이면 blue 로 띄운다.
for i in all:
    tmp = i.split()
    if tmp[2] == '1':
        plt.plot(float(tmp[0]), float(tmp[1]), "co", markersize = 6, visible = True)
    else : 
        plt.plot(float(tmp[0]), float(tmp[1]), "bo", markersize = 6, visible = True)

f.close()

#다시 in_and_out.txt 를 열어서 좌표와 1인지 0인지를 뒤에서부터 써준다.
f = open("in_and_out.txt", "a")

def add_point(event):
    if event.inaxes != ax:
        return
 
    # button 1: 마우스 좌클릭 시 좌표와 1을 써주고, 그 좌표에 cyan 점을 찍는다.
    if event.button == 1:
        x = event.xdata
        y = event.ydata
 
        plt.plot(x, y, "co", markersize = 6, visible = True)
        plt.draw()

        print(x, y)

        a = str(round(x, 6)) + ' ' + str(round(y, 6)) + ' 1' + '\n'
        f.write(a)
            
    # button 3: 마우스 우클릭 시 좌표와 0을 써주고, 그 좌표에 blue 점을 찍는다.
    if event.button == 3:
        x = event.xdata
        y = event.ydata
 
        plt.plot(x, y, "bo", markersize = 6, visible = True)
        plt.draw()

        print(x, y)

        a = str(round(x, 6)) + ' ' + str(round(y, 6)) + ' 0' + '\n'
        f.write(a)
 
    # 마우스 중간버튼 클릭 시 파일을 닫아준다.
    if event.button == 2:
        f.close()

#마우스 이벤트 함수를 할당한다.
cid = plt.connect('button_press_event', add_point)

#그래프를 띄운다.
plt.show()