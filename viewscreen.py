import tkinter as tk
import numpy as np
import img_tools as it
from PIL import Image, ImageTk


class Screen(object):
    def __init__(self, master, w, h):
        self.master = master
        self.w = w
        self.h = h
        self.count = 0
        self.set_initial()
        self.test_screen()

    def set_initial(self):
        img = it.blank_img(self.w, self.h, 'red')
        #img  = ImageTk.PhotoImage(img)
        self.frame = tk.Label(self.master, image  = img)
        self.frame.image = img
        self.frame.grid(column = 0, row = 0)

    def add_image(self):
        pass

    def update_image(self, img):
        self.frame.configure(image = img)
        self.frame.image = img
        self.frame.grid(column = 0, row = 0)

    def test_screen(self):
        greens = 2*['green']
        reds = 2*['red']
        blues = 2*['blue']
        cols = greens + reds + bleus + greens
        i = cols[self.count]
        self.update_image(it.blank_img(self.w, self.h, i))
        self.count += 1
        self.master.after(int(1000/30), self.test_screen)


if __name__ == '__main__':
    root = tk.Tk()
    test = Screen(root, w = 1920, h = 1080)
    root.mainloop()
