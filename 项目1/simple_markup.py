import sys,re,os
from util import *

files = os.listdir('.')
for file in files:
	if file.split('.')[1] == 'txt':
		print '<html><head><title>...</title><body>'
		title = True
		for block in blocks(file):
			block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block) # .：任意 +:多个  ？：可有可无  re.sub:替换
			if title:
				print '<h1>'
				print block
				print '</h1>'
				title =	False
			else:
				print '<p>'
				print block
				print '</p>'
				
		print '</body></html>'
		raw_input(' ')
	else:
		pass

