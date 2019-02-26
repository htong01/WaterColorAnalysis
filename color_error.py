#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:35:36 2018

@author: Huilin
"""

from PIL import Image
import numpy as np
from colormath.color_objects import LabColor, sRGBColor, AdobeRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976


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


im = Image.open('/Users/tian/Desktop/untitled folder/20180529-小吉浦(全段)_90m.jpg') # Name and path of your image
pix = im.load()
#%% RGB  Average
RGB = []
RGB_original = []
Lab = []; Lab_ori = []
error = []
n = 10 # 平均的像素范围，改这个值！n=1是3x3，n=2是5x5平均
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
#    RGB_ = [[[a,b,c]]]
#    RGB_color  = color.rgb2lab(RGB_)
#    
#    RGB_ = tuple((a,b,c))
#    RGB.append(RGB_)
#    RGB_original.append(pix[X[i],Y[i]])
    
    rgb = sRGBColor(a,b,c)
    lab = convert_color(rgb, LabColor,through_rgb_type=AdobeRGBColor)
    Lab.append(lab)
    
    RGB_original = pix[X[i],Y[i]]
    A = int(RGB_original[0])
    B = int(RGB_original[1])
    C = int(RGB_original[2])
    rgb_ori = sRGBColor(A,B,C)
    lab_ori = convert_color(rgb_ori, LabColor,through_rgb_type=AdobeRGBColor)
    Lab_ori.append(lab_ori)
    
    delta_e = delta_e_cie1976(lab, lab_ori)
    error.append(delta_e/100)

print( np.mean(error) )
print ( np.std(error))
