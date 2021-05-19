class Category:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        print("Amount of {} added to {}".format(amount, self.category))

    def withdraw(self, amount):
        if self.check_balance(amount):
            self.amount -= amount
            #you would print
        else:
            return "Transaction failed"
        
    def balance(self):
        return self.amount
    
    def check_balance(self, amount):
        if self.amount < amount:
            return False
        
        return True
    
    def transfer(self, amount, category):
        if not self.check_balance(amount):
            return "Not successful"
        
        self.amount -= amount
        category.amount += amount
        return "Transfer successful"
    


instance = Category("Food", 500)
instance1 = Category("Car", 400)

instance.deposit(600)
print(instance.balance())
instance.transfer(400, instance1)