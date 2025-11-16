from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y >= win_height - 80:
            self.rect.y += self.speed
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y >= win_height - 80:
            self.rect.y += self.speed

background = (200, 255, 255)
win_height = 500
win_width = 600
display.set_caption("Пинг-понг")
window = display.set_mode((win_width, win_height))
window.fill(background)
clock = time.Clock()

game = True
finish = False
fps = 60

rocket1 = Player('rocket_pung-pong1.png', 30, 200, 50, 150, 4)
rocket2 = Player('rocket_pung-pong2.png', 520, 200, 50, 150, 4)
ball = GameSprite('ball_tennis.png', 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.fill(background)
        rocket1.update_l()
        rocket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        rocket1.reset()
        rocket2.reset()
        ball.reset()


    display.update()
    clock.tick(fps)