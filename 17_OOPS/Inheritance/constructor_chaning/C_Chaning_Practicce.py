#the processs of calling the constructor of parent class into constuctor of child class is known as Constructor chaning
class GrandParent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Object Member Initilized From The Class GrandParent",a,b)
class Parent(GrandParent):
    def __init__(self,b1,b2):
        self.b1=b1
        self.b2=b2
        super().__init__(10,20)
        print("Object Member Initilized From The Parent class",b1,b2)
class Child(Parent):
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2
        super().__init__(40,50)
        print("Object Member Initilized From The child Class",a1,a2)
c=Child(100,200)