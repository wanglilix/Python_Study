#! /usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import string

from distutils.core import setup
import os

file = os.listdir('.')


Y=[]

def datahandal(file):
	for line in fileinput.input(file,inplace=True):
		i = 0
		line = line.strip()
		strs = line.split()
		for str in strs:
			i += 1
		if i == 3:
			for str in strs:
				print '%-15s' %str,
			print ' '
	fileinput.close()

	
def datacalculate(file,X,outfile):
	for i in X:
		Y.append(0)
	for line in fileinput.input(file):
		if fileinput.lineno()-1:
			line = line.strip()
			nums = line.split()
			try:
				tmp = string.atof(nums[1])
				for i in range(1,len(X)):
					if X[i+1] > tmp:
						Y[i+1] +=  string.atof(nums[2])
						break
			except:
				pass
	outfile.write((u'直径   	      频率\n').encode('gb2312'))
	for i in range(0,len(X)):
		outfile.write('%-10s 	'%X[i])
		outfile.write('%s\n' %Y[i])
	outfile.close()
	fileinput.close()
	
	
for i in file:
	try:
		if i.split('.')[0] != 'VolumeFrequency' and i.split('.')[0] != 'VolumeFrequency2' and i.split('.')[1] == 'txt':
			datahandal(i)
			X=[0,
				0.072,
				0.144,
				0.287,
				0.575,
				1.149,
				2.299,
				4.598,
				9.195,
				18.39,
				36.78,
				73.56,
				147.12,
				294.24,
				100000000,
				]
			outfile = open('VolumeFrequency.txt','w')
			datacalculate(i,X,outfile)
			X2=[0,
				  20,
				  40,
				  60,
				  80,
				  100,
				  120,
				  140,
				  160,
				  180,
				  200,
				  220,
				  240,
				  260,
				  280,
				  300,
				  320,
				  340,
				  360,
				 380,
				 400,
				  100000000,
				  ]
			outfile2 = open('VolumeFrequency2.txt','w')
			datacalculate(i,X2,outfile2)
	except:
		pass



		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
