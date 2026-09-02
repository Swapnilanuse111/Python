s="madam"
left=0
right=len(s)-1
is_palindrome=True
while left<right:
    if s[left]!=s[right]:
        is_palindrome=False
    left=left+1
    right=right-1
if is_palindrome==True:
    print("The Given String Is Palindrome")
else:
    print("The Give String Is Not Palindrome")