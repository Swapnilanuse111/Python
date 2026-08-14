#Super Is Inbuild Function In python It Is Used To Assses Methods and Properties From The Parent class to child class
#Super Is Inbuild Function In Python It used to asses Method And Properties From The Parent Class to child class 
#Super Is Inbuild Function In Python It Is Used To Asess Properties And Method From Parent Class To Child Class
#Super Is Inbuild Function In Python It is Used to acess Properties And Method From Parent Class TO Child Class
class Parent:
    def show(self):
        print("Call From The Parent Class")
class Child(Parent):
    def disp(self):
        print("Call from Child Class")
        super().show()
c=Child()
print(c.disp())
