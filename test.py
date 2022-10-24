import pygame
import sys



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 360

white = (255, 255, 255)
black = (100, 100, 100)

pygame.init()
pygame.display.set_caption("North Korea")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

white_rects = []
for i in range(20):       
    rect = pygame.draw.rect(screen, 'white', [i * 70, SCREEN_HEIGHT - 300, 69, 300], 0, 2)
    white_rects.append(rect)
black_rects = []
for j in range(19):
    if j != 2 and j != 6 and j != 9 and j != 13 and j != 16: # and j != 20 and j != 23 and j != 27:
        rect = pygame.draw.rect(screen, 'black', [j * 70 + 44.5, SCREEN_HEIGHT - 300, 50, 150], 0, 2)
        black_rects.append(rect)
    else:
        pass

clock = pygame.time.Clock()
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)

    for i in range(20):
        a = white_rects.pop(0)
        white_rects.append(a)
        pygame.draw.rect(screen, white, a)
    for j in range(19):
        b = black_rects.pop(0)
        black_rects.append(b)
        pygame.draw.rect(screen, (0, 0, 0), b)
    
    pygame.display.update()




