from pygame import *
import os

WIDTH = 500
HEIGHT = 500
dir = os.path.dirname(os.path.realpath(__file__))
window = display.set_mode((WIDTH,HEIGHT))
background = transform.scale(image.load(os.path.join(dir,"assets","bg.png")), (WIDTH, HEIGHT))


class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed,size):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def reset(self):
        window.blit(self.image, self.rect)

class Paddle(GameSprite):
    def update(self,p):
        keys = key.get_pressed()
        if p == 2:
            if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= 10
            if keys[K_DOWN] and self.rect.y < HEIGHT-self.rect.height:
                self.rect.y += 10
        if p == 1:
            if keys[K_w] and self.rect.y > 0:
                self.rect.y -= 10
            if keys[K_s] and self.rect.y < HEIGHT-self.rect.height:
                self.rect.y += 10

class PaddleHit(GameSprite):
    def update(self,p):
        if p == 1:
            self.rect.x = paddle1.rect.x+paddle1.rect.width
            self.rect.y = paddle1.rect.y

        if p == 2:
            self.rect.x = paddle2.rect.x-15
            self.rect.y = paddle2.rect.y


class Ball(GameSprite):
    def __init__(self, img, x, y, speed, size):
        super().__init__(img, x, y, speed, size)
        self.toy = -self.speed
        self.tox = -self.speed

    def update(self):
        if self.rect.x <= 0-self.rect.width:
            self.tox = self.tox * -1
        if self.rect.y <= 0:
            self.toy = self.toy * -1
        if self.rect.x >= WIDTH:
            self.tox = self.tox * -1
        if self.rect.y >= HEIGHT:
            self.toy = self.toy * -1
        if self.rect.colliderect(paddlehit1.rect):
            self.tox = self.tox * -1
            self.rect.x += self.tox *2
        if self.rect.colliderect(paddlehit2.rect) and self.rect.x < 460:
            self.tox = self.tox * -1
            self.rect.x += self.tox *2

        self.rect.x += self.tox
        self.rect.y += self.toy

clock = time.Clock()
running = True
finish = False
FPS = 60

paddle1 = Paddle(os.path.join(dir,"assets","paddle1.png"),10,40,10,(35,105))
paddle2 = Paddle(os.path.join(dir,"assets","paddle2.png"),460,300,10,(35,105))
paddlehit1 = PaddleHit(os.path.join(dir,"assets","hitbox.png"),0,0,10,(15,105))
paddlehit2 = PaddleHit(os.path.join(dir,"assets","hitbox.png"),0,0,10,(15,105))
ball = Ball(os.path.join(dir,"assets","ball.png"),0,0,10,(64,64))

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    if finish != True:
        window.blit(background,(0,0))
        paddle1.update(1)
        paddle2.update(2)
        paddle1.reset()
        paddle2.reset()
        paddlehit1.update(1)
        paddlehit2.update(2)
        paddlehit1.reset()
        paddlehit2.reset()
        ball.update()
        ball.reset()

    display.update()
    clock.tick(FPS)
