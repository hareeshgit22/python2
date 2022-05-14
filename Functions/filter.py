from functools import reduce
lst=[num for num in range(-50,50)]
pslst=list(filter(lambda n: n if n>0 else False,lst))
evens=list(map(lambda n: n*2,pslst))
sum=reduce(lambda a,b:a+b,evens)
print("pos nors are:",pslst)
print("even nors are:",evens)
print("total sum of even:",sum)




