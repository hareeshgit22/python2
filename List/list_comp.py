# List comprehension.

#Syntax: [expr for item in iteratable if condition== True]

s = ["abc","def","axz","pqr","azy"]
s1 = []
for val in s:
	if 'a' in val:
		s1.append(val)

print(s1)

s1 = [value for value in s if 'a' in value]
print(s1)

l1 = [val for val in range(11) if val%2==0]
print(l1)
ass EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for stream in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddS

s2 = [value.upper() for value in s if 'a' in value]
print(s2)

l1 = [val for val in range(11)]
print(l1)

l2 = [val if val%2==0 else "ODD" for val in l1]
print(l2)

sqr1 = [value**2 for value in l1]
print(sqr1)











