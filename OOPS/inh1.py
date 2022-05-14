class Students:
	def __init__(self,n,a):
		print("Base class constructor")
		self.name = n
		self.age = a
class Sport(Students):
	def __init__(self):
		Students.__init__(self,"vector",12)
		print("Derived class constructor")

obj1 = Sport()
print(obj1.name)
print(obj1.age)



