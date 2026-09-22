arr=[10,20,300,44,22,80,79]
largest=float('-inf')
secoend_largest=float('-inf')

for num in arr:
    if num>largest:
        secoend_largest=largest
        largest=num
    elif secoend_largest<num and secoend_largest!=max:
        secoend_largest=num
print(secoend_largest)
