from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def Download_Video(url, save_path):
     """""
     Function that get an url from a yt video,
     download that video in high resolution and 
     save the user path where store the video
     """""
     
     try:
        
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension= "mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded succesfully! ")
            
     except Exception as error:
        print(error)
    
url = ""
save_path = "C:/User/Downloads" # Example directory path to save video

Download_Video(url, save_path)
