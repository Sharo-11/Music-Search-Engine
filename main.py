from tkinter import *
import fnmatch
import os 
from pygame import mixer
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

root = Tk()
light = "#FFFFFF"
dark = "#000000"
purple = "#500491"
pink = "#f61b60"
green = "#039103"
root.title("Music-Search-Engine")
root.geometry("1000x750+300+10")
root.resizable(False, False)
root.config(bg=light)
mixer.init()

rootpath = "C:\\Users\\sharo\\Desktop\\Music"
pattern = "*.mp3"

listBox = Listbox(root, fg=pink, bg=purple, width=42, height=19, font=("Courier", 12, "bold"))
listBox.place(x=15, y=370)
#===============================================Functions===============================================
def display_songs():
    global listBox
    listBox = Listbox(root, fg=pink, bg=purple, width=42, height=19, font=("Courier", 12, "bold"))
    listBox.place(x=15, y=370)

    for dirs, _, files in os.walk(rootpath):
        for filename in fnmatch.filter(files, pattern):
            listBox.insert('end', filename)

def search_soundcloud(query):
    # Replace YOUR_CLIENT_ID with your actual client ID
    url = f'https://api.soundcloud.com/tracks?q={query}&client_id=YOUR_CLIENT_ID'
    response = requests.get(url)
    tracks = response.json()
    return tracks

def search_online():
    search_entry = Entry(side_panel, font = ("Courier", 14), width = 33)
    search_entry.place(x = 35, y = 320)

    def search_online():
        global listBox
        search_query = search_entry.get()
        tracks = search_soundcloud(search_query)
        listBox.delete(0, END)
        for track in tracks:
            listBox.insert(END, track['title'])

def play():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()
    def play():
        global listBox
        label.config(text=listBox.get("anchor"))
        track_title = listBox.get("anchor")
        tracks = search_soundcloud(track_title)
        if len(tracks) > 0:
            track_url = tracks[0]['stream_url'] + '?client_id=YOUR_CLIENT_ID'
            mixer.music.load(track_url)
            mixer.music.play()
        else:
            print('Track not found on SoundCloud')


def settings():
    pass

def theme():
    global var, como
    var = StringVar()
    como = ttk.Combobox(root, font = ("Courier", 14), state = 'readonly', width = 30, textvariable = var)
    como["values"] = ("Dark", "Light")
    como.current(1)
    como.place(x = 45, y = 370)
    como.bind("<<ComboboxSelected>>", The)

def The(event = None):
    global dark, green, black, pic, photo_ch, photo_d
    theme = var.get()
    if theme == "Dark":
        root.config(bg=green)
        listBox.config(fg=green, bg=dark)
        label.config(fg=green, bg=dark)
        play_btn.config(bg=green) 
        pause_btn.config(bg=green) 
        restart_btn.config(bg=green) 
        stop_btn.config(bg=green) 
        previous_btn.config(bg=green) 
        next_btn.config(bg=green) 
        title_lbl.config(fg = dark)
        side_panel.config(bg=dark)
        photo_d = PhotoImage(file = "images/bg1.png")
        photo_ch.config(image = photo_d)
        for child in side_panel.winfo_children():
            child.configure(bg=light)
    elif theme == "Light":
        root.config(bg=light)
        listBox.config(fg=pink, bg=purple)
        label.config(fg=pink, bg=purple)
        play_btn.config(bg=light) 
        pause_btn.config(bg=light) 
        restart_btn.config(bg=light) 
        stop_btn.config(bg=light) 
        previous_btn.config(bg=light) 
        next_btn.config(bg=light)
        title_lbl.config(bg=purple)
        photo_d = PhotoImage(file = "images/photo.png")
        photo_ch.config(image = photo_d)
        for child in title_lbl.winfo_children():
            child.configure(bg = pink)
        side_panel.config(bg=purple)
        for child in side_panel.winfo_children():
            child.configure(bg=light)
    como.destroy()

def pause():
    if pause_btn["text"] == "Pause":
        mixer.music.pause()
        pause_btn["text"] = "Play"
    else:
        mixer.music.unpause()
        pause_btn["text"] = "Pause"

def restart():
    mixer.music.rewind()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def previous():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text = prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


label = Label(root, text = "", fg = pink, bg = purple, font = ("Courier", 14, "bold"), width = 45, height = 2)
label.place(x = 470, y = 500)

