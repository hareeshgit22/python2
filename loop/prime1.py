#WAP to check whether a number is prime or not.
while True:
 x = int(input("Enter the number: "))
 for num in range(2,x+1):
  if x%num==0:
   break

 if num==x:
  print("The given number is prime")
 else:
  print("The given number is not prime")
