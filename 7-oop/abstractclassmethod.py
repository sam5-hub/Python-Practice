from abc import ABCMeta, abstractclassmethod
from functools import total_ordering

@total_ordering
class Money(object):
	
	def __init__(self, sum = 0):
		self.sum = sum
	
	@abstractclassmethod
	def dollar(self):
		pass #子类需要计算都要实现这个抽象方法
		
#	S = property(getSum)
	#total_ordering	
	def __eq__(self, other):
		return self.dollar() == other.dollar()
			
	def __gt__(self, other):
		return self.dollar() > other.dollar()
		
class RMB(Money):
#	__slot__()
	
		
	def dollar(self):
		return self.sum * 0.68
	
	def __add__(self, other):
		return Money(self.sum + other.sum)
		
	def __sub__(self, other):
		return Money(self.sum - other.sum)
		
class HKD(Money):
#	__slot__()
	
		
	def dollar(self):
		return self.sum * 0.58
		
h1 = HKD(100)
r1 = RMB(100)

#比较的是doller的值
print(h1 >= r1)
	