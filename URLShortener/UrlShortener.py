import requests as rq
import Apiconfig as Apic


def shorten_link(full_link, link_name):
    API_KEY = Apic.API_KEY
    BASE_URL = "https://cuttly.ly/api/api.php" 
    
    payload = {"key": API_KEY, "short":full_link, "name":link_name}
    requests = rq.get(BASE_URL, params=payload)
    data = rq.json(requests)
        
    try:
        title = data["url"]["title"]
        short_link = data["url"]["shortlink"]
        print(f"TITLE: {title}")
        print(f"Short link: {short_link})
    
    except Exception as error:
           status = data["url"]["status"]
           print("Error Status:", status, error)
                            
 link = input("Enter the link you want to trim : ")
 name = input("Enter a name for your link: ")
                                    
    
            
        
if __name__ == "__main__":
shorten_link(link, name)
