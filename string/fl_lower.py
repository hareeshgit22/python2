#scan a string, make first and last charecter in lower case and rest in upper case.


def fll(s):
	s1 = ""
	s1 += s[0].lower()
	for n in range(1,len(s)-1):
		s1 += s[n].upper()
	s1 += s[len(s)-1].lower()
	return s1

s = input("Enter the string : ")
print(fll(s))












