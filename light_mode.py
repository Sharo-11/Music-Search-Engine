from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def dash():
    pass

def all_songs():
    pass

def resize_img(self, pic):
    self.old_img = Image.open("images/{img}.png".format(img = pic))
    self.olg_img = self.old_img.resize((40, 40))
    self.new_img = ImageTk.PhotoImage(self.old_img)
    # new_img = Label(self.root, image = self.new_img)

class main_GUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Music-Search-Engine")
        self.root.geometry("750x600+500+70")
        self.root.config(bg = "#EAF2E3")

    #=================================LEFT FRAME=================================
        dashBoard = Frame(self.root,width = 280, height = 900, bg = "#B57F50", borderwidth = 4) 
        dashBoard.pack(side = LEFT)
        self.dashboard_img = Image.open("images/menu.png")
        self.dashboard_img = self.dashboard_img.resize((40, 40))
        self.dashBoard_icon = ImageTk.PhotoImage(self.dashboard_img)
        # resize_img(self, menu)
        dashBoard_icon = Label(self.root, image = self.dashBoard_icon)
        dashBoard_btn = Button(self.root, image = self.dashBoard_icon, command = dash, bg = "#B57F50", bd = 0)
        dashBoard_btn.place(x = 230, y = 20)
        title_lbl = Label(dashBoard, text = "Dashboard", font = ("Algerian", 22, "bold"), fg = "#EAF2E3", bg = "#B57F50")
        title_lbl.place(x = 30, y = 20)
        
        self.all_songs_img = Image.open("images/music.png")
        self.all_songs_img = self.all_songs_img.resize((30,30))
        self.all_songs_icon = ImageTk.PhotoImage(self.all_songs_img)
        all_songs_icon = Label(dashBoard, image = self.all_songs_icon, bg = "#B57F50")
        all_songs_icon.place(x = 15, y = 100)

        #=================================DOWN FRAME =================================
        music_control =Frame(self.root, width = 800, height = 120, bg = "#B57F50", borderwidth = 4)
        music_control.pack(side = BOTTOM, fill = X)
obj = main_GUI(root)
root.mainloop()

#Fonts that can be used, Algerian, Comic Sans MS, Courier New