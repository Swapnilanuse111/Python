#Hirarchical Inheritance It Is A type Of Innheritance Where The Multiple Child Class Inherite The Properties And Methods From The Same Parent Class
class A:
    x=20
class B(A):
    def Add(self,a,b):
        print(a+b)
class C(A):
    pass
obj=B()
print(obj.Add(20,10))