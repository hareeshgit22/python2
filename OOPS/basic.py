#class and objects.
class Computer:
 def __init__(self,cpu,ram):
  self.cpu=cpu
  self.ram=ram
 def config(self):
  print("config is ",self.cpu,self.ram)
 



comp1=Computer('i5','8gb')
comp1.config()

comp2=Computer('i3','12gb')
comp2.config()

comp3=Computer('i2','4gb')
comp3.config()



