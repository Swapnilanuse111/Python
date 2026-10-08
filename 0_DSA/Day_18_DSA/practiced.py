a=[1,3,2,3,3,2,4,5,1]
seen=set()
duplicate=set()
for i in a:
    if i in seen:
        duplicate.add(i)
    else:
        seen.add(i)
print(seen)