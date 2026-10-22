arr = [10, 203, 40, 50, 60]
target = 40
for i in range(len(arr)):
    if arr[i] == target:
        print("Index =", i)
        break
else:
    print("Not Found")