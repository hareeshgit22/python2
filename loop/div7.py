#WAP to find numbers divisible by 7 and not divisible by 5 in a scanned range.
x = int(input("Enter the lower range: "))
y = int(input("Enter the upper range: "))
for num in range(x,y+1):
 if num%7==0:
  if num%5!=0:
   print(num,end=" ")
  else:
   pass
 else:
  pass
print("")








