#Multiple Inheritance Is type of Inheritance where a single child class inherite multiple parent class 
#In this type of inheritance one child class can inherite the properties and method from the multiple parent class
class Parent1:
    def show(self):
        print("Call from the First Parent Class")
        super().show()
class Parent2:
    def show(self):
        print("Call from the Secoend Parent Class")
class Child(Parent1,Parent2):
    def show(self):
        super().show()
        print("This is call from the child class")
obj=Child()
obj.show()
print(Child.mro())