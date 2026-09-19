l=[10,200,3000,40,503,400]
max=l[0]
left=0
right=len(l)-1
while left<right:
    if max<l[left]:
        max=l[left]
    if max<l[right]:
        max=l[right]
    left=left+1
    right=right-1
print("The Largest Number In This List Is=",max)