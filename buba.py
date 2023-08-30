import pygame
import math
import random
from pygame.locals import *
#import main
import os
import sys
def buba_prog():
    pygame.init( )
     
    WIDTH= 500
     
    HEIGHT= 500
    screen= pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("arial", 10, bold=True)
    WHITE = (255,255,255) 
    BLACK = (0,0,0)
     
    r1 = 80
    x_space = 10
    y_space = 12
    columns = int(WIDTH / x_space)
    rows = int(HEIGHT / y_space)
    r2 = 150#rotation angles x- and 2-axis
    K2 = 5000
    K1 = WIDTH * K2 * 3/(8*(r1+r2))
    A = 1
    B = 1
    x_offset= WIDTH / 2
    y_offset = HEIGHT / 2
    chars = [".", ",", "-", "~", ":", ";", "=", "!", "*", "#", "$", "@"]
    def draw(x, y, char):
        text = font.render(char, True, WHITE)
        screen.blit(text, (x, y))
     
    while True:
     
        screen.fill((BLACK)) #erase previous donut
     
        cosB, sinB = math.cos(B), math.sin(B)
     
        cosA, sinA = math.cos(A), math.sin(A)
        output = []
        for i in range(rows):
            coll = []
            for j in range(columns):
                coll.append(" ")
            output.append(coll)
        zbuffer = []
        for i in range(rows):
            col2 = []
            for j in range(columns):
                col2.append(0)
            zbuffer.append(col2)
     
        for T in range(0, 628, 12):
     
            cosT, sinT = math.cos(T/100), math.sin(T/100) 
            x2 = r2 + r1 * cosT
            y2 = r1 * sinT
     
     
     
     
     
            for P in range(0, 628, 4):
     
                cosP, sinP = math.cos(P/100), math.sin(P/100)
                
                x = x2 * (cosB * cosP + sinA * sinB * sinP) - y2 * cosA * sinB 
                y = x2 * (cosP * sinB - cosB * sinA * sinP) + y2 * cosA * cosB 
                z = K2 + r1 * sinA * sinT + cosA* sinP * x2
                
                ooz = 1 / z
                
                
                xp = math.floor(-x * K1 * ooz) 
                yp = math.floor(-y * K1 * ooz)
                
                
                l = cosP * cosT * sinB - cosA * cosT * sinP - sinA * sinT + cosB * (cosA * sinT - cosT * sinA * sinP)
                
                
                if l > -0.8:
                
                    l = abs(l)
                    yc = int((yp + y_offset)/y_space)
                    xc = int((xp + x_offset)/x_space)
                    if ooz > zbuffer[yc][xc]:
                        zbuffer[yc][xc] = ooz
                        L = round(l*8)
                        output[yc][xc] = chars[L]
     
     
     
        for a in range(rows):
            for b in range(columns):
                draw(b*x_space, a*y_space, output[a][b])
     
        if (A > 6.283 and A < 6.2831):
            A = 0
            B = 0
     
        else:
            A += 0.06
            B += 0.04
     
        for event in pygame.event.get(): 
     
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()