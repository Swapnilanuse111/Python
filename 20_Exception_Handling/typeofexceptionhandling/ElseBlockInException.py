'''Else Is an Statment Block Which Is Executed when there is No Exception In Try And Except Block In That Type It Will Excecute The Else Block'''
try:
    a=int(input("Enter The First Number:-"))
    b=int(input("Enter The Secoend Number"))
    print(a/b)
except:
    print("Error Handle")
else:
    print("There Is Know Exception In That Program")