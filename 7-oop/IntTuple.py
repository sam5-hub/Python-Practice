class IntTuple(tuple):
#1.new
#2.new后返回的对象传入__init__
#3.init

	def __new__(cls, iterable):
		g = (x for x in iterable if isinstance(x, int) and x > 0)
		return super(IntTuple, cls).__new__(cls, g)
	
	def __init__(self, iterable):
		pass
		

t = IntTuple((2,4,-9,22,"1"))

print(t)