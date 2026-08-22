class Book:
    b_name="Power Of SubConcinous Mind"
    b_price=300
    def disply(self):
        print(self.b_name)
        print(self.b_price)
    def Discount(self):
        discount=self.b_price*10/100
        print("The Final Price Of Book Is:-",self.b_price-discount)
obj=Book()
print(obj.disply())
print(obj.Discount())