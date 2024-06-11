import requests as req
from config import apikey

def convert_currency():
    initial_currency = input("\nEnter your initial currency : \n")
    target_currency = input("Enter your target currency :\n ")
    
    while True:
    
     try:
      amount = float(input("Enter the amount: \n"))
        
     except TypeError:
        print("Sorry, the amount needs to be numeric\n")
    
     if not amount>0:
         print("Sorry, the amount needs to be greater than 0")
         continue
     else:
         break
    
url = "https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"

Payload = {}
header = {
    "apikey:apiconfig"
}
 
response = req.request("GET", url, header=header, data= Payload)
status_code = response.status_code
 
 # CHECK IF WE HAVE A PROBLEM WITH GET REQUEST    
if status_code != 200:
    response = response.json()
    print("Error response" + str(response))
    quit()

response = response.json()



if __name__ == "__main__":
 convert_currency()
