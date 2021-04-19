import numpy as np

a = [[1,2],[3,4]]
b = [[1,2], [3,4]]
c = [[2,-1], [-3,4]]
print(a)
print(b)
print(c)
print()

a = np.array(a).transpose()
b =np.array(b).transpose()
c =np.array(c).transpose()

print(a)
print(b)
print(c)