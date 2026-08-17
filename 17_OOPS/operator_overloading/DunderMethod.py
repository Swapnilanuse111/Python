#Operator Overloading Done By Using The Dunder Method 

#Dunder Method Is Predefined Meethod Avaliable In Python so that an operator can be Overloaded With A Method
#Dunder Method Is Predefined Method Avalaible In Python So That An Opeator Can Be Overloaded With A Method
#Dunder Method Is Predfined Method Available IN Python So That An Operator Can Be Overloded With A MEthod
#Dunder Method Is Predifined Method Available In Python it is used to define the behavior of object
class A:
    x=10
    def __init__(self,data):
        self.data=data
    
    def __add__(self,other):
        return self.data+other.data
obj1=A(100)
obj2=A(5000)
print(obj1+obj2)