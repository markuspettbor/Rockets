import random
import pygame as pg

class Euler_cromer:
    def __init__(self, s, v, dt):
        self.s = s
        self.v = v
        self.dt = dt

    def acc(self, t = 0):
        return 0

    def calculate(self, t = 0):
        self.v = self.v + self.dt*self.acc(t)
        self.s = self.s + self.dt*self.v
        return self.s, self.v

class Gravity(Euler_cromer):
    def acc(self, t = 0):
        return 9.81

def draw_circle(x, y, surf):
    radius = 1
    pg.draw.circle(surf, (255,255,255,255), (x, y), radius)


def test():
    import viewscreen as vs
    width = 1920
    height = 1080
    dt = 0.01
    test = vs.Screen(width, height)
    x = Euler_cromer(1000, 10, dt)
    y = Gravity(1000, -100, dt)
    testrun = True
    surf = pg.display.get_surface()
    while testrun:
        pg.time.delay(1)
        draw_circle(int(x.s), int(y.s), surf)
        pg.display.flip()
        x.calculate()
        y.calculate()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                test.close()
                testrun = False

if __name__ == '__main__':
    test()
