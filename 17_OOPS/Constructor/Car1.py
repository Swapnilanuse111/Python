#Create a Car class using constructor
class Car:
    def __init__(self,c_name,c_model,c_price):
        self.c_name=c_name
        self.c_model=c_model
        self.c_price=c_price
c=Car("Tata",555,200000)
print(c.c_name,c.c_model,c.c_price)
