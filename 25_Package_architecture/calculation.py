# # import entire module

# # syntax:import module_name
# import addition as ad
# # import addition
# num1=int(input("Enetr The Number :"))
# num2=int(input("Enetr The Number :"))

# operation=input("Enetr Your Opeeration")

# # if operation=='+':
# #     print(f'addition of {num1} and {num2} is {addition.add(num1,num2)}')




# if operation=='+':
#     print(f'substraction of {num1} and {num2} is {ad.add(num1,num2)}')


# import specific function
# Syntx from_module_name import function name

# from addition import add,message
# num1=int(input("Enetr The Number :"))
# num2=int(input("Enetr The Number :"))

# operation=input("Enetr Your Opeeration")
# if operation=='+':
#      print(f'addition of {num1} and {num2} is {add(num1,num2)}')
# person_name=input("ENter The NAme:-")
# print(message(person_name))

#iport everything from a module
# from addition import *

# num1=int(input("Enetr The Number :"))
# num2=int(input("Enetr The Number :"))

# operation=input("Enetr Your Opeeration")
# if operation=='+':
#      print(f'addition of {num1} and {num2} is {add(num1,num2)}')
# person_name=input("ENter The NAme:-")
# print(message(person_name))



#import Multiple Modules
# import addition
# import substraction

# num1=int(input("Enetr The Number :"))
# num2=int(input("Enetr The Number :"))

# operation=input("Enetr Your Opeeration")
# if operation=='+':
#     print(f'addition of {num1} and {num2} is {addition.add(num1,num2)}')
# elif operation=='-':
#     print(f'addition of {num1} and {num2} is {substraction.sub(num1,num2)}')
# person_name=input("ENter The NAme:-")
# print(message(person_name))



''' import multiple module in one line
    Syntax-import module1,module2
'''
import addition,substraction

num1=int(input("Enetr The Number :"))
num2=int(input("Enetr The Number :"))

operation=input("Enetr Your Opeeration")
if operation=='+':
    print(f'addition of {num1} and {num2} is {addition.add(num1,num2)}')
elif operation=='-':
    print(f'addition of {num1} and {num2} is {substraction.sub(num1,num2)}')
person_name=input("ENter The NAme:-")
print(message(person_name))