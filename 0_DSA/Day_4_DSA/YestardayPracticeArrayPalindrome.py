arr=[1,2,1,2,1]
left=0
right=len(arr)-1
is_palindrome=True
while left<right:
    if arr[left]!=arr[right]:
        is_palindrome=False
    left=left+1
    right=right-1
if is_palindrome==True:
    print("This Array Is Palindrome")
else:
    print("This Array Is Not Palindrome")