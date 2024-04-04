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
        
def check_balance():
        