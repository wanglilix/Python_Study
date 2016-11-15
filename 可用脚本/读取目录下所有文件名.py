import os
#dir = 
file = os.listdir('.')
for i in file:
	try:
		print i.split('.')[0] + '.' + i.split('.')[1]
	except:
		print i

raw_input(' ')