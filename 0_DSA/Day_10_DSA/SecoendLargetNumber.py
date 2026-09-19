l=[10,20,30,40,500,60,59]
max=float('-inf')
secoend_max=float('-inf')
for i in l:
    if max<i:
        secoend_max=max
        max=i
    elif secoend_max<i and max!=i:
        secoend_max=i
print(secoend_max)
