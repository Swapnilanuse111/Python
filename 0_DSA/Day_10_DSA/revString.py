s="swapnil"
rev=list(s)
left=0
right=len(rev)-1
while left<right:
    rev[left],rev[right]=rev[right],rev[left]
    left=left+1
    right=right-1
s="".join(rev)
print(s)