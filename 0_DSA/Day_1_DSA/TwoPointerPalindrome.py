s="mada"
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        is_palindrome=True
        break
    left=left+1
    right=right-1
if is_palindrome:
    print("Given String Is Palindrome")
else:
    print("paliindrome")