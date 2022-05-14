class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age


	def sport(self):
		print(f"{self.name} is good in sports")

	def study(self):
		print(f"{self.name} is excellent in study")



my_st = Student("Sharath",14)
print("Name: ",my_st.name)
print("Age: ",my_st.age)


my_st.sport()
my_st.study()








