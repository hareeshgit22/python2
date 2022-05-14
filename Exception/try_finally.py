# Finally block

try:
	x = int(input("Enter x: "))
	y = int(input("Enter y: "))
	ret = x/y
except ZeroDivisionError as Err:
	print(Err)
else:
	print("No exceptions....")
	print(f"Result = {ret}")
finally:
	print("Inside finally block...")







