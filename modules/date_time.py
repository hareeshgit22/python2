import datetime as dt
x = dt.datetime.now()
print(x)

print(type(x))
print(x.year)
print(x.strftime("%A"))

y = dt.datetime(2022,5,22)
print(y)
print(y.strftime("%A")) #weekday full version.
print(y.strftime("%B")) #month full version. 
print(y.strftime("%Y")) #Year full version.
print(y.strftime("%S")) #second.
print(y.strftime("%p")) #(AM/PM)
print(y.strftime("%a")) #weekday short version.
print(y.strftime("%b")) #month short version

print(y.strftime('%d')) #day of month(01-31)
print(y.strftime('%w')) #Weekday as a number(0-6)

d1 = dt.date(1997,5,22)
d2 = dt.date(2022,5,22)
diff = d2 - d1
print(diff.days)


d3 = d1.today()
print(d3)
print((d3-d1).days)

