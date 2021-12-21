#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Matthew Hodge
# Created Date: 12.19.21
# version ='1.0'
# ---------------------------------------------------------------------------
""" Contains the set of functions and data that draw a FPS perspective from a 2D map"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from math import cos
from math import sin
from math import tan
from includes.utils import degToRad
from includes.utils import fixAng
from pygame.draw import line
from includes.textures import *

angleOffset = 1
rayWidth = 8
rayCount = 62
quality = 1
qualityMode = 1
updateQuality = 0
blit_list = []
prevPlayerX = 0
prevPlayerY = 0
prevPlayerPA = 0
currentSurfaceColorBoxes = ColorBoxPixels

def setQualityMode(newMode):
    global qualityMode, quality, updateQuality
    qualityMode = newMode
    if qualityMode == 1:
        quality = 1
        updateQuality = 1
        adjustQuality()
        updateQuality = 0
    elif qualityMode == 2:
        quality = 2
        updateQuality = 1
        adjustQuality()
        updateQuality = 0


def setRaycasterQualityLevels(newQuality):
    global quality
    global currentSurfaceColorBoxes
    if newQuality == 1:
        quality = 1
        currentSurfaceColorBoxes = ColorBoxPixels
    elif newQuality == 2:
        quality = 2
        currentSurfaceColorBoxes = ColorBoxPixels2X

def adjustQuality():
    global qualityMode
    global quality
    global angleOffset
    global rayWidth
    global rayCount
    if quality == 1:
        angleOffset = 1
        rayWidth = 8
        rayCount = 62
    elif quality == 2:
        angleOffset = 0.5
        rayWidth = 4
        rayCount = 122

def drawRays2D(pa, px, py, mapX, mapY, mapW, mapC, mapS, mapWindowSurface, gameWindowSurface):
    global prevPlayerPA, prevPlayerX, prevPlayerY, quality, updateQuality
    
    if qualityMode == 3:
        if pa == prevPlayerPA and px == prevPlayerX and py == prevPlayerY:
            if quality != 2:
                quality = 2
                updateQuality = 1
        elif quality != 1:
            quality = 1
            updateQuality = 1
    
        if updateQuality == 1:
            adjustQuality()
            updateQuality = 0

    prevPlayerPA = pa
    prevPlayerX = px
    prevPlayerY = py
    
    r = mx = my = mp = dof = 0
    vx = vy = rx = ry = xo = yo = disV = disH = 0.0
    ra = fixAng(pa + 30)
    blit_list.clear()
    while r < rayCount:
        vmt = 0
        hmt = 0
        #Vertical Line Check
        dof = 0
        disV=1000000
        thisTan = tan(degToRad(ra))
        if cos(degToRad(ra))> 0.001:
            rx = (((int)(px)>>6)<<6)+64
            ry = (px-rx) * thisTan+py
            xo = 64
            yo = -xo*thisTan
        elif cos(degToRad(ra))<-0.001:
            rx = (((int)(px)>>6)<<6) -0.0001
            ry = (px-rx) * thisTan+py
            xo = -64
            yo = -xo*thisTan
        else:
            rx = px
            ry = py
            dof = 8
        while dof < 8:
            mx = int(rx / 64)
            my = int(ry / 64)
            mp = my * mapX + mx
            if mp < mapX*mapY and mp > 0 and mapW[mp] > 0:
                vx = rx
                vy = ry
                vmt=mapW[mp]-1
                disV=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py)
                dof=8
            else:
                rx+=xo
                ry+=yo
                dof+=1
        #Horizontal Line Check
        dof = 0
        disH=1000000 
        if thisTan != 0:
            thisTan = 1.0/thisTan
        if sin(degToRad(ra)) > 0.001:
            ry = (((int)(py)>>6)<<6) -0.0001
            rx = (py-ry) * thisTan+px
            yo = -64
            xo = -yo*thisTan
        if sin(degToRad(ra)) < -0.001:
            ry = (((int)(py)>>6)<<6)+64
            rx = (py-ry) * thisTan+px
            yo = 64
            xo = -yo*thisTan
        if sin(degToRad(ra)) >= -0.001 and sin(degToRad(ra)) <= 0.001:
            rx = px
            ry = py
            dof = 8
        while dof < 8:
            mx = int(rx / 64)
            my = int(ry / 64)
            mp = my * mapX + mx
            if mp < mapX*mapY and mp > 0 and mapW[mp] > 0:
                hmt=mapW[mp]-1
                disH=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py)
                dof=8
            else:
                rx+=xo
                ry+=yo
                dof+=1
        shade = 0
        if disV<disH:
            shade = 10
            hmt = vmt
            rx = vx
            ry = vy
            disH = disV
        
        ca=fixAng(pa-ra)
        
        disH=disH*cos(degToRad(ca))
        lineH=(mapS*320)/disH
        ty_step=32.0/lineH
        ty_off = 0
        if lineH > 320:
            ty_off=(lineH-320)/2.0
            lineH = 320
        lineOff = 160-lineH/2
        if r == 0 or r == rayCount-1:
            line(mapWindowSurface, (255, 255, 255), (px, py), ((px+rx)/2, (py+ry)/2), 8)
        
        #Draw Walls
        y = 0
        ty = ty_off*ty_step+hmt*32
        tx = 0
        if shade == 0:
            tx = (int)(rx/2.0)%32
            if ra > 180:
                tx = 31-tx
        else:
            tx = (int)(ry/2.0)%32
            if ra > 90 and ra < 270:
                tx = 31-tx
        lastYPos = lineOff
        ty += 32
        while y < lineH:
            i = (int)(ty) * 32 + (int)(tx)
            if i >= len(all_textures):
                i = len(all_textures) - 1
            if i < 0:
                i = 0
            c=all_textures[i]
            y += 1
            if c != 9:
                blit_list.append((currentSurfaceColorBoxes[c+shade], (r*rayWidth, lastYPos)))
            lastYPos = y + lineOff
            ty += ty_step
        
        #Draw Floor
        y = lineOff+lineH
        lastXPos = r*rayWidth
        shade = 0
        while y < 320:
            dy = y-(320/2.0)
            deg=degToRad(ra) 
            raFix = cos(degToRad(fixAng(pa-ra)))
            tx = px/2 + cos(deg)*158*32/dy/raFix
            ty = py/2 - sin(deg)*158*32/dy/raFix
            mp=mapW[(int)(ty/32.0)*mapX+(int)(tx/32.0)]*32*32
            c=all_textures[((int)(ty)&31)*32 + ((int)(tx)&31)+mp]
            if c != 9:
                blit_list.append((currentSurfaceColorBoxes[c+shade], (lastXPos, lastYPos)))
            
            #Draw Ceiling
            shade = 20
            mp=mapC[(int)(ty/32.0)*mapX+(int)(tx/32.0)]
            if mp < 9:
                c=all_textures[((int)(ty)&31)*32 + ((int)(tx)&31)+(mp*1024)]
                if c != 9:
                    blit_list.append((currentSurfaceColorBoxes[c+shade], (lastXPos, 320-lastYPos)))
            lastYPos = y
            lastXPos = r*rayWidth
            y+=1
        r += 1
        ra=fixAng(ra-angleOffset)  
    gameWindowSurface.blits(blit_list)
    """
    bI = 0
    while bI < len(blit_list):
        gameWindowSurface.blit(currentSurfaceColorBoxes[blit_list[bI][0]], blit_list[bI][1])
        bI += 1
    """