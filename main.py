#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Matthew Hodge
# Created Date: 12.19.21
# version ='1.0'
# ---------------------------------------------------------------------------
"""The entry point to the 2D raycast Pygame example program"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import math as mth, pygame, os, sys, array as arr

from pygame.locals import *
from includes.maps import *
from includes.player import Player
from includes.textures import *
from includes.raycaster2D import *
from threading import Thread

flags = RESIZABLE
pygame.init()
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
VEC2 = pygame.math.Vector2  # 2 for two dimensional
HEIGHT = 480
WIDTH = 640
ACC = 0.5
FRIC = -0.12
FPS = 60
getTicksLastFrame = 0
t = pygame.time.get_ticks()
# deltaTime in seconds.
deltaTime = (t - getTicksLastFrame) / 1000.0
getTicksLastFrame = t
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT), flags, 24)
gameWindowSurface = pygame.Surface([480, 320]).convert()
mapViewerSurface = pygame.Surface([512,512]).convert()
mapWindowSurface = pygame.Surface([1024,1024]).convert()
mapTilesSurface = pygame.Surface([1024,1024]).convert()
mapOutlineSurface = pygame.Surface((130, 130)).convert()
mapOutlineSurface.fill((200,200,200))
displaysurface.fill((20,20,20))
displaysurface.blit(mapOutlineSurface, (255, 335))
pygame.display.set_caption("PyCaster")
updateColorBoxes(8,1,1)
updateColorBoxes(4,1,2)

datac = pygame.image.load("tmpBG.jpg").convert()
datac_rect = datac.get_rect()
background = pygame.Surface((1000, 333)).convert()
background.blit(datac, datac_rect)


datac = pygame.image.load("tmpTitle.jpg").convert()
datac_rect = datac.get_rect()
titleScreen = pygame.Surface((WIDTH, HEIGHT)).convert()
titleScreen.blit(datac, datac_rect)
displaysurface.blit(titleScreen, (0,0))

datac = pygame.image.load("tmpLose.jpg").convert()
datac_rect = datac.get_rect()
loseScreen = pygame.Surface((WIDTH, HEIGHT)).convert()
loseScreen.blit(datac, datac_rect)

datac = pygame.image.load("tmpWin.jpg").convert()
datac_rect = datac.get_rect()
winScreen = pygame.Surface((WIDTH, HEIGHT)).convert()
winScreen.blit(datac, datac_rect)

gameState = 0

player = Player()
drawMap2D()
mapTilesSurface.blits(mapSprites)

def distance(ax, ay, bx, by, ang):
    return mth.cos(degToRad(ang))*(bx-ax)-mth.sin(degToRad(ang))*(by-ay)

gameRunning = 1
def renderUpdate(gameWindowSurface,mapViewerSurface,mapWindowSurface,displaysurface,gameRunning):
    while gameRunning == 1:
        if gameState == 0:
            displaysurface.blit(titleScreen, (0, 0))
            pygame.display.flip()
        elif gameState == 1:
            gameWindowSurface.blit(background, (0,0))
            mapViewerSurface.fill((0,0,0))
            mapWindowSurface.blit(mapTilesSurface, mapTilesSurface.get_rect())
            mapWindowSurface.blit(player.surf, player.rect)
            drawRays2D(player.pa, player.px, player.py, mapX, mapY, mapW, mapC, mapS, mapWindowSurface, gameWindowSurface)
            mapViewerSurface.blit(mapWindowSurface, (256 - (int)(player.px), 256 - (int)(player.py)), mapViewerSurface.get_rect().inflate(-1, -1))
            mapViewerSurface.scroll(64 - 512 - (int)(player.px), 64 - 512 - (int)(player.py))
            displaysurface.blit(gameWindowSurface, (80, 0))
            displaysurface.blit(pygame.transform.scale(mapViewerSurface, ((128, 128))), (256, 336))
            pygame.display.flip()
        elif gameState == 2:
            displaysurface.blit(loseScreen, (0, 0))
            pygame.display.flip()
        elif gameState == 3:
            displaysurface.blit(winScreen, (0, 0))
            pygame.display.flip()

def logicUpdate():
    global player
    global gameState
    pressed_keys = pygame.key.get_pressed()
    if player.move(deltaTime, mapX, mapW):
        drawMap2D()
        mapTilesSurface.blits(mapSprites)
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_1]:
        setQualityMode(1)
    elif pressed_keys[pygame.K_2]:
        setQualityMode(2)
    elif pressed_keys[pygame.K_3]:
        setQualityMode(3)

    if pressed_keys[pygame.K_k]:
        gameState = 2
    if pressed_keys[pygame.K_l]:
        gameState = 3

def stateManagement():
    global getTicksLastFrame
    global deltaTime
    global gameRunning
    global gameState


    if gameState == 1:
        logicUpdate()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if gameState == 0:  
                if event.key == pygame.K_RETURN:
                    gameState = 1
            elif gameState == 2:  
                if event.key == pygame.K_RETURN:
                    gameState = 0
            elif gameState == 3:  
                if event.key == pygame.K_RETURN:
                    gameState = 0
        if event.type == QUIT:
            gameState = 0
            gameRunning = 0
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    FramePerSec.tick(FPS)

if __name__ == '__main__':
    rT = Thread(target=renderUpdate, args=(gameWindowSurface,mapViewerSurface,mapWindowSurface,displaysurface,gameRunning))
    rT.start()
    while gameRunning == 1:    
        stateManagement()
    pygame.quit()
    sys.exit()