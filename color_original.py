#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:49:04 2018

@author: Huilin
"""

from PIL import Image, ImageDraw

def readtext(filename):
    # read the position file
    f= open(filename, 'r') 
    Line=f.readlines() 
    x = []
    y = []
    for line in Line: 
    	line = line.split(' ')            # seperate the list with white space
    	x.append(line[0])                 # x coordinate
    	y.append(line[1])                 # y coordinate
    
    # turn the input from string to int
    X = []
    Y = []
    for i in range(len(x)):
        X_temp = round(float(x[i]))    
        X.append(X_temp)
        Y_temp = round(float(y[i]))
        Y.append(Y_temp)
    return X,Y


def drawImage(image,X,Y,length):
    a = length
    pix = im.load()                    # read the image
    RGB = []
    for i in range(len(X)):
        RGB.append(pix[X[i],Y[i]])     # Get the RGB Value of the a pixel of an image
    
    size = (len(Y),a)                  # set the new picture size
    im2 = Image.new(im.mode, size)     # create a new image to show your color
    draw = ImageDraw.Draw(im2)
    for i in range(len(X)):            #  draw the line from the first pixel, each color is 1 pixel in width
        draw.line([(i, 0),(i,a)] , fill=RGB[i], width = 1)
    im2.show()
    im2.save('color.JPG')              # file name of the output image
                                       # file path is the same as this program

#%%
filename = "/Users/tian/Desktop/untitled folder/Log.txt"  # Name and path of the position file
im = Image.open('/Users/tian/Desktop/untitled folder/20180529-小吉浦(全段)_90m.jpg') # Name and path of the image
a = 500                                # length of each line
X,Y = readtext(filename)
drawImage(im,X,Y,a)

