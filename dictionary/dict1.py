d = {1:"a",2:"b",3:"c",4:"d"}
try:
	print(d)
	print(d[1])
	print(d[4])
	print(d[100])
	print(d.get(100))
	print(d.get(100,"NA"))
	print(d.get(1,"NA"))
	
	print(d.items())
	print(d.keys())
	print(d.values()) 

	print(d.pop(1))
	print(d.popitem())
	print(d)
	d.update({1:'A',4:"Z"})
	print(d)
	d.clear()
	print(d)

except KeyError as Err:
	print(Err)
else:
	print("no exceptions")






