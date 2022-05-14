#try-except program 3

try:
	z = 10
	print(z)

#	s = "vector"+ 10
	l = [1,2,3,4]
	k = l[100]

except NameError as Err:
	print(Err)
except TypeError as Err:
	print(Err)
except IndexError as Err:
	print(Err)
else:
	print("No exceptions")










