class Car:
    def __init__(self,c_brand,c_model,c_price):
        self.c_brand=c_brand
        self.c_model=c_model
        self.c_price=c_price
    
    def Display(self):
        print("The Car Brand is",self.c_brand)
        print("The Car Brand is",self.c_model)
        print("The Car Brand is",self.c_price)
Display=Car()
Car1=Car("Tata","Punch",20000)
print(Car1.c_brand)
Car2=Car("Mahindra","TAta",2187218)
print(Car2.c_price)
        