from cardholder import cardholder

def print_menu():
 # Print Options to the user 
  print("Please choose one of the following options:\n")
  print("1.Deposit\n")
  print("2.Withdraw\n")
  print("3.Show Balance\n")
  print("4.Exit")
  
def deposit(cardHolder):
    try :
        deposit = float(input("How much money would you like to deposit: "))
        
    except Exception as error :
        print("Invalid input", error)
        