#For is used when we know the number of iteration or range of iteration.
#method-1

'''list = [1,2,3,4,5]
for num in list:
 print("inside the for loop...",num)
print("outside the loop")

#method-2
for num in [1,2,3,4,5]:
 print("Inside the loop",num)
print("outside the loop...")
print(type(num))

#program - 3
l=[1,2,3,4,5]
for num in l:
 print(num)
 if num==3:
    break
print("comming out from loop")'''

l=[1,2,3,4,5]
for num in l:
 print(num)
else:
 print("list ended...")

print("outside the for loop...")



