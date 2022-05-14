#Simple parent child program
import os
if os.fork() == 0:
	print("In child ")
	print(f"pid = {os.getpid()},ppid = {os.getppid()}")
else:
	print("In  parent")
	print(f"pid = {os.getpid()},ppid = {os.getppid()}")
	
