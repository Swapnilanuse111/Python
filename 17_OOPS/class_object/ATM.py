class ATM:
    def __init__(self):
        self.c_name = input("Enter The Customer Name:-")
        self.c_ac_no =input("Enter The Customer Account Number:-")
        self.c_bal=2000
    
    def Deposite(self):
        self.depo=int(input("Enter The Amount To Deposite:-"))
        if self.depo >= 100:
            self.c_bal=self.c_bal+self.depo
            print("Now Yore Bank Balance Is:-",self.c_bal)
        else:
            print("Youre Ammount Is Not Suficient For Add")

    def Withdrow(self):
        self.Withdrow=int(input("Enter The Amoount How Manny Withdrow:-"))
        if self.Withdrow<self.c_bal:
            self.c_bal=self.c_bal-self.Withdrow
            print("Your Money Withdrow Sucessfully")
            print("Avalable Balance is:-",self.c_bal)
        else:
            print("In Youre Bank Account There Is No Suficent Balance")
obj=ATM()
obj.Deposite()
obj.Withdrow()