from pygame import *
font.init()

window = display.set_mode((1000, 600))
display.set_caption("Пинг-Понг")
font1 = font.Font(None, 35)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_image_x, player_image_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_image_x, player_image_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
        self.image_x = player_image_x
        self.image_y = player_image_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:     
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 590:       
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:     
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 590:       
            self.rect.y += self.speed


        

    
player1 = Player("platform.png", 970, 300, 5, 20, 100)
player2 = Player("platform.png", 10, 300, 5, 20, 100)
ball = GameSprite("ball.png", 500, 250, 4, 35, 35)
speed_x, speed_y = 6, 6
font_lose1 = font1.render("PLAYER 1 LOSE", True, (180, 0, 0))
font_lose2 = font1.render("PLAYER 2 LOSE", True, (180, 0, 0))


clock = time.Clock()
FPS = 60
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((255, 200, 200))
    player1.update1()
    player1.reset()
    player2.update2()
    player2.reset()
    
    


    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 570 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(font_lose1, (500, 250))
        if ball.rect.x > 1000:
            finish = True
            window.blit(font_lose2, (500, 250))
    ball.reset()
        

    display.update()
    clock.tick(FPS)