arr = [10,10,20,20,20,30,30,40]
slow = 0
for fast in range(1, len(arr)):
    if arr[slow] != arr[fast]:
        slow += 1
        arr[slow] = arr[fast]
print(arr[:slow + 1])
print("Unique count:", slow + 1)