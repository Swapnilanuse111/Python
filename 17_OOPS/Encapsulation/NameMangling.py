'''What Is NameMangling?
---->Name Mangling Is a way of changing the class and object to create a Unique Syntax in order to asess and modify the private mebmers
'''
#This Is 1st way of acessing the private The Private Member In Encapsulation
class Bank:
    __a=10
b=Bank()
print(Bank._Bank__a) #This Is A Way Of Aseesing The Private Members W.r.t class
Bank._Bank__a=120
print("After Updating The Private Members",Bank._Bank__a)

