#Use case of while-else.
x=0
#x = int(input("Enter the value of x: "))
while x<5:
 print("Inside while block...")
 print(x)
 x+=1
 if x == 3:
  break
else:
 print("Inside else of while")
 print("x= ",x)
 #pass
print("outside while loop..")
