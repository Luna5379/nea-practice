import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('player_walk_1.png').convert_alpha()
        player2 = pygame.image.load('player_walk_2.png').convert_alpha()
        self.players = [player1, player2]
        self.playeridx = 0
        self.player3 = pygame.image.load('jump.png').convert_alpha()
        self.image = self.players[self.playeridx]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jumpSound = pygame.mixer.Sound('jump.mp3')
        self.jumpSound.set_volume(0.3)

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jumpSound.play()

    def applyGravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def state(self):
        if self.rect.bottom < 300:
            self.image = self.player3
        else:
            self.playeridx += 0.1
            if self.playeridx >= len(self.players):
                self.playeridx = 0
            self.image = self.players[int(self.playeridx)]

    def update(self):
        self.playerInput()
        self.applyGravity()
        self.state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly1 = pygame.image.load('Fly1.png').convert_alpha()
            fly2 = pygame.image.load('Fly2.png').convert_alpha()
            self.frames = [fly1, fly2]
            ypos = 210
        else:
            snail1 = pygame.image.load('snail1.png').convert_alpha()
            snail2 = pygame.image.load('snail2.png').convert_alpha()
            self.frames = [snail1, snail2]
            ypos = 300
        self.animationidx = 0
        self.image = self.frames[self.animationidx]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), ypos))
    
    def state(self):
        self.animationidx += 0.1
        if self.animationidx >= len(self.frames):
            self.animationidx = 0            
        self.image = self.frames[int(self.animationidx)]

    def update(self):
        self.state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def score(startTime, active):
        time = int((pygame.time.get_ticks() - startTime)/1000)
        scoreText = testFont.render(str(time), False, (64,64,64))
        scoreRect = scoreText.get_rect(midtop = (50,50))
        pygame.draw.rect(screen, '#c0e8ec', scoreRect)
        screen.blit(scoreText, scoreRect)
        return time

def spriteCollide():
    if pygame.sprite.spritecollide(playersp.sprite,obstacles,False):
        obstacles.empty()
        return False
    else:
        return True

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('tutorial')
clock = pygame.time.Clock()
testFont = pygame.font.Font('Pixeltype.ttf', 50)
active = False
startTime = 0
final = 0
music = pygame.mixer.Sound('music.wav')
music.set_volume(0.1)
music.play(loops = -1)

playersp = pygame.sprite.GroupSingle()
playersp.add(Player())
obstacles = pygame.sprite.Group()

sky = pygame.image.load('Sky.png').convert_alpha()
ground = pygame.image.load('ground.png').convert()
text = testFont.render('My practice game for learning pygame!', True, (64,64,64))
textRect = text.get_rect(midtop = (400,50))
bg = pygame.Surface((800,400))
title = testFont.render('Practice Game', False, (111,196, 169))
titleRect = title.get_rect(center = (400,50))
playerO = pygame.image.load('player_stand.png').convert_alpha()
playerO = pygame.transform.rotozoom(playerO, 0, 2)
playerORect = playerO.get_rect(center = (400,200))

obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if active:
            if event.type == obstacleTimer:
                obstacles.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = True
                    startTime = pygame.time.get_ticks()

    if active:
        screen.blit(bg, (0,0))
        screen.blit(sky, (0,0))
        screen.blit(ground, (0,300))
        pygame.draw.rect(screen, '#c0e8ec', textRect)
        screen.blit(text, textRect)
        playersp.draw(screen)
        playersp.update()
        obstacles.draw(screen)
        obstacles.update()
        active = spriteCollide()
        final = score(startTime, active)
    else:
        screen.fill((94,129,162))
        screen.blit(playerO, playerORect)
        screen.blit(title, titleRect)
        if final == 0:
            instruct = testFont.render('Press space to start', False, (111, 196, 169))
            instRect = instruct.get_rect(center = (400,350))
            screen.blit(instruct, instRect)
        else:
            finalScore = testFont.render('SCORE: '+ str(final), False, (111, 196, 169))
            finalRect = finalScore.get_rect(center = (400,350))
            screen.blit(finalScore, finalRect)
    pygame.display.update()
    clock.tick(60)
