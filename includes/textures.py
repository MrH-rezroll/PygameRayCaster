import array as arr
import pygame

from pygame.locals import *
        
Shade1 = 0.7
Shade2 = 0.75
ColorSet1 = {
    0: [192,192,192],
    1: [160,160,164],
    2: [128,64,0],
    3: [160,96,64],
    4: [64,64,64],
    5: [64,96,128],
    6: [112,146,190],
    7: [64,160,64],
    8: [192,64,64],
    9: [0,0,0],
    10: [192*Shade1,192*Shade1,192*Shade1],
    11: [160*Shade1,160*Shade1,164*Shade1],
    12: [128*Shade1,64*Shade1,0],
    13: [160*Shade1,96*Shade1,64*Shade1],
    14: [64*Shade1,64*Shade1,64*Shade1],
    15: [64*Shade1,96*Shade1,128*Shade1],
    16: [112*Shade1,146*Shade1,190*Shade1],
    17: [64*Shade1,160*Shade1,64*Shade1],
    18: [192*Shade1,64*Shade1,64*Shade1],
    19: [0,0,0],
    20: [192*Shade2,192*Shade2,192*Shade2],
    21: [160*Shade2,160*Shade2,164*Shade2],
    22: [128*Shade2,64*Shade2,0],
    23: [160*Shade2,96*Shade2,64*Shade2],
    24: [64*Shade2,64*Shade2,64*Shade2],
    25: [64*Shade2,96*Shade2,128*Shade2],
    26: [112*Shade2,146*Shade2,190*Shade2],
    27: [64*Shade2,160*Shade2,64*Shade2],
    28: [192*Shade2,64*Shade2,64*Shade2],
    29: [0,0,0],
}
ColorBoxPixels = [0]*30
ColorBoxPixels2X = [0]*30
all_textures = arr.array('i', [              #all 32x32 textures
#Floor
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
4,4,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4,
5,5,5,6,6,6,6,6, 6,6,6,6,6,5,5,4, 5,5,6,6,6,6,6,6, 6,6,6,6,6,5,5,4,
5,5,6,4,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,0,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,5,6,6,6,6,6, 6,6,6,6,6,5,5,4, 5,5,6,6,6,6,6,6, 6,6,6,6,6,5,5,4, 
4,4,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
4,4,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4,
5,5,5,6,6,6,6,6, 6,6,6,6,6,5,5,4, 5,5,6,6,6,6,6,6, 6,6,6,6,6,5,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4,
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 5,6,6,6,6,6,6,6, 6,6,6,6,6,6,5,4, 
5,5,5,6,6,6,6,6, 6,6,6,6,6,5,5,4, 5,5,6,6,6,6,6,6, 6,6,6,6,6,4,5,4, 
4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,4, 
4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 
#Walls
2,2,3,2,2,2,2,4, 3,4,4,4,4,2,3,3, 3,2,4,4,4,4,2,3, 4,2,2,3,2,2,2,2,
3,3,3,3,3,3,3,3, 3,3,3,3,4,2,2,3, 3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,2,2,2,4,3,2,3, 2,3,3,3,3,4,2,2, 2,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,3,3,2,2,2,3,3, 3,3,3,3,3,4,4,4, 4,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
2,3,3,3,3,3,2,2, 2,3,3,2,2,2,4,4, 4,2,2,3,3,2,3,3, 2,2,3,3,3,3,2,2,
2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
3,2,1,1,1,1,1,1, 1,1,1,4,4,2,2,2, 2,2,2,4,1,1,1,1, 1,1,1,1,1,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,1,1,4,2,2,3, 3,2,3,1,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,2,3, 3,2,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,3, 3,2,3,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,2,3, 3,2,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,2,3, 3,2,3,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,2,3, 2,3,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,2, 3,2,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,2, 3,2,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,3, 3,3,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,3, 3,3,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,1,4,2,3,3, 3,3,2,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,0,1,4,2,3, 3,2,0,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,1,0, 0,0,0,0,0,1,4,2,3, 3,2,0,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,1,1,0,0, 0,0,0,0,0,1,4,2,3, 3,2,0,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,0,1,4,2,3, 3,2,0,0,0,0,0, 0,0,0,0,0,1,2,3,
3,2,1,0,0,0,0,0, 0,0,0,0,0,4,4,2,3, 3,2,0,0,0,0,0, 0,0,0,0,0,1,2,3,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,2,2, 2,2,4,4,4,4,4, 4,4,4,4,4,4,4,4,
5,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,4,4, 4,4,5,5,5,5,5, 5,5,5,5,5,5,5,5,
6,6,6,5,6,6,5,5, 5,6,6,6,5,6,6,6,6, 6,6,6,6,6,5,5, 5,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,6, 6,6,6,6,6,6,5, 6,6,6,6,1,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,6, 6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,6, 6,6,6,5,6,6,6,6,6, 6,6,6,6,5,6,6, 6,6,6,6,6,6,5,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,6, 6,6,6,5,6,6,5, 6,6,6,6,6,6,6,6,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
#Window
2,2,3,2,2,2,2,4, 3,4,4,4,4,2,3,3, 3,2,4,4,4,4,2,3, 4,2,2,3,2,2,2,2,
3,3,3,3,3,3,3,3, 3,3,3,3,4,2,2,3, 3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,2,2,2,4,3,2,3, 2,3,3,3,3,4,2,2, 2,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,3,3,2,2,2,3,3, 3,3,3,3,3,4,4,4, 4,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
2,3,3,3,3,3,2,2, 2,3,3,2,2,2,4,4, 4,2,2,3,3,2,3,3, 2,2,3,3,3,3,2,2,
2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
3,1,4,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,1,1,3,
3,1,4,2,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,2,0,0,3,
3,1,4,2,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,2,0,0,3,
3,0,1,4,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,1,0,0,3,
3,0,0,1,4,2,2,2, 2,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,2, 3,3,2,1,0,0,0,3,
3,0,0,0,1,2,3,3, 2,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,2, 3,3,2,1,0,0,0,3,
3,0,1,0,1,2,3,3, 2,9,9,9,9,9,9,9, 9,9,9,8,8,9,9,2, 3,3,2,0,1,0,0,3,
3,0,0,0,1,2,3,3, 2,9,9,9,9,9,9,9, 9,9,9,7,8,9,9,2, 3,3,2,0,0,0,0,3,
3,0,0,0,1,2,3,3, 2,9,9,9,9,9,9,9, 9,8,7,9,9,9,9,2, 3,3,2,0,0,0,0,3,
3,0,0,0,1,2,3,3, 2,9,9,9,9,9,9,9, 9,9,7,9,9,9,9,2, 3,3,2,0,0,0,0,3,
3,1,0,0,1,1,2,3, 3,2,9,9,9,9,9,9, 9,9,9,7,9,9,2,3, 3,2,1,0,0,1,0,3,
3,0,1,0,0,1,2,3, 3,2,9,9,9,9,9,9, 9,4,6,4,4,9,2,3, 3,2,0,0,0,0,1,3,
3,0,1,0,0,1,2,2, 3,2,9,9,9,9,9,9, 9,4,4,4,4,9,2,3, 2,2,0,0,0,0,0,3,
3,1,0,0,0,1,2,2, 3,2,9,9,9,9,9,9, 9,9,4,4,9,9,2,3, 2,2,0,0,0,0,0,3,
3,0,1,4,3,3,3,3, 2,2,3,3,3,2,3,3, 3,3,3,3,2,3,2,2, 3,3,3,3,0,0,0,3,
3,0,1,1,4,2,4,2, 2,4,4,4,4,4,4,4, 4,4,4,2,4,4,2,2, 4,2,2,1,0,0,0,3,
3,0,0,0,1,4,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,1,0,1,1,0,3,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,2,2, 2,2,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
5,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,4,5,5,5,5,5,5, 5,5,5,5,5,5,5,5,
6,6,6,5,6,6,5,5, 5,6,6,5,6,6,6,6, 6,6,6,6,6,6,5,5, 5,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,5, 6,6,6,6,1,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,6, 6,6,5,6,6,6,6,6, 6,6,6,6,6,5,6,6, 6,6,6,6,6,6,5,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,5,5,6,6,5, 6,6,6,6,6,6,6,6,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
#Door
3,3,3,3,3,3,3,3, 3,3,3,3,4,2,3,3, 3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,3,3,3,3,3,3,3, 3,3,3,3,4,2,2,3, 3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,3,3,3,3,3,3,3, 3,3,3,3,3,4,2,2, 2,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
3,3,3,3,3,3,3,3, 3,3,3,3,3,4,4,4, 4,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3,
2,2,2,2,2,2,2,2, 2,2,2,2,2,2,4,4, 4,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2,
2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,   
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,     
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,    
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,    
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,   
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,4,3,4, 4,3,4,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,4,4,4,4,3,4, 4,3,4,4,4,4,3,3, 3,3,3,3,6,5,5,4,   
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,    
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,    
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,   
4,5,5,6,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,6,5,5,4, 
4,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,  
4,5,5,6,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,6,5,5,4,     
6,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,4,   
4,5,5,6,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,6,5,5,6,   
6,5,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,6,   
6,5,5,6,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,6,5,6,4,  
4,6,5,6,3,3,3,3, 3,3,3,3,3,3,3,4, 4,3,3,3,3,3,3,3, 3,3,3,3,6,5,5,6,   
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
#Rail
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,    
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,    
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,   
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,     
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,    
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,    
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,   
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,  
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,    
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,   
9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9, 9,9,9,9,9,9,9,9,
6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,6,  
5,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,5,    
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,  
9,9,9,2,2,2,3,9, 9,9,9,9,9,9,2,2, 2,3,9,9,9,9,9,9, 9,2,2,2,3,9,9,9,   
9,9,9,2,2,2,3,9, 9,9,9,9,9,9,2,2, 2,3,9,9,9,9,9,9, 9,2,2,2,3,9,9,9, 

4,4,4,2,2,2,3,4, 4,4,4,4,4,4,2,2, 2,3,4,4,4,4,4,4, 4,2,2,2,3,4,4,4,  
5,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4, 4,4,5,5,5,5,5,5, 5,5,5,5,5,5,5,5,     
6,6,6,5,6,6,5,5, 5,6,6,5,6,6,6,6, 6,6,6,6,6,6,5,5, 5,6,6,6,6,6,6,6,   
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,5, 6,6,6,6,1,6,6,6,   
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6,   
6,6,6,6,6,6,6,6, 6,6,5,6,6,6,6,6, 6,6,6,6,6,5,6,6, 6,6,6,6,6,6,5,6,  
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,6, 6,6,6,5,5,6,6,5, 6,6,6,6,6,6,6,6,   
4,5,5,5,5,4,5,4, 4,5,5,4,5,5,5,5, 5,5,5,5,4,5,4,4, 4,4,5,5,4,5,5,5,
#Ceiling
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,    
0,0,0,0,0,0,0,0, 0,0,1,1,4,2,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,    
0,0,0,0,0,0,0,0, 0,0,1,1,4,2,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,2,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,2,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,0,0,0,0,0, 0,0,1,1,4,2,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,     
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,1,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,1,1,0,0,0,0,    
1,1,1,1,1,1,1,1, 1,1,1,1,4,3,3,3, 3,3,4,1,1,1,1,1, 1,1,1,1,1,1,1,1,    
1,1,1,1,1,1,1,1, 1,1,1,1,4,3,3,3, 2,3,4,1,1,1,1,1, 1,1,1,1,1,1,1,1,   
4,4,4,4,4,4,4,4, 4,4,4,4,4,3,3,3, 2,3,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,  
2,2,2,2,2,2,2,2, 2,2,2,2,4,3,3,3, 2,3,4,2,2,2,2,2, 2,2,2,2,2,2,2,2,    
2,2,2,2,2,2,2,2, 3,3,2,2,4,3,3,3, 2,3,4,2,2,2,2,2, 2,2,3,3,3,3,2,2,  
2,2,2,3,3,3,3,3, 2,2,2,2,4,3,3,3, 2,3,4,2,2,2,2,2, 2,2,2,2,2,2,3,3,
2,2,2,2,2,2,2,2, 2,2,2,2,4,3,3,3, 3,3,4,2,2,2,2,2, 2,2,2,2,2,2,2,2,   
2,2,2,2,2,2,2,2, 2,2,2,2,4,3,3,3, 3,3,4,2,2,2,2,2, 2,2,2,2,2,2,2,2,   
4,4,4,4,4,4,4,4, 4,4,4,4,4,3,3,2, 3,3,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,    
1,1,1,1,1,1,1,1, 1,1,1,1,4,3,3,2, 3,3,4,1,1,1,1,1, 1,1,1,1,1,1,1,1,    
1,1,1,1,1,1,1,1, 1,1,1,1,4,3,3,2, 3,3,4,1,1,1,1,1, 1,1,1,1,1,1,1,1,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,2, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,2, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0, 

0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,     
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,2,3, 3,3,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,2,3, 3,2,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,1,0,0,0,0, 0,0,1,1,4,3,2,3, 3,2,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,2,3, 3,2,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,  
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,2,3, 3,2,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,   
0,0,0,0,0,0,0,0, 0,0,1,1,4,3,3,3, 3,2,4,1,1,0,0,0, 0,0,0,0,0,0,0,0,
])
"""

3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,4,2,3,3,
3,2,4,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,4,2,2,3,
2,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,4,2,2,
4,4,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, 3,3,3,3,3,4,4,4,
4,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,4,4,
2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2, 2,2,2,2,2,2,2,2,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
2,2,2,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1,1,1,4,1,1,1,1, 1,1,1,4,4,2,2,2,
3,2,3,0,0,0,0,0, 0,0,1,0,0,0,0,0, 0,0,0,1,0,0,0,0, 0,0,0,1,4,2,2,3,
3,2,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,2,3,
3,2,3,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,3,
3,2,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,2,3,
3,2,3,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,2,3,
2,3,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,2,3,
3,2,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,2,
3,2,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,2,
3,3,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,3,
3,3,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,3,
3,3,2,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,1,4,2,3,3,
3,2,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,1,4,2,3,
3,2,0,0,0,0,0,0, 0,0,0,0,0,1,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,1,4,2,3,
3,2,0,0,0,0,0,0, 0,0,0,1,1,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,1,4,2,3,
3,2,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,1,4,2,3,
3,2,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,4,4,2,3,
2,2,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,2,2,
4,4,5,5,5,5,5,5, 5,5,5,5,5,5,5,5, 5,5,5,5,5,5,5,5, 5,5,5,5,5,5,4,4,
6,6,6,5,6,6,5,5, 5,6,6,5,6,6,5,5, 6,5,5,6,6,6,5,5, 5,6,6,5,6,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,5, 6,6,5,6,6,6,6,5, 6,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,5, 6,6,5,6,6,6,6,5, 6,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,6, 6,6,5,6,6,6,6,6, 5,6,6,6,6,5,6,6, 6,6,6,6,6,6,6,6,
6,6,6,6,6,6,6,5, 6,6,6,6,6,6,6,5, 6,6,5,5,5,6,6,5, 6,6,6,6,6,6,6,6,
4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4, 4,4,4,4,4,4,4,4,
"""

def updateColorBoxes(sizeX, sizeY, colorBoxSet):
    c = 0
    while c < 30:
        cbSurface = pygame.Surface((sizeX,sizeY))
        cbSurface.fill(ColorSet1.get(c))
        cbSurface.convert()
        if colorBoxSet == 1:
            ColorBoxPixels[c] = cbSurface
        if colorBoxSet == 2:
            ColorBoxPixels2X[c] = cbSurface
        c+=1