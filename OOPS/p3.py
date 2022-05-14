#method overiding

class A:
 def show(self):
  print("in A show")

class B(A):
 def show(self):
  print("in B show")

s1=B()
s1.show()
 






