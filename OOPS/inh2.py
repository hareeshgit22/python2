class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show(self):
		print(f"{self.name} was {self.age} old\n")	
class Sport(Student):
	def __init__(self,g_name):
		self.game_name=g_name
		Student.__init__(self,"mirafra",12)
		print(f"{self.name} is very good in {self.game_name} even he was {self.age} years old")
		Student.show(self)
		print(f"{self.game_name} is very famous\n")	


obj2=Sport("cricket")







