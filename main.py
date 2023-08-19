class Atm:

    # creating the constructor
    def __int__(self):

        # creating the functions
        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):

        user_input = input("""""
         WELCOME TO MY ATM
         1.ENTER 1 TO CREATE THE PIN
         2.ENTER 2 TO DEPOSIT THE AMOUNT
         3.ENTER 3 TO CHECK THE BALANCE
         4.ENTER 4 TO WITHDRAW THE AMOUNT
         
         THANK YOU VISIT AGAIN                            
       """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.balance()
        elif user_input == "4":
            self.withdraw_amt()

    def create_pin(self):
        self.pin = int(input("Enter the pin"))
        print("THE PIN IS CREATED SUCCESFULLLY")
    def deposit(self):
        temp = int(input("Enter the pin"))
        if temp == self.pin:
           amount = int(input("Enter the amount to deposit"))
           self.balance = self.balance=+amount
           print("DEPOSIT IS SUCCESSFUL")
        else:
           print("INVALID PIN")

    def balance(self):
        temp = int(input("Enter the pin"))
        if temp == self.pin:
           print(self.balance)
        else:
           print("Invalid pin")


    def withdraw_amt(self):
            temp = int(input("Enter the pin "))
            if temp == self.pin:
                amount = int(input("Enter the amount withdraw"))
                if amount<self.balance:
                    self.balance = self.balance-amount
                    print("Operation is succcesful")
                else:
                    print("Insufficient balance")
            else:
                print("INVALID PIN")
obj = Atm()
obj.menu()
obj.deposit()
var = obj.balance
obj.withdraw_amt()
var = obj.balance


