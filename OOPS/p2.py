#OPERATOR OVERLOADING.

a=5
b=6
print(a+b)
print(int.__add__(a,b))


class Student:
 def __init__(self,m1,m2):
  self.m1=m1
  self.m2=m2
 
 def __add__(self,other)
  m1=self.m1+other.m1
  m2=self.m2+other.m2
  s3=student(m1+m2)
  return s3

 
