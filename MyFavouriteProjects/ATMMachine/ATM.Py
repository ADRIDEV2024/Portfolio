from cardholder import cardholder

def print_menu():
 # Print Options to the user 
  print("Please choose one of the following options:\n")
  print("1.Deposit\n")
  print("2.Withdraw\n")
  print("3.Show Balance\n")
  print("4.Exit")
  
def deposit(cardholder):
    try :
        deposit = float(input("How much money would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance()+ deposit)
        print("Successful operation, your new balance is: ", str(cardholder.get_balance()))
        
    except Exception as error :
        print("Invalid input", error)
        

def withdraw (cardholder):
    try :
        withdraw = float(input("How much money would you like to withdraw: "))
        # Check if a user has enough money
        if(cardholder.get_balance() < withdraw):
            print("Insufficient balance :( ")
        else :
             cardholder.set_balance()
             print("Thanks you :)")
            
    except Exception as error :
        print("Invalid input", error)
        
def check_balance(cardholder):
    print("Your current balance: ", cardholder.get_balance())
    

if __name__ == "__main__":
    current_user = cardholder("","","","","")
    
# CREATE A LIST OF CARDHOLDERS WITH CARDNUM,PIN,FIRSTNAME,
# LASTNAME AND A BALANCE
list_cardholders = []
list_cardholders.append(cardholder("123456787654", 4321, "Jonh", "Pitt", 280.50 ))
list_cardholders.append(cardholder("223456787655", 1234, "Alejandro", "Gonzalez", 90.50 ))
list_cardholders.append(cardholder("123456787654", 5521, "Anna", "Smith", 0.00 ))
list_cardholders.append(cardholder("123456787654", 4321, "Jonhy", "Depp", 57,280.50 ))

# PROMPT USER FOR DEBIT CARD NUMBER 
debitCardNum = ""

while True:
    try:
       debitCardNum= input("Please,insert your debit card: ")
       cardMatch= [holder for holder in list_cardholders if holder.cardNum == debitCardNum]
       if (len(cardMatch) > 0):
           current_user = cardMatch[0]
           break
    except Exception :
        print("Card number not recognized. Please try again ")
        