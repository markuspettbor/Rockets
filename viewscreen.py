import pygame as pg

class Screen(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        #pg.display.init()
        pg.display.set_mode((self.w, self.h))

    def update(self):
        pass

    def close(self):
        pg.display.quit()

if __name__ == '__main__':
    width = 1920 # Can't remember resolution things
    height = 1080
    test = Screen(width, height)
    running = True
    while running:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                test.close()
                running = False
