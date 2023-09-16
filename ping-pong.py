#from
from pygame import*


#Флаги
game = True


#класс спрайты
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, playerw, playerh):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (playerw, playerh))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 920:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 920:
            self.rect.y += self.speed
#окошко
win_width = 1000
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")
background = transform.scale(image.load('pingpong.png'), (win_width, win_height))


#цикл
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    

#концовка
    display.update()
    time.delay(60)
