#Try-except Program 1



try:
	x = int(input("enter the first number:"))
	y = int(input("enter the second number:"	))
	ret = x/y
	print("result = ",ret)
except ZeroDivisionError:
	print("Divide by zero exception happened")

