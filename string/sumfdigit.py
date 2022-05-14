#Sum of digits in a string.

s = input("Enter the string: ")
l = list(s)
sum1 = 0
for num in l:
	if num.isdigit():
		sum1 += int(num)
print(f"Digits sum = {sum1}")
