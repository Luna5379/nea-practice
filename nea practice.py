import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1500,750))
pygame.display.set_caption('tutorial')
clock = pygame.time.Clock()
testFont = pygame.font.Font('comfortaa\Comfortaa-Regular.ttf', 200)

pinkFlower = pygame.image.load('pngtree-pink-flower-cute-png-image_13522448.png').convert_alpha()
poppet = pygame.image.load('2ad587cfed9859310a7cee225dcca1f3306b91f4r1-471-431v2_hq.jpg').convert()
text = testFont.render('I miss Hannah', True, 'red')
bg = pygame.Surface((1500,750))

puzzlerSurface = pygame.image.load('Puzzling_puzzling_puzzler.webp').convert_alpha()
puzzlerX = 1100

spooky = pygame.image.load('Spooky_Spoon.webp').convert_alpha()
spookyRect = spooky.get_rect(topleft = (80, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bg, (0,0))
    screen.blit(pinkFlower, (0,0))
    screen.blit(poppet, (0,350))
    screen.blit(text, (0, 0))
    puzzlerX -= 10
    if puzzlerX <= -400:
        puzzlerX = 1300
    screen.blit(puzzlerSurface, (puzzlerX,250))
    screen.blit(spooky, spookyRect)
    pygame.display.update()
    clock.tick(60)