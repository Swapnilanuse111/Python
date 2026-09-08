arr=[10,45,202,80,35,60]
left=0
right=len(arr)-1
max=arr[0]
while left<right:
    if arr[left]>max:
        max=arr[left]
    if arr[right]>max:
        max=arr[right]
    left=left+1
    right=right-1
print(max)
      
