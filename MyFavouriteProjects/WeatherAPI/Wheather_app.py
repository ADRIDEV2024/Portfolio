import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Entry
from PIL import Image, ImageTk
import requests as req
import ttkbootstrap as ttkb
from Apiconfig import apikey


root = ttkb.Window(themename="night")
root.title("Weather app")
root.geometry("400x400")

def fetch_weather_icon(icon_url):
    """
    Function to get and create the icon for the app

    return: None
    """
    try:
        image = Image.open(req.get(icon_url, stream=True).raw)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error fetching weather icon: {e}")
        return None

def update_ui(icon, temperature, description, city, country):
    """Function to configure and update the user interface when needed"""
    location_label.configure(text=f"{city}, {country}")

    if icon:
        icon_label.configure(image=icon)
        icon_label.image = icon 
    
    temperature_lbl.configure(text=f"Temperature: {temperature:.2f}ºC")
    description_label.configure(text=f"Description: {description}")

def search():
    """Function to search weather for a city using a get method"""
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return 
    
    icon_url, temperature, description, city, country = result
    icon = fetch_weather_icon(icon_url)
    update_ui(icon, temperature, description, city, country)

    
# ENTRY WIDGET TO ENTER THE CITY NAME

city_entry = ttkb.Entry(root, font="Arial, 14")
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

temperature_lbl = tk.Label(root, font="Arial, 16")
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
