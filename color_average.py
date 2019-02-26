#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:49:30 2018

@author: Huilin
"""

filename = "/Users/tian/Desktop/untitled folder/Log.txt"  # Name and path of the position file
f= open(filename, 'r') 
Line=f.readlines() 
x = []
y = []
for line in Line: 
	line = line.split(' ')
	x.append(line[0])
	y.append(line[1])

# turn the input from string to int
X = []
Y = []
for i in range(len(x)):
    X_temp = round(float(x[i]))
    X.append(X_temp)
    Y_temp = round(float(y[i]))
    Y.append(Y_temp)


from PIL import Image, ImageDraw
import numpy as np

im = Image.open('/Users/tian/Desktop/untitled folder/20180529-小吉浦(全段)_90m.jpg') # Name and path of your image
pix = im.load()
#print (im.size)  # width and hight of the image
#%%  Average
RGB = []
n = 3 # 平均的像素范围，改这个值！n=1是3x3，n=2是5x5平均
for i in range(n,len(X)):
    R = np.zeros(3)
    px = np.zeros(3)
    for p in range(-n,n+1): # X 
        py = np.zeros(3)
        s = np.zeros(3)
        for q in range(-n,n+1): # Y
            x2 = int(X[i]+p)
            y2 = int(Y[i]+q)
            PIX = pix[x2,y2]
            s[0] = s[0] + PIX[0]
            s[1] = s[1] + PIX[1]
            s[2] = s[2] + PIX[2]

        py[0] = round( s[0]/(2*n+1) )
        py[1] = round( s[1]/(2*n+1) )
        py[2] = round( s[2]/(2*n+1) )
        px[0] = px[0] + py[0]
        px[1] = px[1] + py[1]
        px[2] = px[2] + py[2]
    R[0] = int( round( px[0]/(2*n+1) ) ); R[0] = int(R[0])
    R[1] = int( round( px[1]/(2*n+1) ) ); R[1] = int(R[1])
    R[2] = int( round( px[2]/(2*n+1) ) ); R[2] = int(R[2])
    a = R[0]; b = R[1]; c = R[2]
    a = int(a); b = int(b); c= int(c)
    RGB_ = tuple((a,b,c))
    RGB.append(RGB_)

#%% Original selected pixels
RGB_original = []
for i in range(len(X)):
    RGB_original.append(pix[X[i],Y[i]])     # Get the RGB Value of the a pixel of an image

#%%
error = []
for i in range(len(RGB)):
    er = np.zeros(3)
    er[0] = abs( RGB[0] - RGB_original[0] )
    er[1] = abs( RGB[1] - RGB_original[1] )
    er[2] = abs( RGB[2] - RGB_original[2] )
    er2 = tuple((er[0],er[1],er[2]))
    error.append(er2)
    

#%%
a = 500 # length of your line
size = (len(Y),a)
im2 = Image.new(im.mode, size) # create a new image to show your lines
draw = ImageDraw.Draw(im2)
for i in range(len(X)-n):
    draw.line([(i, 0),(i,a)] , fill=RGB[i], width = 1)
im2.show()


    
    