import pygame as pg
import random

class Screen(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        pg.init()
        pg.display.set_mode((self.w, self.h))

    def update(self):
        pass

    def close(self):
        pg.display.quit()

def test_draw_random_circle(surf):
    radius = 1
    x = random.randint(0, width- radius)
    y = random.randint(0, height- radius)
    pg.draw.circle(surf, (255,255,255,255), (x, y), radius)

def test_timer(surf, txt):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, 70)
    txt_surf = font.render(txt, True, (255, 255, 255, 255), (0,0,0,0))
    txt_rect = txt_surf.get_rect()
    txt_rect.midtop = (400, 40)
    surf.blit(txt_surf, txt_rect)

if __name__ == '__main__':
    width = 1920 # Can't remember resolution things
    height = 1080
    test = Screen(width, height)
    testrun = True
    clock = pg.time.Clock()
    surf = pg.display.get_surface()
    numstars = 0
    while testrun:
        time = clock.tick()
        test_timer(surf, 'Number of stars= ' + str(numstars))
        numstars += 1
        test_draw_random_circle(surf)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                test.close()
                testrun = False

        if numstars > 10**4:
            test.close()
            testrun = False
