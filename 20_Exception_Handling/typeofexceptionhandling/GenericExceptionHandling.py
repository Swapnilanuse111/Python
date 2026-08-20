'''Generic Exception Handling?
----->Generic exception handling is a type of exception handling in which we handle multiple types of exceptions using Python's built-in Exception class with the except Exception statement.'''
try:
    a=int(input("Enter The Number"))
    b=int(input("Enter The Number"))
    print(a/b)
except Exception as e:
   print("Exception Is handled By Using The Exception Class:-",e)