#THis Example Is Related TO Operator Overloading
#<----Operator Overloading-->
# Operator Overloading Is The Process Of Overloading The Operators TO Works With User Defined DataType As well
class A:
    def __init__(self,data):
        self.data=data
obj1=A(100)
obj2=A(50)
print(obj1+obj2)