import numpy as np
import matplotlib.pyplot as plt
 
fig, ax = plt.subplots(figsize=(15, 8))
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interactive Plot')
 
ax.set(xlim=[0, 2], ylim=[0, 2])
ax.set_aspect('auto', adjustable='box')
 
xdata = []
ydata = []
line, = ax.plot(xdata, ydata)
 
f = open("12_test.txt", "r")

all = f.readlines()

for i in all:
    tmp = i.split()
    xdata.append(float(tmp[0]))
    ydata.append(float(tmp[1]))

line.set_data(xdata, ydata)

f.close()

f = open("in_and_out.txt", "w")

def add_point(event):
    if event.inaxes != ax:
        return
 
    # button 1: 마우스 좌클릭
    if event.button == 1:
        x = event.xdata
        y = event.ydata
 
        plt.plot(x, y, "co", markersize = 6, visible = True)
        plt.draw()

        print(x, y)

        a = str(round(x, 6)) + ' ' + str(round(y, 6)) + ' 1' + '\n'
        f.write(a)
            
    # button 3: 마우스 우클릭 시 기존 입력값 삭제
    if event.button == 3:
        x = event.xdata
        y = event.ydata
 
        plt.plot(x, y, "bo", markersize = 6, visible = True)
        plt.draw()

        print(x, y)

        a = str(round(x, 6)) + ' ' + str(round(y, 6)) + ' 0' + '\n'
        f.write(a)
 
    # 마우스 중간버튼 클릭 시 종료하기
    if event.button == 2:
        f.close()

cid = plt.connect('button_press_event', add_point)

plt.show()