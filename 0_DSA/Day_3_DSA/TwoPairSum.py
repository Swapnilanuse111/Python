arr = [1,2,4,7,11,15]
left=0
right=len(arr)-1
target=9
while left<right:
    sum=arr[left]+arr[right]
    if sum == target:
        print("Pair found:", arr[left], "and", arr[right])
        break
    elif sum < target:
        left += 1
    else:
        right -= 1