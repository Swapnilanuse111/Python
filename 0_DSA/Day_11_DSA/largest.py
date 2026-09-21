arr=[10,20,300,40,50]
max=0
left=0
right=len(arr)-1
while left<=right:
    if max<arr[left]:
        max=arr[left]

    if max<arr[right]:
        max=arr[right]
    left=left+1
    right=right-1
print(max)