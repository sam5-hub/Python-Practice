
#global
num = 1
def testGlobal():
	
#	1.当内部作用域想修改外部作用域的变量时，就要用到global
#	2.如果没有声明
#	3.错误信息为局部作用域引用错误，因为 testGlobal 函数中的 num 使用的是局部
#	local variable 'num' referenced before assignment
	 
	global num
	print(num) 
	num = 123
	print(num)
	
testGlobal()

#nonlocal
#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

def outer():
	num = 10  #（enclosing 作用域，外层非全局作用域）
	def inner():
		nonlocal num   # nonlocal关键字声明
		num = 100
		print(num) #2.执行
	
	print(num) #1.执行		
	return inner

	
i = outer()
i()


