#Try-except Program 2 



try:
	x = int(input("enter the first number:"))
	y = int(input("enter the second number:"	))
	ret = x/y
	print(f"result = {ret}")
#	print(var1)
	#var2 = "vector" + x
except ZeroDivisionError:
	print("Divide by zero exception happened")
except NameError:
	print("Name is not defined")
except TypeError:
	print("Type missmatched")


else:
	print("No exceptions")





