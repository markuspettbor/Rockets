from viewscreen import Screen
import numpy as np
import pygame as pg

class Wall:
    def __init__(self, w, h, normal_vector, position):
        '''
        w, h, is the width and height of a rectangular wall.
        Assumes normal_vector is a numpy array on the form [x, y, z]
        The normal_vector determines the orientation of the wall relative
        to the center of a box.
        '''
        self.w = w
        self.h = h
        self.normal_vector = normal_vector
        self.position = position

    def __call__(self):
        print('wall coordinates returned')

    def get_corners(self):
        '''
        Finds corners in a rectangle of width w, height h, for a given
        normal_vector. Idea: Find a vector in the plane, cross that vector
        with the normal vector, and get a vector perpendicular to the vector
        in the plane. The two can then be used to span a rectangle.

        For future: Should redo entire code. Should also add option
        to build a wall from an existing one.
        '''
        a, b, c = self.normal_vector
        x0, y0, z0 = self.position
        p = np.array([0, 0, a/c*x0 + b/c*y0 + z0])
        tryvec = p - self.position
        othervec = np.cross(tryvec, self.normal_vector)
        res1 = self.position + tryvec/np.linalg.norm(tryvec)*self.w/2 + othervec/np.linalg.norm(othervec)*self.h/2
        res2 = self.position + tryvec/np.linalg.norm(tryvec)*self.w/2 - othervec/np.linalg.norm(othervec)*self.h/2
        res3 = self.position - tryvec/np.linalg.norm(tryvec)*self.w/2 + othervec/np.linalg.norm(othervec)*self.h/2
        res4 = self.position - tryvec/np.linalg.norm(tryvec)*self.w/2 - othervec/np.linalg.norm(othervec)*self.h/2
        return res1, res2, res3, res4, self.position


if __name__ == '__main__':
    width = 1920 # Can't remember resolution things
    height = 1080
    test = Screen(width, height)
    testrun = True
    clock = pg.time.Clock()
    surf = pg.display.get_surface()
    countx = 0
    county = 0
    timer = 0
    grav = 0
    wall = Wall(100, 100, np.array([0,0, 1]), np.array([1000, 1000, 0]))
    while testrun:
        pressed = pg.key.get_pressed()
        w = pressed[pg.K_w]
        d = pressed[pg.K_d]
        s = pressed[pg.K_s]
        a = pressed[pg.K_a]
        boost = pressed[pg.K_b]

        if boost:
            vel = timer
            if timer > 40:
                timer = 0
            timer += 1
        else:
            vel = 1

        if w:
            county += vel
        if s:
            county -= vel
        if d:
            countx -= vel
        if a:
            countx += vel

        grav += 2

        pg.time.delay(30)
        surf.fill((0,0,0))
        for j in wall.get_corners():
            pg.draw.circle(surf, (255, 255, 255, 255), (int(j[0]) - countx, int(j[1]) - county + grav), 10)
        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                test.close()
                testrun = False
