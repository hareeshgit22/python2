'''
s = "vector"
print(s)
print(s[0])
print(s[5])
#print(s[7]) #index Error
#s[0]='z' #type error bcoz string is immutable and doesnot support assignment.
s="India"
print(s)
size=len(s)

print(size)

print(s[len(s)-1])

# 0  1   2   3   4
# I  n   d   i   a
#-5 -4  -3  -2  -1

print(s[-5])
print(s[-3])
print(s[-2])

'''
#slicing operator [:],It will devide/slice the data.string will not get modified.slicing can be done on strings,List,tuple.

s="vector"
print(s)
s1=s[2:5]
print(s1)
print(s[0:5])
print(s[:9])
print(s[:3])
print(s[3:])
print(s[:])
print(s[4:1])

'''negative slicing.'''

# 0  1  2  3  4  5
# v  e  c  t  o  r
#-6 -5 -4 -3 -2 -1

s='vector'
print(s[-3:-1])
print(s[-6:-4])

#[start:stop:step]
print(s[1:4:1])
print(s[0:len(s)-1:2])
print(s[::2])
print(s[::10])


print(s[4:1:-1])
print(s[len(s)-1:0:-1])
print(s[::-1])




  
