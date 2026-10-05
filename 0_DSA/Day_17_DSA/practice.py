arr=[10,203,0,0,2,0,0,30]
slow=0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow]=arr[fast]
        slow=slow+1
for i in range(slow,len(arr)):
    arr[i]=0
print(arr)