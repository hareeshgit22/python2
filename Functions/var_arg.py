#Variable args list method for functions
# * is packing the variable arguments into a tuple
def add(*arg):
	print(type(arg)) #arg is a Tuple
	sum1=0
	for num in arg:
		sum1+=num
	return sum1

print(add(10,20))
print(add(10,20,30,40,50))
print(add(30,50,60))
print(add(100))














