#user defined function example

#defination of function.
def test():
	print("Inside test function")
	print("Hello world....")

#function with arguments and return value. 
def addition(x,y):
	z=x+y
	return z
#function with  multiple returns.
def mul_ret(x,y):
	z=x+y
	z1=x*y
	return z,z1




#Function calls
#test()
ret = addition(10.25,20.33)
print(ret)
ret=addition(10,20)
print(ret)
ret=addition("Vector ","India")
print(ret)

ret,ret1=mul_ret(10,2)
print(ret,ret1)










