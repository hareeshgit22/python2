#WAP to print fibonacci series upto a scanned value
r = int(input("Enter the range: "))
x = 0
y = 1
print(x,end=" ")
print(y,end=" ")
while r>(x+y):
 z=x+y
 print(z,end=" ")
 x=y
 y=z
print()