#===============================================LEFT===============================================
side_panel = Frame(root, width = 450, height = 750, bg = purple)
side_panel.pack(side = LEFT)
title_lbl = Label(side_panel, text = "MUSIC-SEARCH-ENGINE", font = ("Courier", 23, "bold"), fg = pink, bg = purple)
title_lbl.place(x = 35, y = 35)
#------------------------------------------------Stuff------------------------------------------------
all_songs_btn = Button(side_panel, text = "All songs", font = ("Lucida Console", 15), command = display_songs, bg = light, bd = 0, height = 2, width = 30)
all_songs_btn.place(x = 35, y = 125)
search_btn = Button(side_panel, text = "Search Online", font = ("Lucida Console", 15), command = search_online, bg = light, bd = 0, height = 2, width = 30)
search_btn.place(x = 35, y = 185)
theme_btn = Button(side_panel, text = "Themes", font = ("Lucida Console", 15), command = theme, bg = light, bd = 0, height = 2, width = 30)
theme_btn.place(x = 35, y = 245)

#===============================================RIGHT===============================================
pic_frame = Frame(root, width=425, height=425)
pic_frame.place(x = 500, y = 30)
photo_bg = PhotoImage(file="images/photo.png")
photo_ch = Label(pic_frame, image=photo_bg, bg = light)
photo_ch.pack()
#------------------------------------------------Play button------------------------------------------------
play_img = Image.open("images/play.png")
play_img = play_img.resize((30,30), Image.LANCZOS)
play_ch = ImageTk.PhotoImage(play_img)
play_icon = Label(root, image=play_ch, bg = light)
play_icon.image = play_ch  
play_icon.place(x=600, y=600)  
play_btn = Button(root, text = "Play", image=play_ch, command=play, bg = light, relief = FLAT)
play_btn.place(x=600, y=600)
#------------------------------------------------Pause button------------------------------------------------
pause_img = Image.open("images/pause.png")
pause_img = pause_img.resize((30,30), Image.LANCZOS)
pause_ch = ImageTk.PhotoImage(pause_img)
pause_icon = Label(root, image=pause_ch, bg = light)
pause_icon.image = pause_ch 
pause_icon.place(x=675, y=600)
pause_btn = Button(root, text = "Pause",image=pause_ch, command=pause, bg = light, relief = FLAT)
pause_btn.place(x=675, y=600)
#------------------------------------------------Restart button------------------------------------------------
restart_img = Image.open("images/restart.png")
restart_img = restart_img.resize((30,30), Image.LANCZOS)
restart_ch = ImageTk.PhotoImage(restart_img)
restart_icon = Label(root, image=restart_ch, bg = light)
restart_icon.image = restart_ch  
restart_icon.place(x= 750, y = 600) 
restart_btn = Button(root, image=restart_ch, command=restart, bg = light, relief = FLAT)
restart_btn.place(x= 750, y = 600)
#------------------------------------------------Stop button------------------------------------------------
stop_img = Image.open("images/stop.png")
stop_img = stop_img.resize((30,30), Image.LANCZOS)
stop_ch = ImageTk.PhotoImage(stop_img)
stop_icon = Label(root, image=stop_ch, bg = light)
stop_icon.image = stop_ch 
stop_icon.place(x= 825, y = 600) 
stop_btn = Button(root, image=stop_ch, command=stop, bg = light, relief = FLAT)
stop_btn.place(x= 825, y = 600)
#------------------------------------------------Previous button------------------------------------------------
previous_img = Image.open("images/previous.png")
previous_img = previous_img.resize((30,30), Image.LANCZOS)
previous_ch = ImageTk.PhotoImage(previous_img)
previous_icon = Label(root, image=previous_ch, bg = light)
previous_icon.image = previous_ch  
previous_icon.place(x= 525, y = 600) 
previous_btn = Button(root, image=previous_ch, command=previous, bg = light, relief = FLAT)
previous_btn.place(x= 525, y = 600)
#------------------------------------------------Next button------------------------------------------------
next_img = Image.open("images/next.png")
next_img = next_img.resize((30,30), Image.LANCZOS)
next_ch = ImageTk.PhotoImage(next_img)
next_icon = Label(root, image=next_ch, bg = light)
next_icon.image = next_ch  
next_icon.place(x= 900, y = 600) 
next_btn = Button(root, image=next_ch, command=next, bg = light, relief = FLAT)
next_btn.place(x= 900, y = 600)

for dirs, _, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

root.mainloop()