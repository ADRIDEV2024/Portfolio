import requests as req

def convert_currency():
    initial_currency = input("Enter your initial currency : ")
    target_currency = input("Enter your target currency : ")
    
    while True:
    
     try:
      amount= float(input("Enter the amount: "))
        
     except TypeError:
        print("Sorry, the amount needs to be numeric")
    
     if not amount>0:
         print("Sorry, the amount needs to be greater than 0")
         continue
     else:
         break
    
url= 