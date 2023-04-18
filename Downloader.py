import os
import requests
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *

def browse_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    path_label.config(text=folder_path)

def download():
    url1 = entry1.get()
    url2 = entry2.get()
    file_type = var.get()

    if not url1 and not url2:
        status_label.config(text="Error: Ingresa al menos una URL")
        return

    if not folder_path:
        status_label.config(text="Error: Selecciona una carpeta de destino")
        return

    if url1:
        try:
            yt = YouTube(url1)
            stream = yt.streams.get_highest_resolution()
            file_title = stream.title
            status_label.config(text="Descargando video 1...")
            stream.download(output_path=folder_path)
            status_label.config(text="Video 1 descargado!")
            if file_type == "mp3":
                status_label.config(text="Convirtiendo a MP3...")
                video_path = os.path.join(folder_path, file_title + ".mp4")
                audio_path = os.path.join(folder_path, file_title + ".mp3")
                video = VideoFileClip(video_path)
                audio = video.audio
                audio.write_audiofile(audio_path)
                video.close()
                os.remove(video_path)
                status_label.config(text="Archivo 1 convertido a MP3!")
        except Exception as e:
            print(e)
            status_label.config(text="Error al descargar o convertir el archivo 1")

    if url2:
        try:
            yt = YouTube(url2)
            stream = yt.streams.get_highest_resolution()
            file_title = stream.title
            status_label.config(text="Descargando video 2...")
            stream.download(output_path=folder_path)
            status_label.config(text="Video 2 descargado!")
            if file_type == "mp3":
                status_label.config(text="Convirtiendo a MP3...")
                video_path = os.path.join(folder_path, file_title + ".mp4")
                audio_path = os.path.join(folder_path, file_title + ".mp3")
                video = VideoFileClip(video_path)
                audio = video.audio
                audio.write_audiofile(audio_path)
                video.close()
                os.remove(video_path)
                status_label.config(text="Archivo 2 convertido a MP3!")
        except Exception as e:
            print(e)
            status_label.config(text="Error al descargar o convertir el archivo 2")

root = Tk()
root.title("YTDownloader By-Budda")
root.geometry("500x250")

var = StringVar()
var.set("mp4")

label1 = Label(root, text="Ingresa la URL del primer video:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Ingresa la URL del segundo video:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

mp3_radio = Radiobutton(root, text=".mp3", variable=var, value="mp3")
mp3_radio.pack()

mp4_radio = Radiobutton(root, text=".mp4", variable=var, value="mp4")
mp4_radio.pack()

folder_button = Button(root, text="Selecciona la carpeta de destino", command=browse_folder)
folder_button.pack()

path_label = Label(root, text="No se ha seleccionado ninguna carpeta")
path_label.pack()

download_button = Button(root, text="Descargar", command=download)
download_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
