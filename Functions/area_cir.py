#Find the area of circle by scanning the radius value from user.

#method 1: using user defined function
def area(r):
	return 3.14*r**2

radius = int(input("Enter the radius: "))
ret=area(radius)
print(f"Area of the circle with radius {radius} is {ret}: ") 

#method 2: using lambda function
ret=lambda r:3.14*r**2
radius = int(input("Enter the radius: "))
print(f"Area of the circle with radius {radius} is {ret(radius)}: ") 









