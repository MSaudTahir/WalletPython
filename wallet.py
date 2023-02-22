class Wallet:
    def __init__(self):
        self.balance = 0
	
        
    def setAmount(self, amount):
        self.balance = amount
	
    
    def getAmount(self):
        return self.balance
    
    def removeAmount(self, amount):
        self.balance = self.balance - amount

