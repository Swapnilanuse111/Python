l=[10,23,212,213,323,43,50]
largest=float('-inf')
secoend_largest=float('-inf')

for i in l:
    if i>largest:
        secoend_largest=largest
        largest=i
    elif secoend_largest<i and largest!=i:
        secoend_largest=i
print(secoend_largest)