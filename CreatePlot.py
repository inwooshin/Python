import matplotlib.pyplot as plt
 
fig, ax = plt.subplots(figsize=(15, 8))

#grid 마다 격자를 넣는다. x축의 라벨, y축의 라벨의 이름을 정하고 제목을 정한다.
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interactive Plot')
 
#x축과 y축의 구간을 (0,2) 로 설정한다.
ax.set(xlim=[0, 2], ylim=[0, 2])
ax.set_aspect('auto', adjustable='box')
 
#12_test.txt 파일에 line의 값을 써줄 수 있도록 부르고, 각 좌표의 값을 
#xdata와 ydata 로 받아서 라인을 그려준다.
xdata = []
ydata = []
line, = ax.plot(xdata, ydata)
 
f = open("12_test.txt", "w")

def add_point(event):
    if event.inaxes != ax:
        return
 
    # button 1: 마우스 좌클릭 시 좌표와 1 파일에 입력
    if event.button == 1:
        x = event.xdata
        y = event.ydata

        a = str(round(x, 6)) + ' ' + str(round(y, 6)) + '\n'
        print(a)
        f.write(a)
 
        xdata.append(x)
        ydata.append(y)
 
        line.set_data(xdata, ydata)
        plt.draw()
            
    # button 3: 마우스 우클릭 시 좌표와 0 파일에 입력
    if event.button == 3:
        xdata.pop()
        ydata.pop()
        line.set_data(xdata, ydata)
        plt.draw()
 
    # 마우스 중간버튼 클릭 시 파일을 종료시킨다.
    if event.button == 2:
        f.close()
 
#마우스 이벤트 함수를 할당한다.
cid = plt.connect('button_press_event', add_point)

#그래프를 띄운다.
plt.show()