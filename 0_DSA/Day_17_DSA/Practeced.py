a=[1,3,2,3,3,2,4,5,1]
slow=0
for fast in a:
    if a[slow]==fast:
       aa=a[fast]
       slow=slow+1
print(aa)