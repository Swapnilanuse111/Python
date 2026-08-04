class ATM:
    # Class Variables
    name = "ICICI"
    branch = "Hadapsar"

    # Constructor
    def __init__(self, c_name, c_ac_no, c_bal=2000):
        self.c_name = c_name
        self.c_ac_no = c_ac_no
        self.c_bal = c_bal

    # Check Balance
    def ch_bal(self):
        return self.c_bal

    # Deposit Money
    def deposit(self, amt):
        if amt >= 100:
            self.c_bal += amt
            print("\nAmount Deposited Successfully.")
            print("Current Balance:", self.c_bal)
        else:
            print("\nInvalid Amount. Minimum deposit is ₹100.")

    # Withdraw Money
    def withdraw(self, amt):
        if amt >= 100:
            if amt > self.c_bal:
                print("\nInsufficient Balance.")
            else:
                self.c_bal -= amt
                print("\nAmount Withdrawn Successfully.")
                print("Current Balance:", self.c_bal)
        else:
            print("\nInvalid Amount. Minimum withdrawal is ₹100.")


# ===============================
# OBJECT CREATION
# ===============================

customer = ATM(
    input("Enter Customer Name: "),
    input("Enter Account Number: ")
)

print("\nAccount Registered Successfully!")

# ===============================
# MENU
# ===============================

while True:
    print("\n========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    opt = int(input("Enter Your Choice: "))

    if opt == 1:
        print("\nCurrent Balance:", customer.ch_bal())

    elif opt == 2:
        amt = int(input("Enter Deposit Amount: "))
        customer.deposit(amt)

    elif opt == 3:
        amt = int(input("Enter Withdrawal Amount: "))
        customer.withdraw(amt)

    elif opt == 4:
        print("\nThank You for Using ICICI ATM!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")