import time
from functools import reduce
#装饰器，无具体参数
#factorial = performance(factorial)

def performance(f):
	def fn(*args, **kw):
		t1 = time.time()
		t2 = time.time()
		
		print("call %s() in %fs" %(f.__name__,(t2 - t1)))
		print (f(*args, **kw))
		return f
	return fn
	
def performance_params(path):
	def performance_no_params(f):
		
		#这个会作用在返回的新函数
		#1.复制了原函数的信息到factorial
		#2.__doc___ => f.__doc__
		#3.__name__ => f.__name___
		@functools.wraps(f)
		def fn(*args, **kw):
			
			print("call %s() in %s" %(f.__name__,path))
			print (f(*args, **kw))
			return f
		return fn
	return performance_no_params
	

@performance_params('/abc/kobe01')
#f = performance_params('/abc/kobe01')(factorial)

def factorial(n):
	return reduce(lambda x,y: x*y, range(1, n+1))
	

factorial(10)



#----------------带参数的-------------#




