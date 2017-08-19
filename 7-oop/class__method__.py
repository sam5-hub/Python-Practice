#因为 Python 定义了__str__()和__repr__()两种方法
#__str__()用于显示给用户
#而__repr__()用于显示给开发人员。

class Person(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		

class Student(Person):
	def __init__(self, name, gender, score):
			super(Student, self).__init__(name, gender)
			self.score = score
			
	
	def __str__(self):
		return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
		
	__repr = __str__
	
	
s = Student('kobe', 'male', '81')
print(s)