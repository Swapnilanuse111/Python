#-----What Is Abstraction?-------------#
#-Abstraction Is The Process Of Hiding The Implimentation Detail and Only Displaying The Used to User
#Abstraction is used to hide the important source code but show the Execution
#In Python Abstrcation Can be Explian In Three Things
#1]Abstract Class
#2]Abstract Method
#3]Concrete Method

#1]Abstract Class--->Abstract class is a type of class Which Is Inherite From Abstract Base Class(ABC
#Absttract Class Is a Type Of Class Which Iherite From ABstract BAse Class
#Abstract Class Is A Type Of Class Which Inherte From Abstract Base Class
from abc import ABC,abstractmethod  #Abstract Class
class Animal(ABC):
    @abstractmethod #Abstract Method
    def sound(self):
        pass
class Dog(Animal):#Concret Class
    def sound(self):
        print("Dog Is Barking")
a=Dog()
a.sound()
