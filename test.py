import pygame
import sys
import keyboard
from pygame import mixer
import pianotes as nt


SCREEN_WIDTH = 1470
SCREEN_HEIGHT = 720

pygame.init()
pygame.display.set_caption("장군님 축지법 쓰신다")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mixer.set_num_channels(50)

white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)
yellow = (255, 255, 0)

white_sound = []
black_sound = []

white_note = nt.white_notes
black_note = nt.black_notes

for i in range(len(white_note)):
    white_sound.append(mixer.Sound(f'assets\\notes\\{white_note[i]}.wav'))

for i in range(len(black_note)):
    black_sound.append(mixer.Sound(f'assets\\notes\\{black_note[i]}.wav'))


maxSpeed = 500

white_rects = []
for i in range(22):       
    rect = pygame.draw.rect(screen, 'white', [i * 70, SCREEN_HEIGHT - 300, 69, 300], 0, 2)
    white_rects.append(rect)
black_rects = []
for j in range(21):
    if j != 2 and j != 6 and j != 9 and j != 13 and j != 16 and j != 20:# and j != 23 and j != 27:
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
    screen.fill(gray)

    
    
    for i in range(22):
        drawWhite = white_rects.pop(0)
        white_rects.append(drawWhite)
        pygame.draw.rect(screen, white, drawWhite)

        if keyboard.is_pressed("z"):
            if i == 0:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("x"):
            if i == 1:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("c"):
            if i == 2:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("v"):
            if i == 3:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("b"):
            if i == 4:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("n"):
            if i == 5:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("m"):
            if i == 6:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed(",") or keyboard.is_pressed("q"):
            if i == 7:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("w"):
            if i == 8:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("e"):
            if i == 9:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("r"):
            if i == 10:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("t"):
            if i == 11:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("y"):
            if i == 12:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("u"):
            if i == 13:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("i"):
            if i == 14:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("o"):
            if i == 15:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)
        elif keyboard.is_pressed("p"):
            if i == 16:
                pygame.draw.rect(screen, yellow, drawWhite)
                white_sound[i].play(0, maxSpeed)


        else:
            pass


    for j in range(21):
        drawBlack = black_rects.pop(0)
        black_rects.append(drawBlack)
        pygame.draw.rect(screen, black, drawBlack)

        if keyboard.is_pressed("s"):
            if j == 0:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("d"):
            if j == 1:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("g"):
            if j == 3:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("h"):
            if j == 4:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("j"):
            if j == 5:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("2"):
            if j == 7:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("3"):
            if j == 8:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("5"):
            if j == 10:
                pygame.draw.rect(screen, yellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
            

        else:
            pass


    pygame.display.update()




