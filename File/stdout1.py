# stdout connection to file

import sys
sys.stdout = open("data1","w")
print("Hello world")
print("hai how are you")

sys.stdin = open("data1","r")
x = input()
y = input()
print(x,y)

sys.stdin.close()




