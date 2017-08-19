class TalentClient():
	
	#让对象支持上下文管理
	def __init__(self, ip):
		self.ip = ip
		
	def __enter__(self):
		print("进入");
		pass
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		print("离开");
		
	

with TalentClient("1.2") as client:
	pass
	