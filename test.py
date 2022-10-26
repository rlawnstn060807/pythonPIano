# 모듈 불러오기
from re import X
import pygame
import sys
import keyboard
from pygame import mixer
import pianotes as nt
import littlestar as ls


SCREEN_WIDTH = 1470
SCREEN_HEIGHT = 720

pygame.init()
pygame.display.set_caption("장군님 축지법 쓰신다")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mixer.set_num_channels(50)



maxSpeed = 1000





white = (255, 255, 255) # 흰 타일 색깔
gray = (100, 100, 100) # 배경 색깔
black = (0, 0, 0) # 검은 타일 색깔
yellow = (255, 255, 0) # 흰 타일 눌렸을 때 색깔
moreYellow = (212, 255, 0) # 검은 타일 눌렸을 때 색깔
green = (0, 255, 0) # 임시

white_sound = [] # 흰 타일의 소리 리스트
black_sound = [] # 검은 타일의 소리 리스트

song1 = [] # 작은별

white_note = nt.white_notes
black_note = nt.black_notes

littlestar = ls.littleStar





for i in range(len(white_note)):
    white_sound.append(mixer.Sound(f'assets\\notes\\{white_note[i]}.wav'))

for i in range(len(black_note)):
    black_sound.append(mixer.Sound(f'assets\\notes\\{black_note[i]}.wav'))


for i in range(len(littlestar)):
    song1.append(mixer.Sound(f'assets\\notes\\{littlestar[i]}.wav'))


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
'''
class Tiles:
    def __init__(self, size):
        self.size = size
'''    



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
                pygame.draw.rect(screen, yellow , drawWhite)
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


    for j in range(15):
        drawBlack = black_rects.pop(0)
        black_rects.append(drawBlack)
        pygame.draw.rect(screen, black, drawBlack)

        if keyboard.is_pressed("s"):
            if j == 0:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("d"):
            if j == 1:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("g"):
            if j == 2:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("h"):
            if j == 3:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("j"):
            if j == 4:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("2"):
            if j == 5:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("3"):
            if j == 6:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("5"):
            if j == 7:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("6"):
            if j == 8:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("7"):
            if j == 9:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("9"):
            if j == 10:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)
        elif keyboard.is_pressed("0"):
            if j == 11:
                pygame.draw.rect(screen, moreYellow, drawBlack)
                black_sound[j].play(0, maxSpeed)    


        else:
            pass
        

    

    '''
    if keyboard.is_pressed("a"):
        
        for i in range(len(littlestar)):
            song1[i].play(0, maxSpeed)
            if i == 6 or i == 13 or i == 20 or i == 27 or i == 34: 
                pygame.time.delay(1000)
            else:
                pygame.time.delay(500)
    '''



    checkline = pygame.draw.rect(screen, 'black', [0 , 300, 1470, 10])
    pygame.draw.rect(screen, black, checkline)
    
    pygame.display.update()




