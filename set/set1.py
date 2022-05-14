#SET : set is a collection of unordered unique elements.

s = {1,1,1,2,3,4,4,5,5,6}
print(s)
s1=set([10,20,30,30])
print(s1)
s2 = set(["vector",10,5,'abc'])
print(s2)
print(len(s))
print(type(s))

s.add(100)
print(s)
s1.clear()
print("s1")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s2.pop())

x = {1,2,3,4,5,6,7,8,9}
y = {2,4,6,8}
print(x.union(y))
#y.add(100)
print(x.union(y))

print(x.intersection(y))
print(y.intersection(x))
print(x.issubset(y))
print(y.issubset(x))


print(y.issubset(x))
print(x.issuperset(y))

print(x.difference(y))
x.difference_update(y)
print(x)
print(x)
x.discard(9)
print(x)

