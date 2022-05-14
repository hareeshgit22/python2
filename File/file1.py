# Explore basics of file concepts in python.
try:
	fp = open("myfile.txt","r")
except FileNotFoundError as Err:
	print(Err)
else:
	print(type(fp))
	print("File is present")














