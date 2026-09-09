arr = [1, 1, 2, 2, 3, 4, 4, 5]
slow=0
fast=0
if arr[slow]==arr[fast]:
    arr[slow]=arr[fast]
    fast=fast+1
elif arr[slow]!=arr[fast]:
    arr[slow]=arr[fast]
    fast=fast+1
print(arr[slow])