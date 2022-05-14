#keyword arg type function

def display(name,age,marks):
	print(f"Name-{name}, Age-{age},Marks-{marks}")

#number of args and keywords matches in order
display(name = "Hareesh", age=23, marks =12.56)
#number of args matches ,keyword in different order
display(age=23,name="Hareesh",marks=12.56)


