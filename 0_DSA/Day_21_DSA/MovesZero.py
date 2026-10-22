a=[10,0,20,0,20,0,10,0]
slow=0
for fast in range(len(a)):
    if a[fast]!=0:
        a[slow]=a[fast]
        slow=slow+1
for i in range(slow,len(a)):
    a[i]=0
print(a)