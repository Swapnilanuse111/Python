class Parent:
    def __init__(self):
        print("Call from the parent class")
class Child(Parent):
    def __init__(self):
        print("Call From The Child Class")
        super().__init__()
class ABC(Child):
    def __init__(self):
        print('Call from the ABC Class')
        super().__init__()
obj=ABC()



