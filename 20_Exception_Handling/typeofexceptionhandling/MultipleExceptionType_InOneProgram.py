try:
    a=int(input("Enter The Number"))
    b=int(input('Enter The Number'))
    print(a/b)

#1]Specific Exception Handling'''
except ZeroDivisionError: 
    print("The The Number Cant be Divible By zero")

#2]Generic Exception Handling
except Exception as e:
    print(e)
    print("The Exception IS handled By Using the Generic Exception Handling:----",e)

#Defauilt Exception Handling
except:
    print('The Exception Is Handled By using the Default Exceptooion Hanlding')
