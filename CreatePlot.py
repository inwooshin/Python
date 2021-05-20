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
 
f = open("12_test.txt", "w")
 
def add_point(event):
    if event.inaxes != ax:
        return
 
    # button 1: 마우스 좌클릭
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
            
    # button 3: 마우스 우클릭 시 기존 입력값 삭제
    if event.button == 3:
        xdata.pop()
        ydata.pop()
        line.set_data(xdata, ydata)
        plt.draw()
 
    # 마우스 중간버튼 클릭 시 종료하기
    if event.button == 2:
        f.close()
 
cid = plt.connect('button_press_event', add_point)

plt.show()