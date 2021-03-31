

w1, w2, thres = (8.0, 8.0, 8.0)
n = 0.01
t = [[0,1,1,1], [0,0,0,1]]
xx = [[0,0], [0,1], [1,0], [1,1]]
or_and = 0
wcount = 2


def perceptron(t):
    global w1, w2, thres, wcount, n
    check = 0
    error = 0
    for i in range(0,4):
        y = w1 * xx[i][0] + w2 * xx[i][1]

        w1 = w1 + (n * (t[i] - y) * xx[i][0])
        w2 = w2 + (n * (t[i] - y) * xx[i][1])
        error += 0.5 * (t[i] - y) * (t[i] - y)
    
    print("w1 = %lf, w2 = %lf, err = %lf"%(w1, w2, error))
    wcount += 1
    return check

check = 0
count = 0
while check != 4:
    check = 0
    check = perceptron(t[or_and])
    count += 1
    if count >= 300:
        print("> 1000")
        break

print('%.3f * x1 + %.3f * x2 = %.3f'%(w1,w2,thres))