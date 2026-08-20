'''Default Exception Handling Is Last Option we choes TO Handle The Exception'''
try:
    a=int(input("Enter The First Number"))
    b=int(input("Enter The Secend Number"))
    print(a/b)
except:
    print("Exception Is Handled By Using The Default Exception Block")