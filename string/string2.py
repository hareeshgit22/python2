#print string character by character
# method-1
s="vector"
for ch in s:
 print(ch,end=" ")
print()

# method-2
for ch in range(0,len(s)):
 print(s[ch],end=" ")
print()

#WAP the given string is palindrome or not.
s=input("Enter the string: ")
s1=s[::-1]
if s==s1:
 print("string is palindrome")
else:
 print("string is not palindrome")



print(min(s))
print(max(s))





