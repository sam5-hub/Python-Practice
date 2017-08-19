from time import time
from random import randint
from collections import OrderedDict

players = list("ABCDEFGHJK")
start = time()
d = OrderedDict()


for i in range(10):
	p = players.pop(randint(0, 9 - i))
	end = time()
	
	print(i+1, p, end - start) #随机排名 字母 时间间隔
	#p为key ,元组是(编号,时间)
	#排序是拿元组的第一位去排序的,时间也可以，编号也可以
	d[i+1] = (p,end - start)

#   p (i+1),end - start)
#	1 ('H', 1.1920928955078125e-05)
#	2 ('K', 8.082389831542969e-05)
#	3 ('E', 9.489059448242188e-05)
#	4 ('C', 0.0001049041748046875)
#	5 ('J', 0.00011491775512695312)
#	6 ('B', 0.0001239776611328125)
#	7 ('F', 0.00013399124145507812)
#	8 ('D', 0.00014400482177734375)
#	9 ('G', 0.00015282630920410156)
#	10 ('A', 0.0001628398895263672)
	
	
print
print('_' * 20)

for k in d:
	print(k, d[k])