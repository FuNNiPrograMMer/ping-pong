#from
from pygame import*


#Флаги
game = True
speed_x = 10
speed_y = 10
finish = False
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
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
#окошко
win_width = 1000
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")
background = transform.scale(image.load('background.png'), (win_width, win_height))


#текст
font.init()
font = font.Font(None, 70)
lose1 = font.render('player 1 lose', True, (255, 0, 0))
lose2 = font.render('player 2 lose', True, (255, 0, 0))

#экземпляры
ball = GameSprite('ball.png', 472, 270, 5, 60, 60)
player1 = Player('p1.jpg', 30, 270, 30, 20, 150)
player2 = Player('p2.jpg', 950, 270, 30, 20, 150)


#цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    keys_pressed = key.get_pressed()
    if finish!=True:
        window.blit(background, (0, 0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y<0:
            speed_y*=-1


        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x*=-1
            speed_x+=3
            speed_y+=3

        if ball.rect.x<0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x>950:
            finish = True
            window.blit(lose2, (200, 200))


#отрисвка 
        ball.reset()
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()


#концовка
    display.update()
    time.delay(60)
