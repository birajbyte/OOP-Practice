  
# Class Name: BankAccount
# Properties: Owner (name), CurrentBalance
# Methods: Deposit(amount), Withdraw(amount), get_balance() 
# Validations: cannot withdraw more than the balance (print insufficient fund message)
# Create two objects (for two people) and do deposit, withdraw, and print their balances
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited Successfully")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw amount: {amount}")
        else:
            print("Insufficient Balance")
    def get_balance(self):
        print(f"Total balance in account name {self.name} : {self.balance}")

person1 = BankAccount("Bob",5000)
person1.deposit(5000)
person1.withdraw(8000)
person1.get_balance()
person2 = BankAccount("Alice",10000)
person2.deposit(1000)
person2.withdraw(5000)
person2.get_balance()
