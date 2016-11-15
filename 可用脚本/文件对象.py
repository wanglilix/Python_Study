#coding=utf-8  #中文注释需要加这一句
f = open('TXT.txt','r+')
f.write('Hello')
f.write('World!\n')
f.writelines(['a\n','b','c\n','d\n','e\n'])
f.close()


f = open('TXT.txt')

# while True:
	# line = f.readline(20)
	# if not line: break
	# print ' '+line

for line in f:
	print ' '+ line
	
f.close()
raw_input(' ')
