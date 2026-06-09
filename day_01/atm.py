class Atm:
    #Constructor that assist to make blueprint of class
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        while True:
            user_input = input("""
            How would you like to proceed?
            1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
                            """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
                    
            elif user_input == "5":
                return
                    
            else:
                print("Invalid choice")
                
    def create_pin(self):
        while True:
            pin = input("Enter your pin:")
            if pin == "":
                print("Pin cannot be empyt ! Try again")
            else:
                self.pin = pin
                print("Pin setup completely")
                break
    def deposit(self):
        if self.pin == "":
            print("Create pin first")
            return
        pin = input("Enter your Atm pin:")
        if self.pin == pin:
            amount = int(input("Enter the amount to deposit:"))
            self.balance += amount
            print(f"Total balance after deposit {self.balance}")
        else:
            print("Invalid pin")
    def withdraw(self):
        if self.pin == "":
            print("Create pin first")
            return
        pin = input("Enter your Atm pin:")
        if self.pin == pin:
            withdraw_amount = int(input("Enter the amount:"))
            if withdraw_amount <= self.balance:
                self.balance -= withdraw_amount
                print(f"Withdral Balance {self.balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
    def check_balance(self):
        if self.pin == "":
            print("Create pin first")
            return
        pin = input("Enter your atm pin:")
        if self.pin == pin:
            print(f"Balance in account {self.balance}")
c = Atm()

          
          





