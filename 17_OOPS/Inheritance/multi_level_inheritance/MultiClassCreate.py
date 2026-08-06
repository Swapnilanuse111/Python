#<-------------MULTI LEVEL INHERITANCE------------>
#it is a type of inheritance whree 2 or more occurence of inheritance exist
# in this type of structure at list one class will a parent class as well as child class
class A: #This Is Parent Class Of Class B
    def Show(self):
        print("The Class A Is Calling")
class B(A):#This Is Child Class of A & Parent of the Class C
#       <--In our Defination A one class will be the parent as well as child so that process is known as the multilevel Inheritance    
    def Disp(self):
        print("Class B Is calling")
class C(B):#This is the Child Class of B
    def Demo(self):
        print("Class C is Calling")
        super().Disp()
        super().Show()
obj=C()
obj.Demo()
