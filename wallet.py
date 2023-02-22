class Wallet:
    def __init__(self):
        self.balance = 0
	
        
    def setAmount(self, amount):
        self.balance = amount
	
    
    def getAmount(self):
        return self.balance
    
    def addAmount(self, amount):
	self.balance = self.balance + amount
	
    def removeAmount(self, amount):
        self.balance = self.balance - amount

