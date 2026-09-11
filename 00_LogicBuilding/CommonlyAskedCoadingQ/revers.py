s=input("Enter the String")
arr=list(s)
left=0
right=len(s)-1
while left<right:
    arr[left], arr[right] = arr[right], arr[left]
    left=left+1
    right=right-1
reverse = "".join(arr)
print(reverse)
# if reverse==s:
#     print("This String Is Palindrome")
# else:
#     print("This String is Not Palindrome")
