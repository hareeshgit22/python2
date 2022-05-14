import os
fd = os.pipe()
if os.fork() == 0:
	print("In child ")
	print(f"pid = {os.getpid()}, ppid = {os.getppid()}")
	ret = os.read(fd[0],1024)
	print("Data = ",ret.decode())
else:
	print("In parent ")
	print(f"pid = {os.getpid()}, ppid = {os.getppid()}")
	s = b"Vector" 
	os.write(fd[1],s)
