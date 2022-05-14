with open('new_file.txt',mode='w') as f:
 f.write('\n I created new file')
 
with open('new_file.txt',mode='a') as f:
 f.write('I added second line. \n I added Thirdline.')

with open('new_file.txt',mode='r') as f:
 print(f.read())
 f.seek(0)
 print(f.read())


 
