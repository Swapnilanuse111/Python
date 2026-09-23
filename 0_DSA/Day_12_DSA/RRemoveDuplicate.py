arr=[10,10,20,20,20,30,30,40]
slow=0
for fast in range(1,len(arr)):
    if arr[slow]!=fast:
        slow=slow+1

        arr[slow]=arr[fast]
print(arr[:slow+1])