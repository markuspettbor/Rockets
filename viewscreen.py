import tkinter as tk
import numpy as np
import img_tools as it
from PIL import Image, ImageTk, ImageDraw

import time
import random

class Screen(object):
    def __init__(self, master, w, h):
        self.master = master
        self.w = w
        self.h = h
        self.count = 0
        self.set_initial()

    def set_initial(self):
        img = it.blank_img(self.w, self.h, 'white')
        img  = ImageTk.PhotoImage(img)
        self.frame = tk.Label(self.master, image  = img)
        self.frame.image = img
        self.frame.grid(column = 0, row = 0)

    def add_image(self):
        pass

    def update_image(self, img):
        img = ImageTk.PhotoImage(img)
        self.frame.configure(image = img)
        self.frame.image = img
        self.frame.grid(column = 0, row = 0)

if __name__ == '__main__':
    root = tk.Tk()
    test = Screen(root, w = 1920, h = 1080)
    root.mainloop()
