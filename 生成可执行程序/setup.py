from distutils.core import setup
import py2exe
import os
#dir = 
file = os.listdir('.')
for i in file:
	try:
		if i.split('.')[0] != 'setup' and i.split('.')[1] == 'py':
			#print i
			setup(console=[i])
	except:
		pass
	