#Required argument functions
#Number of actual arguments should match with the formal arguments

def display(name,age,marks):
	print(f"my name is {name}. I'm {age} years old. and I got marks in pu is {marks}.")



display("Hareesh",23,98) #valid
display("Hareesh",23) #Invalid-less args
display("Hareesh",23,96,93) #Invalid-more args.

display(23,13,"hareesh") #order changes ,operation also changes.



