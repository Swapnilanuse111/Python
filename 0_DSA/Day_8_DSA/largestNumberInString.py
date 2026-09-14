l=[20,300,400,22,43,97]
# left=0
# right=len(l)-1
# max=l[0]
# while left<right:
#     if max<l[left]:
#         max=l[left]
#     if max<l[right]:
#         max=l[right]
#     left=left+1
#     right=right-1
# print(max)

max=l[0]
for i in l:
    if max<i:
        max=i
print(max)