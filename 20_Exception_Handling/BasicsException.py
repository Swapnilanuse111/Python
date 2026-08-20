'''a=int(input("Enter The First Number"))
b=int(input("Enter The Secoend Number"))
print(a/b)
print(a+b)
print(a*b)'''

#When I Execute The Program That Time I am Geting One Runtime Error which is ZeroDivisionError Noting But Exception
'''What Is An Error?
---->An Error Is An Problem Commmig In Program ,In Programing We Usally Get Syntax Error And We Can Fix Them Easily
What Is An Exception?
----->Exception Is An Error Which Are Only Recive in after executing the program

What Is Exception Handling?
----->Exeption Handling Is The Process Of Handling The Runtime Error To Avoid The Crashing The Programs
'''
try:
    a=int(input("Enter The Number"))
    b=int(input("Enter The Number"))
    print(a/b)
except:
    print("The Exception Is Handled")
print(a+b)
print(a*b)