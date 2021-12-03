import pygame

PI = 3.1315926535
PI2 = PI/2
PI3 = 3*PI/2
M_PI = 3.14159265358979323846264338327950288
DR = 0.0174533
    
def degToRad(a):
    return a*M_PI/180.0
     
def fixAng(a):
    if a>359:
        a -= 360
    if a<0:
        a += 360
    return a  