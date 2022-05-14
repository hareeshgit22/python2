#Sum of all elements in all list.
#method 1
def sum_list(l):
	t=0
	for i in l:
		t+=i
	return t

list1=[1,2,3,4,5,6]
print(f"sum of the list is: {sum_list(list1)}")

#method 2
ret= lambda list1: sum(list1)

list1=[1,2,3,4,5,6]
print(f"sum of list is: {ret(list1)}")








