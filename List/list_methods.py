l=[10,203,30,40,"vector","India"]
print(l)
l[5]=100
print(l)

l.insert(3,99)
print(l)

l.insert(100,'GOOD') #If we give out of range it adds at last.
print(l)

l1=[10,50,90,20,40,2]
print(l1)
l1.sort()
print(l1)

del l1[3]
print(l1)
del l1
#print(l1)

l.append(100)
print(l)
l.append([1,2,3])
l.append((1,2,3))
print(l)

l.extend((1,2,3))
l.extend(["a",10.5,20])
print(l)

print(l.count(100))
print(l.index('a'))

pop=l.pop()
print(pop)

print(l)
print(l.pop(5))

#SHALLOW COPY.
l=[1,2,3,4,5,6]
l1=l #shallow copy: two objects  which is pointing to a same memory location.
print(id(l1))
print(id(l))

print(l)
print(l1)
l.pop()
print(l)
print(l1)


#DEEP COPY.
l2=l[:]
print(id(l))
print(id(l2))
print(l)
print(l2)
l.pop()
print(l)
print(l2)

l3=l.copy()
print(id(l3))
print(id(l))

print(l)
l.remove(3)
print(l)
l.remove(0)
print()







