class Bank:
    
    def __init__(self):
        self.__maxinterest = 0.01
        
    def getInterest(self)-> float:
        return self.__maxinterest
        
    # def setMaxInterest(self, interest):
    #     self.__maxinterest = interest
      
loan_amount = 1000
bank = Bank()

print(f"Calculation {loan_amount*bank.getInterest()}")




# bank.__maxinterest = 20
# bank.getInterest()

# bank.setMaxInterest(20)
# bank.getInterest()