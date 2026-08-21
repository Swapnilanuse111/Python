'''Finally Block Is An Keyword Which Is Used to create a statment Block in Exception Handling
---->It Will Execute Always If There is An Exeption Ocuur And If There Is Not Exception Occor It will Always Excecute the finllay block

'''
try:
    a=int(input('Enter The Number'))
    b=int(input('Enter The Number'))
    print(a/b)
except:
    print("Error Is Handled")
else:
    print('There Is An No Error Or Exception')
finally:
    print("The Finally Block Is Excecuted")
