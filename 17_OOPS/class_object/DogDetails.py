class Dog:
    def __init__(self,d_name,d_age,d_breed):
        self.d_name=d_name
        self.d_age=d_age
        self.d_breed=d_breed
    
    def bark(self):
        print("Most Of The Time The Dog Is Barking In The Time Of Night")

    def disply(self):
        print(self.d_name)
        print(self.d_age)
        print(self.d_breed)
obj1=Dog("Sonya",22,"German Sheferd")
obj1.disply()
obj1.bark()
obj2=Dog("Monya",21,"German Sheferd Orignal")
obj2.bark()
obj2.disply()