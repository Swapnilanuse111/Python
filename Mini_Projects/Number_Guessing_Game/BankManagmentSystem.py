class BankAccount:

    b_name = "BIO"
    b_location = "Hadapsar"

    def __init__(self, c_id, c_name, c_ac_no, balance):

        self.c_id = c_id
        self.c_name = c_name
        self.c_ac_no = c_ac_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance


Account1 = BankAccount(101, "swapnil", 13102003, 2000)
print("First Costomer Data")
print(Account1.c_id)
print(Account1.c_name)
print(Account1.c_ac_no)
print(Account1.get_balance())
Account2 = BankAccount(102, "Rahul", 13102003, 3000)

print("Secoend Costomer Data")
print(Account2.c_id)
print(Account2.c_name)
print(Account2.c_ac_no)
print(Account2.get_balance())