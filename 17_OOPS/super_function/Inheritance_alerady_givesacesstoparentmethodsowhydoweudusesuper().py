#Because When The Child Class Overrides A Parent Method And Still Want to Use Teh Parent

#OK
#In Inheritance The Chld Class Can Use Parent Methods Directly

#Example 
class A:
    def show(self):
        print("This Is The Parent Class")
class B(A):
    pass
obj=B()
obj.show()

#So Yes Inheritance Aleready Allows Acess To Parent Class 
#Then why We Need Super() function

#Without Using Super() function

class Parent:
    def show(self):
        print("Call From The Parent Class")
class Child(Parent):
    def show(self):
        print("Call From The Child1 Class")
c=Child2()
c.show()

#In That Eg Parent Method Is Hidden 

#With Super Function
#By Using Super Function We Can Easily acees Method And Properties From Parent Class TO Child Class
class Parent:
    def show(self):
        print("Call From The Parent Class")
class Child1(Parent):
    def show(self):
        print("Call From The Chiild Class")
        super().show()
obj=Child1()
obj.show