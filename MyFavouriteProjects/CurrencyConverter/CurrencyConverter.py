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
    
url= "https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"

Payload= {}
header={
"apikey: 9sSG7LPikh55WQQli023V8LipQI43"  
} 
response= req.request("GET", url, header=header, data= Payload)
status_code= response.status_code
 
 # CHECK IF WE HAVE A PROBLEM WITH GET REQUEST    
if status_code != 200:
    response = response.json()
    print("Error response" + str(response))
    quit()

response = response.json()
print("Convertion result: " + str(response))


if __name__ == "__main__":
 convert_currency()