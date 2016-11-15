#! /usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import string
from PIL import Image
import os

parent_path = os.path.dirname(os.getcwd())
file = os.listdir(parent_path)

def getoldlength():
	path = parent_path+'\\Debug\\model.info_'
	for line in fileinput.input(path,inplace=False):
		if fileinput.lineno() == 7:
			line = line.strip()
			nums = line.split()
			return nums[0]
	fileinput.close()
	
def setnewlength(newlength):
	path = parent_path+'\\Debug\\model.info_'
	file = open(path,'r+')
	old = file.readlines()
	file.close()
	old[6]=str(newlength)+' '+str(newlength)+' '+str(newlength)+' '+str(1)+'\n'
	file2 = open(path,'w+')
	file2.writelines(old)
	file2.close()

for i in file:
	try:
		if  i.split(' ')[0] == '2':
			im = Image.open(parent_path+'\\'+i)
			imgsize = max(im.size)
			oldlength = getoldlength()
			newlength = imgsize*float(oldlength)/512
			setnewlength(newlength)
	except:
		pass