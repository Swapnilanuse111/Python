class Car:

    c_brand = "BMW"
    c_model = "XR"
    c_price = 1000000

    @classmethod
    def display(cls):
        print(cls.c_brand)
        print(cls.c_model)
        print(cls.c_price)

    def start(self):
        print("Car Is Started")

    def stop(self):
        print(self.c_brand, "Car Is Stopped")

obj = Car()
Car.display()
obj.start()
obj.stop()