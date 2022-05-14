#WAP to find odd numbers between the given range.scan the ranges.

x=int(input("Enter the lower range: "))
y=int(input("Enter the upper range: "))
for num in range(x,y+1):
 if num%2!=0:
  print(num,end=" ")
 else:
  pass
print("")


for num in range(1,y+1,2):
 print(num,end=" ")
print("")
