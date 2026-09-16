s="abcd"
a=list(s)
left=0
right=len(a)-1
while left<right:
    a[left],a[right]=a[right],a[left]
    left=left+1
    right=right-1
s=" ".join(a)
print(s)

