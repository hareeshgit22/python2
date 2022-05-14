import time
myfile=open('myfile.txt')
while True:
 a=myfile.read()
 print(a)
 myfile.seek(0)
 b=myfile.readlines()
 print(b)
 time.sleep(2)
 myfile.seek(0)
 with open('myfile.txt') as new_file:
  contents=new_file.read()
 print(contents)
 myfile.close()
