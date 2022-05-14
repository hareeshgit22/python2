class Python:
	def __init__(self,n,a):
		print("Constructor")
		self.__name = n  #private data members.
		self.__age = a
	def snake_data(self):
		print("Name: ",self.__name)
		print("age: ",self.__age)


obj1 = Python("Cobra",4)
obj2 = Python("naga",2)
obj1.snake_data()

obj2.snake_data()

try:
	print(obj1.__name,obj1.__age) #Not possible.
except:NameError




