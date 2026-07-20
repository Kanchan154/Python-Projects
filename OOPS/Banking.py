class Bank: 
    __balance = 15000000
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount {amount} deposited Sussessfully")
    
    def withdrawl(self, amount):
        if(amount > self.__balance):
            print("Insufficient Balance")
            return
        self.__balance -= amount
        print(f"Amount of {amount} Withdrawl sussessfully")
        
    def viewBalance(self):
        print(f"Your bank balance is: {self.__balance}")
    
obj1 = Bank()
try:
    print("""
          Press 1 for Deposit
          Press 2 for Withdrawl
          Press 3 for View Balance
          Press 4 for exit
          """)
except Exception as error:
    print(error)
while(True):
    option = int(input("Enter the options: "))
    match option:
        case 1: 
            amount = int(input("Enter the amount you want to deposit"))
            obj1.deposit(amount=amount)
        case 2:
            amount = int(input("Enter the amount you want to withdrawl"))
            obj1.withdrawl(amount=amount)
        case 3: 
            obj1.viewBalance()
        case 4:
            exit()
        case _:
            print("Enter the valid option")
        
    