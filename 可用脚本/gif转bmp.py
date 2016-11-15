#! /usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import string
import Image
import os

file = os.listdir('.')

for i in file:
	try:
		if  i.split('.')[-1] == 'dcm':
			outfile = i.split('.')[0] + ".bmp"
			im = Image.open(i)
			im = im.convert('RGB')
			im.save(outfile,"bmp")
	except:
		pass