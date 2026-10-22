a=[10,10,20,30,30,30,40,40,50]
slow=0
for fast in range(1,len(a)):
    if a[fast]!=a[slow]:
        slow=slow+1
        a[slow]=a[fast]
print(a[:slow+1])
