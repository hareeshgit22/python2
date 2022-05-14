import sys
if len(sys.argv) != 2:
	print("usage : python3 program.py filename")
else:
	try:
		fp = open(sys.argv[1],"r")
	except FileNotFoundError as Err:
		print(Err)
	else:
		print("File is present")
		print(type(fp))
		print(f"File name : {fp.name}")
		print(f"Mode :{fp.mode}")
		print(f"File closed status: {fp.closed}")
		fp.close()
