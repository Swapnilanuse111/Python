#It Is A type Of Inheritance where multiple child classes inherites a properties and methods from same parent class
#It is A Type Of Inheritance Where the Multiple Child Class Inherite The Properties And Methids From the same Parent Class
class A:
    def super1(self):
        print("Call from the A Class")
class B(A):
    def demo(self):
        print("call From The B Class")
class C(A):
    def Show(self):
        print("call From The C Class")
obj=C()
print(obj.Show())
print(obj.super1())