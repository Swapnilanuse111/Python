arr = [10, 10, 20, 20, 30]
slow=0

for fast in range(1,len(arr)):
    if arr[slow]==arr[fast]:
        pass
    elif arr[slow]!=arr[fast]:
        arr[slow]=arr[fast]
        slow=slow+1
    print(arr)