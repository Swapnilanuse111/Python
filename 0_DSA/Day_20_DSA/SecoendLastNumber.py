a=[10,20,30,25,22,60]
largest=float('-inf')
s_largest=float('-inf')
for i in a:
    if i>largest:
        s_largest=largest
        largest=i
    elif i!=largest and i>s_largest:
        s_largest=i
print(s_largest)
         