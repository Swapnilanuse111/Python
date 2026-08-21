class Custom_Error(Exception):
    pass
age=2
if age>18:
    print("The User is Eligible For Voting")
else:
    raise Custom_Error