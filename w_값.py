import pickle

name = 'nirsa'
age = 99
address = 'seoul'

with open('nirsa.txt', 'wb') as file:
	pickle.dump(name, file)
	pickle.dump(age, file)
	pickle.dump(address, file)