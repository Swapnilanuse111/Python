s="mom"
left=0
right=len(s)-1
Palindrome=True
while left<right:
    if s[left]!=s[right]:
        Palindrome=False
    left=left+1
    right=right-1
if Palindrome==True:
    print("String Is Palindrome")
else:
    print("Sring Is Not Palindrome")