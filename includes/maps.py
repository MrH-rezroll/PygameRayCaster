#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Matthew Hodge
# Created Date: 12.19.21
# version ='1.0'
# ---------------------------------------------------------------------------
"""Contains the set of functions and data neccesary to represent a 2D environment"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import array as arr
import pygame

mapSprites = []
mapX = 8
mapY = 8
mapS = 64
mapW = arr.array('i', 
[
    4,4,4,1,1,2,1,1,
    4,0,0,1,0,0,0,1,
    4,0,0,1,0,0,0,1,
    1,1,3,1,0,0,0,2,
    1,0,0,0,0,0,0,1,
    2,0,0,0,0,1,0,2,
    1,0,0,0,0,0,0,1,
    1,1,2,1,2,1,1,1
])
mapC = arr.array('i', 
[
    9,9,9,5,5,5,5,5,
    9,9,9,5,5,5,5,5,
    9,9,9,5,5,5,5,5,
    5,5,5,5,5,5,5,5,
    5,5,5,5,5,5,5,5,
    5,5,5,5,5,5,5,5,
    5,5,5,5,5,5,5,5,
    5,5,5,5,5,5,5,5
])

def drawMap2D():
    """Draws the map int arrays as a 2D top down graphic.

    Parameters
    ----------
    none
    """
    global mapSprites
    global mapW
    mapSprites.clear()
    x = y = 0
    while y < mapY:
        x = 0
        while x < mapX:
            boxColor = (150,150,150)
            if mapW[y * mapX + x] == 1:
                boxColor = (0,0,255)
            elif mapW[y * mapX + x] == 2:
                boxColor = (0,255,0)
            elif mapW[y * mapX + x] == 3:
                boxColor = (255,0,0)
            else: boxColor = (0,0,200)
            tile = pygame.Surface((64, 64))
            tile.fill(boxColor)
            mapSprites.append((tile, (x * 64, y * 64)))
            x += 1
        y += 1