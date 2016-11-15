import fileinput
import string

from distutils.core import setup
import os

file = os.listdir('.')

for i in file:
	try:
		if i.split('.')[1] == 'txt':
			for line in fileinput.input(i,inplace=True):
				if fileinput.lineno()-1:
					line = line.strip()
					nums = line.split()
					for num in nums:
						try:
							tmp = string.atof(num)
						except:
							try:
								tmp = string.atof(num[:-1])
							except:
								pass
							else:
								print '%-15f' %tmp,
						else:
							print '%-15f' %tmp,
					print ' '
				else:
					pass
				if fileinput.lineno()==1:
					line = line.strip()
					strs = line.split()
					for str in strs:
						print '%-15s' %str,
					print ' '
				else:
					pass
			fileinput.close() 
			f1 = open(i,'r+')
			lines = f1.readlines()
			f1.close()
			f2 = open(i,'w')
			f2.write(lines[0])
			for i in range(0,len(lines)-1):
				f2.write(lines[len(lines)-i-1])
			f2.close()			
	except:
		pass


	
