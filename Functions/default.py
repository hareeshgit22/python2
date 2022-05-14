#Default args in function

def addition(x,y=100):
	z=x+y
	return z

print(addition(x=10,y=20)) #user data for y is taken as 20
print(addition(x=10))#Default value of y is taken as 100
print(addition(y=20))#Issue with not providing positional argumen i.e x
	








