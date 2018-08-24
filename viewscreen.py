import pygame as pg
import random

class Screen(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        pg.init()
        #pg.display.init()
        pg.display.set_mode((self.w, self.h))

    def update(self):
        pass

    def close(self):
        pg.display.quit()

def test_draw_random_circle(surf):
    radius = 0
    x = random.randint(0, width- radius)
    y = random.randint(0, height- radius)
    pg.draw.circle(surf, (255,255,255,255), (x, y), radius)

def test_timer(surf, txt):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, 70)
    txt_surf = font.render(txt, True, (255, 255, 255, 255), (0,0,0,0))
    txt_rect = txt_surf.get_rect()
    txt_rect.midtop = (100, 40)
    surf.blit(txt_surf, txt_rect)

if __name__ == '__main__':
    width = 1920 # Can't remember resolution things
    height = 1080
    test = Screen(width, height)
    testrun = True
    clock = pg.time.Clock()
    surf = pg.display.get_surface()
    while testrun:
        elapsed = pg.time.get_ticks()
        time = clock.tick()
        test_timer(surf, str(elapsed))
        test_draw_random_circle(surf)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                test.close()
                testrun = False

        if elapsed > 10**4:
            test.close()
            testrun = False
