class ATM:

    def __init__(self):
        self.c_name = input("Enter The Customer Name")
        self.c_ac_no =input("Enter The Customer Account Number")
        self.c_bal=int(input("Enter The Bank Balance"))
    
    def Deposite(self):
        self.depo=int(input("Enter The Amount To Deposite"))
        self.c_bal=self.c_bal+self.depo
        print("Now Yore Bank Balance Is",self.c_bal)
obj=ATM()
obj.Deposite()


