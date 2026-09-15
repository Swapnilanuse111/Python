arr=[10,20,300,40,71,98]
largest=float('-inf')
second_largest=float('inf')

for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print("Secoend Largest Number Is")
print(second_largest)
