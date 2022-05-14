s ="vector"
print(s.upper())
s=s.upper()
print(s)

print(s.lower())
s=s.lower()
print(s)

print(s.index("c"))

s1="embedded"
print(s1.index('e'))
print(s1.index('d'))

print(s1.index('e',1))
print(s1.index('e',4))
print(s1.index('e',1,4))
print(s1.index('ed',3,7))
print(s1.index('ed',4))

print(s.capitalize())
print(s1.count('m'))

print(s.isalnum())
print(s.isalpha())

s2 = "vector_india"
print(s2.isalnum())
print(s2.isalpha())

num = "1234"
print(num.isdecimal())
print(num.isdigit())

print(s.isdigit())

s3="India"
print(s3.islower())
print(s3.isupper())

print(num.isnumeric())
print(s.isnumeric())

s4 = "vector india"
print(s4.strip())


s5="vector india pvt ltd bangalore chennai hyd"
print(s5.split())

print(s5.split('i'))
print(s5.split('i',2))
print(s5.split(' ',2))


p="india"
p1="# "
print(p1.join(p))
print(num.join(s))

print(s.center(10))
print(s.center(10,'$'))

print(s1.replace("e","#"))
print(s1.replace("e","#",1))
print(s1.replace("e","#",2))


p2="VECTOR iNDIa"
print(p2.swapcase())
print(p.zfill(10))
