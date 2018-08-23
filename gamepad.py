import tkinter as tk

class Controller(object):
    def __init__(self, master):
        self.master = master
        self.master.bind('<d>', self.dxr)
        self.master.bind('<a>', self.dxl)
        self.master.bind('<w>', self.dyu)
        self.master.bind('<s>', self.dyd)
        self.master.bind('<e>', self.rotatecw)
        self.master.bind('<q>', self.rotateccw)

    def dxr(self, event, direction = 'right'):
        print('Turned right')

    def dxl(self, event):
        print('Turned left')

    def dyu(self, event, direction = 'up'):
        print('Went up')

    def dyd(self, event):
        print('Went down')

    def rotatecw(self, event):
        print('Turned clockwise')

    def rotateccw(self, event):
        print('Turned counter-clockwise')

if __name__ == '__main__':
    root = tk.Tk()
    test = Controller(root)
    root.mainloop()
