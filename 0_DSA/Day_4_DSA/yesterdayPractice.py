arr=[1,2,4,7,8,2]
target=9
left=0
right=len(arr)-1
while left<right:
    sum=arr[left]+arr[right]
    if sum==target:
        print("Pair Is Found",arr[left],"And",arr[right])
        break
    elif sum>target:
        right=right-1
    else:
        left=left+1
        
