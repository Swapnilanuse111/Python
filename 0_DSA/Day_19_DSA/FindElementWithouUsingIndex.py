arr=[10,20,30,40,45]
target=45
for i in range(len(arr)):
    if arr[i]==target:
        print("The Element Is Found At Index",i)
        break
else:
    print("The Elemet Is Not Present In That Array")


