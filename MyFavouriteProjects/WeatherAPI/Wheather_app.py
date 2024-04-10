import tkinter as tk
import requests as req
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttkb


def search():
    """""
    Function to search weather for a city
    using a get method  
    
    """""
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    
def get_weather(city):
    """""
    Function to get weather info using OpenWeatherMap Api 
    
    """""
    APIKEY = "   "
    URL = f"https://api.openweathermap.org/data/3.0/weather?q={city}&appid={APIKEY}"
    request = req.get(URL)
    
    if request.status_code == 404:
        messagebox.showerror("Not found")
        return None
    
    
root = ttkb.Window(themename="night")
root.title("Weather app")
root.geometry("400x400")

# ENTRY WIDGET TO ENTER THE CITY NAME

city_entry = ttkb.Entry(root, font="Cambria, 14")
city_entry.pack(pady=10)

# BUTTON WIDGET TO FOUND WEATHER INFO 

search_button = ttkb.Button(root, text="Search")
search_button.pack(pady=10)

# LABEL WIDGET TO SHOW THE LOCATION NAME 

location_label = tk.Label(root, font="Cambria, 19")
location_label.pack(pady=18)

# LABEL WIDGET TO SHOW THE WEATHER ICON

icon_label = tk.Label(root)
icon_label.pack()

temperature = tk.Label(root, font="Cambria, 16")
temperature.pack()