arr=[1,2,1,2,1,2]
left=0
right=len(arr)-1
is_palindrome=True
while left<right:
    if arr[left]!=arr[right]:
        is_palindrome=False
        break
    left=left+1
    right=right-1
if is_palindrome==True:
    print("The Given Array Is Totaly Palindrome Array")
else:
    print("The Give array is Not Palidrome")