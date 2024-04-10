import tkinter as tk
import requests as req
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttkb

root = ttkb.Window(themename="night")
root.title("Weather app")
root.geometry("400x400")

# ENTRY WIDGET TO ENTER THE CITY NAME

city_entry = ttkb.Entry(root, font="Cambria, 14")
city_entry.pack(pady=10)

# BUTTON WIDGET TO FOUND WEATHER INFO 

search_button = 