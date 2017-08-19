# '__ge__', >= 
# '__gt__', >
# '__le__', <= 
# '__lt__'  <
#__eq__      == 
#__ne__     != is not

#以上可以用functool的total_ordering的类装饰器来简化
#1.定义一个eq方法 2.gt/lt的其中一个


#__add__ 加
#__sub__ 减
#__mul__ 2边都是自定义数据
#__rmul__ 左边是原始数据 + 右边自定义


#重载运算符

from functools import total_ordering


@total_ordering

class Money:
#	__slot__()
	def __init__(self, sum = 0):
		self.sum = sum
		
	#打印
	def __str__(self):
		return str(self.sum)
	
	def __add__(self, other):
		return Money(self.sum + other.sum)
		
	def __sub__(self, other):
		return Money(self.sum - other.sum)
		
		
	#total_ordering	
	def __eq__(self, other):
		return self.sum == other.sum
		
	def __gt__(self, other):
		return self.sum > other.sum
	

m1 = Money(10)
m2 = Money(5)

print(m1 < m2) #False
print(m1 + m2) #15
print(m1 - m2) #5












#..


