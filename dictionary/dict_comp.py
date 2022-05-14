#dictionary comprehension.

d1 = dict()
print(type(d1))

for num in range(11):
	d1[num] = num**2


print(d1)

d2 = {num:num**2 for num in range(11)}
print(d2)


d3 = {"name1":11,"name2":22,"name3":33}
print(d3)


odd1 = {k:v for (k,v) in d3.items() if v%2!=0 if v%3!=0}
print(odd1)


