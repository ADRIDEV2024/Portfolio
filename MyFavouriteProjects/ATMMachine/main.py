
class CardHolder():
    def __init__(self,cardNum,pin,firstname,lastname,balance):
        
        self.cardNum = cardNum
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance 
        
#GETTER METHODS
    
    def get_cardNum(self):
        return self.cardNum
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance

#SETTER METHODS 

    def set_cardNum(self,NewVal):
        self.cardNum = NewVal
    def get_pin(self,NewVal):
        self.pin = NewVal
    def get_firstname(self,Newval):
        self.firstname = Newval
    def get_lastname(self,NewVal):
        self.lastname = NewVal
    def get_balance(self,NewVal):
        self.balance = NewVal 
        
    def print_out(self):
        print("Card #: ", self.cardNum)
        print("Pin: ", self.pin)
        print("Firstname: ", self.firstname)
        print("Lastname: ", self.lastname)
        print("Balance: ", self.balance)


    
    