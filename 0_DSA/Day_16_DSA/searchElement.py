arr=[10,203,40,50,50,60]
t=int(input("Enter The Target"))
for i in arr:
    if t==i:
        print("Found")
        break
else:
    print("NotFound")

 