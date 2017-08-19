from os.path import join

'''文件对象的装饰类，用来保证文件被删除时能够正确关闭。'''

class FileObject:
	def __init__(self, filepath = '~', filename = 'sameple.txt'):
		self.file = open(join(filepath, filename),'r+')
		
	def __del__(self):
		self.file.close()
		del self.file 