a=input("Enter string:")
l=len(a)-1
temp=0
for i in range(l):
    if a[i]!=a[l-i]:
        break
    temp=temp+1
if temp==l:
    print("Palindrome")
else:
    print("Not a Palindrome")
