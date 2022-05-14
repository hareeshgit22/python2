class Dog:
	"""A Model class for a dog"""
	def __init__(self,n,age):
		"""Intializing name and age attributes"""
		self.name = n
		self.age = age
	

	def sit(self):
		"""Simulating dog sitting"""
		print(f"{self.name} is now sitting.")
	def bark(self):
		print(f"{self.name} is barking now")
	def roll_over(self):
		print(f"{self.name} is rolled over now")



my_dog = Dog("jonny",3)  #object creation.
print("Name:",my_dog.name) #accessing of name attribute from class.
print("Age = ",my_dog.age) #accessing of age attribute from class.
my_dog.sit() #accessing of sit() methods from class.
my_dog.bark() #accessing of bark() methods from class.
my_dog.roll_over()













