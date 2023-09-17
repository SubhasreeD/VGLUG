class fileop():
	def __init__(self,filename):
		self.filename=filename
	def readfunc(self):
		with open(self.filename,'r') as file:
			print(file.read())
	def writefunc(self):
		with open(self.filename,'w') as file:
			print(file.write(input()))
	def appendfunc(self):
		with open(self.filename,'a') as file:
			file.write(input())
		with open(self.filename,'r') as file:
			print(file.read())
a=fileop("subha.txt")
a.writefunc()
a.readfunc()
a.appendfunc()
