from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def dash():
    pass

class main_GUI():
    def __init__(self, root):
        self.root = root
        self.root.title("Music-Search-Engine")
        self.root.geometry("750x600+500+70")

    #=================================Background=================================
        self.root.config(bg = "#EAF2E3")
        dashBoard = Frame(self.root,width = 310, bg = "#B57F50", borderwidth = 4)
        dashBoard.pack(side = LEFT, fill = Y)
        self.dashboard_img = Image.open("images/menu.png")
        self.dashboard_img = self.dashboard_img.resize((40, 40))
        self.dashBoard_icon = ImageTk.PhotoImage(self.dashboard_img)
        dashBoard_icon = Label(self.root, image = self.dashBoard_icon)
        # dashBoard_icon.place(x = 290, y =150)
        dashBoard_btn = Button(self.root, image = self.dashBoard_icon, command = dash)
        dashBoard_btn.place(x = 250, y = 20)
    
obj = main_GUI(root)
root.mainloop()