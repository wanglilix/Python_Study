from heapq import *
from random import *
data = range(10)
shuffle(data)
heapify(data)
while data:
	print '%i' %heappop(data)
raw_input('press enter')
