#Nested for loop
for x in [0,1,2]:
 print("outer loop: ",x)
 for y in [0,1]:
  print("inner loop :...",x*y)

#patterns
'''
*
* *
* * *
* * * *'''
n=int(input("enter the number of rows"))
for row in range(1,n+1):
 for coloumn in range(row):
   print("*",end=" ")
 print()


n=int(input("Enter the number of rows: "))
for row in range(1,n+1):
 print("* "* row)



'''
* * * *
* * *
* *
*
'''
n=int(input("Enter the number of rows: "))
for row in range(0,n+1):
 print("* "*(n-row))

n=int(input("Enter the number of rows: "))
for row in range(n,0,-1):
 print("* "*row)

