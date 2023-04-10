from tkinter import *
import fnmatch
import os 
from pygame import mixer
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title("Music-Search-Engine")
root.geometry("1000x750+300+10")
root.resizable(False, False)
root.config(bg = "#FFFFFF")

rootpath = "C:\\Users\\sharo\\Desktop\\Music"
pattern = "*.mp3"


listBox = Listbox(root, fg = "#f61b60", bg = "#500491", width = 42, height = 19, font = ("Courier", 12, "bold"))
listBox.place(x = 15, y = 370)

#===============================================Functions===============================================
def display_songs():
    global listBox
    listBox = Listbox(root, fg = "#f61b60", bg = "#500491", width = 42, height = 19, font = ("Courier", 12, "bold"))
    listBox.place(x = 15, y = 370)

    for dirs, _, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            listBox.insert('end', filename)

def play():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def settings():
    pass

def theme():
    pass

def pause():
    pass

def restart():
    pass

def stop():
    pass

def previous():
    pass

def next():
    pass

def search_online():
    pass

label = Label(root, text = "", bg = "black", fg = "yellow", font = ("Courier", 23, "bold"), width = 25, height = 1)
label.place(x = 500, y = 500)

#===============================================LEFT===============================================
side_panel = Frame(root, width = 450, height = 750, bg = "#500491")
side_panel.pack(side = LEFT)
title_lbl = Label(side_panel, text = "MUSIC-SEARCH-ENGINE", font = ("Courier", 23, "bold"), fg = "#f61b60", bg = "#500491")
title_lbl.place(x = 35, y = 35)
#------------------------------------------------Stuff------------------------------------------------
all_songs_btn = Button(side_panel, text = "All songs", font = ("Lucida Console", 15), command = display_songs, bg = "white", bd = 0, height = 2, width = 30)
all_songs_btn.place(x = 35, y = 125)
search_btn = Button(side_panel, text = "Search Online", font = ("Lucida Console", 15), command = search_online, bg = "white", bd = 0, height = 2, width = 30)
search_btn.place(x = 35, y = 185)
settings_btn = Button(side_panel, text = "Settings", font = ("Lucida Console", 15), command = settings, bg = "white", bd = 0, height = 2, width = 30)
settings_btn.place(x = 35, y = 245)
theme_btn = Button(side_panel, text = "Themes", font = ("Lucida Console", 15), command = theme, bg = "white", bd = 0, height = 2, width = 30)
theme_btn.place(x = 35, y = 305)

#===============================================RIGHT===============================================
photo_img = Image.open("images/photo.png")
photo_img = photo_img.resize((465,425), Image.LANCZOS)
photo_ch = ImageTk.PhotoImage(photo_img)
photo_bg = Label(root, image = photo_ch)
photo_bg.place(x = 500, y = 30)

#------------------------------------------------Play button------------------------------------------------
play_img = Image.open("images/play.png")
play_img = play_img.resize((30,30), Image.LANCZOS)
play_ch = ImageTk.PhotoImage(play_img)
play_icon = Label(root, image=play_ch, bg = "white")
play_icon.image = play_ch  # Store a reference to the image to prevent it from being garbage collected
play_icon.place(x=600, y=600)  # Add the play_icon label to the window
play_btn = Button(root, image=play_ch, command=play, bd = 0, bg = "white")
play_btn.place(x=600, y=600)
#------------------------------------------------Pause button------------------------------------------------
pause_img = Image.open("images/pause.png")
pause_img = pause_img.resize((30,30), Image.LANCZOS)
pause_ch = ImageTk.PhotoImage(pause_img)
pause_icon = Label(root, image=pause_ch, bg = "white")
pause_icon.image = pause_ch  # Store a reference to the image to prevent it from being garbage collected
pause_icon.place(x=675, y=600)  # Add the play_icon label to the window
pause_btn = Button(root, image=pause_ch, command=pause, bd = 0, bg = "white")
pause_btn.place(x=675, y=600)
#------------------------------------------------Restart button------------------------------------------------
restart_img = Image.open("images/restart.png")
restart_img = restart_img.resize((30,30), Image.LANCZOS)
restart_ch = ImageTk.PhotoImage(restart_img)
restart_icon = Label(root, image=restart_ch, bg = "white")
restart_icon.image = restart_ch  # Store a reference to the image to prevent it from being garbage collected
restart_icon.place(x= 750, y = 600)  # Add the play_icon label to the window
restart_btn = Button(root, image=restart_ch, command=restart, bd = 0, bg = "white")
restart_btn.place(x= 750, y = 600)
#------------------------------------------------Stop button------------------------------------------------
stop_img = Image.open("images/stop.png")
stop_img = stop_img.resize((45,45), Image.LANCZOS)
stop_ch = ImageTk.PhotoImage(stop_img)
stop_icon = Label(root, image=stop_ch, bg = "white")
stop_icon.image = stop_ch  # Store a reference to the image to prevent it from being garbage collected
stop_icon.place(x= 825, y = 590)  # Add the play_icon label to the window
stop_btn = Button(root, image=stop_ch, command=stop, bd = 0, bg = "white")
stop_btn.place(x= 825, y = 590)
#------------------------------------------------Previous button------------------------------------------------
previous_img = Image.open("images/previous.png")
previous_img = previous_img.resize((30,30), Image.LANCZOS)
previous_ch = ImageTk.PhotoImage(previous_img)
previous_icon = Label(root, image=previous_ch, bg = "white")
previous_icon.image = previous_ch  # Store a reference to the image to prevent it from being garbage collected
previous_icon.place(x= 525, y = 600)  # Add the play_icon label to the window
previous_btn = Button(root, image=previous_ch, command=previous, bd = 0, bg = "white")
previous_btn.place(x= 525, y = 600)
#------------------------------------------------Next button------------------------------------------------
next_img = Image.open("images/next.png")
next_img = next_img.resize((40,40), Image.LANCZOS)
next_ch = ImageTk.PhotoImage(next_img)
next_icon = Label(root, image=next_ch, bg = "white")
next_icon.image = next_ch  # Store a reference to the image to prevent it from being garbage collected
next_icon.place(x= 900, y = 590)  # Add the play_icon label to the window
next_btn = Button(root, image=next_ch, command=next, bd = 0, bg = "white")
next_btn.place(x= 900, y = 590)

for dirs, _, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

root.mainloop()