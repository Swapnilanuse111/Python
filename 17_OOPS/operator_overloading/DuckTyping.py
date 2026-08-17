#In Duck Typing We Care About What An Object Can Do We Do not Check What Type It Is
class Dog:
    def sound(self):
        print("Dog IS Braking")

class Duck:
    def sound(self):
        print("Duck Is Quack")
def mack_sound(animal):
    animal.sound()
d=Dog()
a=Duck()
mack_sound(d)
mack_sound(a)