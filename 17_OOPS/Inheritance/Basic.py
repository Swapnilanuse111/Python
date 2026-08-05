#Inharitance is process of sharing or inheriting properties and methods one class to anathor class
class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Child(Parent):
    pass

Obj=Child("Swapnil",28)
print(Obj.name)