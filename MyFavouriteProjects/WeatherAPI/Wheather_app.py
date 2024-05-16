import tkinter as tk
import requests as req
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttkb
from Apiconfig import apikey


root = ttkb.Window(themename="night")
root.title("Weather app")
root.geometry("400x400")



def get_weather(city):
    """""
    Function to get weather info using OpenWeatherMap Api 
    
    """""
    APIKEY = Apiconfig.apikey
    URL = f"https://api.openweathermap.org/data/3.0/weather?q={city}&appid={APIKEY}"
    req = req.get(URL)
    
    if req.status_code == 404:
        messagebox.showerror("Not found")
        return None

def search():
    """""
    Function to search weather for a city
    using a get method  
    
    """""
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return None
     # If the city is found, unpack the weather information
    icon_url,temperature,description,city,country = result 
    location_label.configure(text=f"{city},{country}")
    
    image = Image.open(req.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon 
    
    temperature_lbl.configure(text=f"Temperature: {temperature:.2f}ºC")
    description_label.configure(text=f"Description: {description}")
    
    
# ENTRY WIDGET TO ENTER THE CITY NAME

city_entry = ttkb.Entry(root, font="Cambria, 14")
city_entry.pack(pady=10)

# BUTTON WIDGET TO FOUND WEATHER INFO 

search_button = ttkb.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# LABEL WIDGET TO SHOW THE LOCATION NAME 

location_label = tk.Label(root, font="Cambria, 19")
location_label.pack(pady=18)

# LABEL WIDGET TO SHOW THE WEATHER ICON

icon_label = tk.Label(root)
icon_label.pack()

temperature_lbl = tk.Label(root, font="Cambria, 16")
temperature_lbl.pack()

description_label = tk.Label(root, font="Cambria, 16")
description_label.pack()

    

# Parse the response in JSON to get weather information

weather = req.json()
icon_id = weather["weather"][0]["icon"]
temperature = weather["main"]["temp"] - 273.15
description = weather["weather"][0]["description"]
city = weather["name"]
country = weather["sys"]["country"]


def get_icon(icon_url):
    """"
    Get the icon url and return all the weather data
    """""
    icon_url = f"https://openweathermap.org/img/wm/{icon_id}@2x.png"
    return (icon_url,temperature,description,city,country)
    



root.mainloop()
