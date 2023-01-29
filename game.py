import sys
import os
import random
from tkinter import *
import time
import pygame
from pygame.locals import *
import main

def gamesh():  
    FPS = 15
    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    CELLSIZE = 20
    assert WINDOWWIDTH % CELLSIZE == 0, "Ширина окна должна быть кратна размеру ячейки."
    assert WINDOWHEIGHT % CELLSIZE == 0, "Высота окна должна быть кратна размеру ячейки."
    CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
    CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

    #             R    G    B
    WHITE     = (255, 255, 255)
    BLACK     = (  0,   0,   0)
    RED       = (255,   0,   0)
    GREEN     = (  0, 255,   0)
    DARKGREEN = (  0, 155,   0)
    DARKGRAY  = ( 40,  40,  40)
    BGCOLOR = BLACK

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    HEAD = 0 # индекс головы червя

    def not_main():
        global FPSCLOCK, DISPLAYSURF, BASICFONT

        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Змейка')

        showStartScreen()
        while True:
            runGame()
            showGameOverScreen()


    def runGame():
        # Установится случайная начальная точка.
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        wormCoords = [{'x': startx,     'y': starty},
                      {'x': startx - 1, 'y': starty},
                      {'x': startx - 2, 'y': starty}]
        direction = RIGHT

        # Яблоко появится в случайном месте.
        apple = getRandomLocation()

        while True: # основной цикл игры
            for event in pygame.event.get(): # цикл обработки событий
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                        direction = UP
                    elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        terminate()

            # проверка -  не задел ли червь себя или край
            if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
                return # прогрыш
            for wormBody in wormCoords[1:]:
                if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                    return # проигрыш

            # проверить, не съел ли червь яблоко
            if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
                # не удаляется хвостовой сегмент червя
                apple = getRandomLocation() # положить где-нибудь новое яблоко
            else:
                del wormCoords[-1] # удалить хвостовой сегмент червя

            # переместь червяка, добавив сегмент в направлении его движения
            if direction == UP:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
            elif direction == DOWN:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
            elif direction == LEFT:
                newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
            elif direction == RIGHT:
                newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
            wormCoords.insert(0, newHead)
            DISPLAYSURF.fill(BGCOLOR)
            drawGrid()
            drawWorm(wormCoords)
            drawApple(apple)
            drawScore(len(wormCoords) - 3)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def drawPressKeyMsg():
        pressKeySurf = BASICFONT.render('Нажмите a чтобы играть.', True, DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINDOWWIDTH - 240, WINDOWHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


    def checkForKeyPress():
        if len(pygame.event.get(QUIT)) > 0:
            terminate()

        keyUpEvents = pygame.event.get(KEYUP)
        if len(keyUpEvents) == 0:
            return None
        if keyUpEvents[0].key == K_ESCAPE:
            terminate()
        return keyUpEvents[0].key


    def showStartScreen():
        titleFont = pygame.font.Font('freesansbold.ttf', 100)
        titleSurf1 = titleFont.render('Змейка!', True, WHITE, DARKGREEN)
        titleSurf2 = titleFont.render('Змейка!', True, GREEN)

        degrees1 = 0
        degrees2 = 0
        while True:
            DISPLAYSURF.fill(BGCOLOR)
            rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
            rotatedRect1 = rotatedSurf1.get_rect()
            rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
            DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

            rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
            rotatedRect2 = rotatedSurf2.get_rect()
            rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
            DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

            drawPressKeyMsg()

            if checkForKeyPress():
                pygame.event.get() # очистить очередь событий
                return
            pygame.display.update()
            FPSCLOCK.tick(FPS)
            degrees1 += 3 # поворот на 3 градуса каждый кадр
            degrees2 += 7 # поворот на 7 градуса каждый кадр


    def terminate():
        pygame.quit()
        sys.exit()


    def getRandomLocation():
        return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


    def showGameOverScreen():
        gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
        gameSurf = gameOverFont.render('Игра', True, WHITE)
        overSurf = gameOverFont.render('Окончена', True, WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (WINDOWWIDTH / 2, 10)
        overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 5 + 12)

        DISPLAYSURF.blit(gameSurf, gameRect)
        DISPLAYSURF.blit(overSurf, overRect)
        drawPressKeyMsg()
        pygame.display.update()
        pygame.time.wait(500)
        checkForKeyPress() # очистить все нажатия клавиш в очереди событий

        while True:
            if checkForKeyPress():
                pygame.event.get() # очистить очередь событий
                return

    def drawScore(score):
        scoreSurf = BASICFONT.render('Очков: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 120, 10)
        DISPLAYSURF.blit(scoreSurf, scoreRect)


    def drawWorm(wormCoords):
        for coord in wormCoords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


    def drawApple(coord):
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, RED, appleRect)


    def drawGrid():
        for x in range(0, WINDOWWIDTH, CELLSIZE): # нарисовать вертикальные линии
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
        for y in range(0, WINDOWHEIGHT, CELLSIZE): # нарисовать горизонтальные линии
            pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

    not_main()