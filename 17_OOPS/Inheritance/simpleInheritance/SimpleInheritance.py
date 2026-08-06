#Single Level Is type of Inheritance where the only one parent class and only one child class 
#it is the simplest type of inheritance where a single child class Directly Inherite the Parent class 
class A:#Parent class
    def Show(self):
        print("Hello From The Parent class")
class B(A):
    def Disp(self):
        print("Hello From Child Class")
        super().Show()
obj=B()
obj.Disp()

