#Arbitrary keyword arguments **kwargs
#if we dont know how many keyword args will be passed into our function
#arguments will be stored as a dictionary

def my_fun(**name):
	print("Name is: "+name["x"] +" " +name["y"] +" " + name["z"])
	print(name)

def empty():
	pass


my_fun(x="vector",y="India",z="Bangalore")

empty()








