import tkinter as tk

class Controller(object):
    def __init__(self, master):
        self.master = master
        self.master.bind('<d>', self.dx, 'right') # USE LAMBDA HERE
        self.master.bind('<a>', self.dx, 'right')
        self.master.bind('<w>', self.dy, 'up')
        self.master.bind('<s>', self.dy, 'down')
        self.master.bind('<q>', self.rotate, 'ccw')
        self.master.bind('<e>', self.rotate, 'cw')


    def dx(self, event, direction = 'right'):
        if direction == 'right':
            print('Turned right')
        else:
            print('Turned left')

    def dy(self, event, direction = 'up'):
        if direction == 'up':
            print('Went up')
        else:
            print('Went down')

    def rotate(self, event, direction = 'cw'):
        if direction == 'cw':
            print('Turned clockwise')
        else:
            print('Turned Counter-clockwise')

if __name__ == '__main__':
    root = tk.Tk()
    test = Controller(root)
    root.mainloop()
