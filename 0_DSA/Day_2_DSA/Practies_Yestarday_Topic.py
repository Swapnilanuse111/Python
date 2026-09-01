s="adam"
left=0
right=len(s)-1
is_Palindrome=True
while left<right:
    if s[left]!=s[right]:
        is_Palindrome=False
    left=left+1
    right=right-1
if is_Palindrome==True:
    print("Palindrome")
else:
    print("Not Palindrome")