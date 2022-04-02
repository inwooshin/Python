import time

startTime = time.time()

n = []

for i in range(int(1e7)):
    n.append(i)

endTime = time.time()

print('time : ', endTime - startTime)