#Factorial of a number
#Method 1
'''while True:

	num = int(input("Enter the value : "))
	fact = 1
	if num < 0:
		print("Factorial doesn't exist for neg vaues")
	elif num == 0:
		print(f"Factorial of {num} is {fact}")
	else: 
		for i in range(1,num+1):
			fact = fact * i
		print(f"Factorial of {num} is {fact}")
'''	

#Method2
def fact1(num):
	if num == 1:
		return 1
	else:
		return num*fact1(num-1)


while True:
	num = int(input("Enter the value : "))
	if num < 0:
		print("Factorial doesn't exist for neg vaues")
	elif num == 0:
		print(f"Factorial of {num} is {fact}")
	else: 
		print(f"Factorial of {num} is {fact1(num)}")
			

