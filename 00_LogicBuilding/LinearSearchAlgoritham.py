#this is the program to find the target value is present in the list or not
l=eval(input("Enter the List"))
target=int(input("Enter the target value"))
for i in l:
    if i==target:
        print("the target-",target,"Present in the list-",l)
        print("target is present in index of",l.index(target))
        break           #if the target valus is presnt in the list then it will break the loop and come out of the exicution
else:
    print("Target Is not present in the list")