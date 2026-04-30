class Account:
    def __init__(self):
        self.amount = 0
        
    def deposit(self, amount: float):
        self.amount += amount
    
    def withdraw(self, amount: float):   
        if  self.amount < amount:
            raise ValueError("Nie można wypłacić więcej niż posiadamy na koncie")
            
        self.amount -= amount

try:
    my_account = Account()
    my_account.deposit(1000)
    my_account.withdraw(500)
except ValueError as message:
    print(message)