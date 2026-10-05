arr=[0,1,0,3,13]
slow=0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow]=arr[fast]
        slow=slow+1
for i in range(slow,len(arr)):
    arr[i]=0
print(arr)