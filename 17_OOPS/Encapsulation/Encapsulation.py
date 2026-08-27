'''What Is Encapsulation?
----->Encapsulation is the process Of Binding The Data And Method Together Inside The Class
----->Encapsulation Is The Process of binding the data and method together insite the class 
=====>Encapsulation is used to provide the security to class members or method with the help of acess specifiers
----=>Asses Specifier are the compoent wich tells the object about the status of method
'''
class Bank:
    #Public Aceces Specifire
    b_address="Hadapsar"    #Public Data Member
    #prootected Acess Specefier
    _b_location="XYz"   #Protected Class Member
    #Private Acess Specifire
    __accounts=10       #Private Class Member 
b=Bank()
print(b.b_address)
print(b._b_location)
print(b.__accounts)