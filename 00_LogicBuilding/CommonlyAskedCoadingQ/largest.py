a=[10,20,70,30,40,50]
left=0
right=len(a)-1
while left<right:
    max=a[left]
    if a[left]<a[right]:
        max=a[right]
    left=left+1
    right=right-1
print(max)
