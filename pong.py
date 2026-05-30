from pygame import *

window = display.set_mode((500,500))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed,size):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect)

class Paddle(GameSprite):
    def update(self,p,keys):
        if p == 1: