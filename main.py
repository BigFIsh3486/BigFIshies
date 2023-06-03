# importing os and system
import os, sys

# importing pygame 
import pygame as pg

# testting

fps = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.image.load('graphics\downR.png')
        self.rect = self.image.get_rect(center = (620,410))

    def draw(self,surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pass

# defining main function
def main():

    # initialisisng pygame
    pg.init()
    
    # setting caption and logo (optional)
    pg.display.set_caption('Imagine')

    # creating screen surface
    screen = pg.display.set_mode((1240,820))

    player = Player()
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        player.draw(screen)
        pg.display.update()
        fps.tick(60)

if __name__ == '__main__':
    main()