import math as mth
import pygame

from includes.utils import degToRad
from includes.utils import fixAng
from pygame.locals import *
from math import cos
from math import sin

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() 
        self.moveSpeed = 100
        self.surf = pygame.Surface((32, 32))
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect(center = (256, 256))
        self.px = 320
        self.py = 320
        self.pa = 90
        self.pdx = cos(degToRad(self.pa))
        self.pdy = -sin(degToRad(self.pa))

    def move(self, deltaTime, mapX, mapW):

        updateMap = False
        xo = 0
        if self.pdx < 0:
            xo = -20
        else:
            xo = 20
        yo = 0
        if self.pdy < 0:
            yo = -20
        else:
            yo = 20
        ipx = (int)(self.px/64.0)
        ipx_add_xo=(int)((self.px+xo)/64.0)
        ipx_sub_xo=(int)((self.px-xo)/64.0)
        ipy= (int)(self.py/64.0)
        ipy_add_yo=(int)((self.py+yo)/64.0)
        ipy_sub_yo=(int)((self.py-yo)/64.0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LSHIFT]:
            if pressed_keys[K_LEFT]:
                xo = 20
                yo = 20
                if degToRad(self.pa) < 2.0 or degToRad(self.pa) > 6.0:
                    xo = -20
                    yo = -20
                ipx = (int)(self.px/64.0)
                ipx_add_xo=(int)((self.px+xo)/64.0)
                ipx_sub_xo=(int)((self.px-xo)/64.0)
                ipy= (int)(self.py/64.0)
                ipy_add_yo=(int)((self.py+yo)/64.0)
                ipy_sub_yo=(int)((self.py-yo)/64.0)
                if mapW[(int)(ipy*mapX + ipx_add_xo)]==0:
                    self.px -= cos(degToRad(fixAng(self.pa - 90))) * self.moveSpeed * deltaTime
                if mapW[(int)(ipy_add_yo*mapX + ipx) ]==0:
                    self.py -= -sin(degToRad(fixAng(self.pa - 90))) * self.moveSpeed * deltaTime
            if pressed_keys[K_RIGHT]:
                xo = -20
                yo = -20
                if degToRad(self.pa) < 2.0 or degToRad(self.pa) > 6.0:
                    xo = 20
                    yo = 20
                ipx = (int)(self.px/64.0)
                ipx_add_xo=(int)((self.px+xo)/64.0)
                ipx_sub_xo=(int)((self.px-xo)/64.0)
                ipy= (int)(self.py/64.0)
                ipy_add_yo=(int)((self.py+yo)/64.0)
                ipy_sub_yo=(int)((self.py-yo)/64.0)
                if mapW[(int)(ipy*mapX + ipx_add_xo)]==0:
                    self.px += cos(degToRad(fixAng(self.pa - 90))) * self.moveSpeed * deltaTime
                if mapW[(int)(ipy_add_yo*mapX + ipx) ]==0:
                    self.py += -sin(degToRad(fixAng(self.pa - 90))) * self.moveSpeed * deltaTime
        else:
            xo = 0
            if self.pdx < 0:
                xo = -20
            else:
                xo = 20
            yo = 0
            if self.pdy < 0:
                yo = -20
            else:
                yo = 20
            ipx = (int)(self.px/64.0)
            ipx_add_xo=(int)((self.px+xo)/64.0)
            ipx_sub_xo=(int)((self.px-xo)/64.0)
            ipy= (int)(self.py/64.0)
            ipy_add_yo=(int)((self.py+yo)/64.0)
            ipy_sub_yo=(int)((self.py-yo)/64.0)
            if pressed_keys[K_LEFT]:
                self.pa+=self.moveSpeed*deltaTime
                self.pa = fixAng(self.pa)
                self.pdx = cos(degToRad(self.pa))
                self.pdy = -sin(degToRad(self.pa))
                    
            if pressed_keys[K_RIGHT]:
                self.pa-=self.moveSpeed*deltaTime
                self.pa = fixAng(self.pa)
                self.pdx = cos(degToRad(self.pa))
                self.pdy = -sin(degToRad(self.pa))


        xo = 0
        if self.pdx < 0:
            xo = -20
        else:
            xo = 20
        yo = 0
        if self.pdy < 0:
            yo = -20
        else:
            yo = 20
        ipx = (int)(self.px/64.0)
        ipx_add_xo=(int)((self.px+xo)/64.0)
        ipx_sub_xo=(int)((self.px-xo)/64.0)
        ipy= (int)(self.py/64.0)
        ipy_add_yo=(int)((self.py+yo)/64.0)
        ipy_sub_yo=(int)((self.py-yo)/64.0)
        if pressed_keys[K_UP]:
            if mapW[(int)(ipy*mapX + ipx_add_xo)]==0:
                self.px += self.pdx * self.moveSpeed * deltaTime
            if mapW[(int)(ipy_add_yo*mapX + ipx) ]==0:
                self.py +=self.pdy *self. moveSpeed * deltaTime
        if pressed_keys[K_DOWN]:
            if mapW[(int)(ipy*mapX + ipx_sub_xo)]==0:
                self.px -= self.pdx * self.moveSpeed * deltaTime
            if mapW[(int)(ipy_sub_yo*mapX + ipx)]==0:
                self.py -= self.pdy * self.moveSpeed * deltaTime

        if pressed_keys[K_e]:
            xo=0 
            if self.pdx<0:
                xo=-25 
            else: 
                xo=25

            yo=0 
            if self.pdy<0: 
                yo=-25
            else: 
                yo=25
            ipx = (int)(self.px/64.0)
            ipx_add_xo=(int)((self.px+xo)/64.0)
            ipy= (int)(self.py/64.0)
            ipy_add_yo=(int)((self.py+yo)/64.0)

            if mapW[(int)(ipy_add_yo*mapX+ipx_add_xo)]==3: 
                mapW[(int)(ipy_add_yo*mapX+ipx_add_xo)]=0
                updateMap = True

        self.rect.center = (self.px, self.py)
        return updateMap