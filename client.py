import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE = 4096

selectSongLabel = None
listbox = None
playButton = None
stopButton = None
uploadButton = None
downloadButton = None
infoLabel = None

def musicWindow():    
    window = Tk()
    window.title('MUSIC WINDOW')
    window.geometry("300x300")
    window.configure(bg="black")

    global selectSongLabel
    global listBox
    global playButton
    global stopButton
    global uploadButton
    global downloadButton
    global infoLabel

    selectSongLabel = Label(window, text = "Select Song", bg = 'white', font = ('Calibri', 8))
    selectSongLabel.place(x=120,y=1)

    listBox = Listbox(window, height = 10, width = 39, activestyle="dotbox",bg = "LightSkyBlue", borderwidth=2, font = ("Calibri", 10))
    listBox.place(x=10,y=18)

    scrollBar1 = Scrollbar(listBox)
    scrollBar1.place(relheight = 1,relx=1)
    scrollBar1.config(command = listBox.yview)

    playButton = Button(window, text = "Play", width = 10, bd = 1, bg = "purple", font = ("Calibri", 10))
    playButton.place(x=30,y=200)

    stopButton = Button(window, text = "Stop", bd = 1, width = 10, bg = "red", font = ("Calibri",10))
    stopButton.place(x=200,y=200)

    uploadButton = Button(window, text = "Upload", width = 10, bd = 1, bg = "yellow", font = ("Calibri", 10))
    uploadButton.place(x=30,y=250)

    downloadButton = Button(window, text = "Download", bd = 1, width = 10,bg = "green", font = ("Calibri",10))
    downloadButton.place(x=200,y=250)

    infoLabel = Label(window, text = "", fg = "blue", font = ("Calibri",8))
    infoLabel.place(x=4,y=280)

    window.mainloop()

def setup():

    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()
