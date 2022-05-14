class Python():
	def __init__(self,n,a):
		print("constructor")
		self.name = n
		self.age = a
	def __str__(self):
		return f"Name : {self.name},Age : {self.age}"
	def __add__(self,other):
		return f"Name :{self.name + other.name,self.age + other.age}"



obj1 = Python("Cobra",5)
obj2 = Python("Naga",2)
print(obj1)
print(obj2)
print(obj1 + obj2)












