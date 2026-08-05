#constructor is inbuild or predefined method in python which is created inside the class
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
Emp_1=Student("Swapnil",30)
print(Emp_1.name)