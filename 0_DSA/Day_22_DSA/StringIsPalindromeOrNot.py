s="madam"
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("Given String Is Not Palindrome")
        break
    left=left+1
    right=right-1
else:
    print("Given String Is Palindrome")