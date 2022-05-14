'''x=lambda a: a+100
print(type(x))
print(x(10))


add=lambda a,b:a+b
print(type(add))
print(add(10,20))
'''
#Explore lambda functions
def fun1(num):
	return lambda x: num

ret = fun1(10)
print(ret(5))
print(type(ret))
print(ret(10.5))








