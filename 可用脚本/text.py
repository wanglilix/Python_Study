import fileinput

for line in fileinput.input('TXT.txt',inplace=True):
    if fileinput.lineno():
        line = line.rstrip()
        
        num = fileinput.lineno()
        print '%-20s # %2i' %(line,num)

fileinput.close()
    
