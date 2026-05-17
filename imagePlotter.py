# Code converts images into GCode
# Created by Jeff Costello (github: jdcostllo)
# Python 3.14.5

#################################
### IMPORTS
#################################

# pip install -r requirements.txt
from PIL import Image # pip install pillow
import numpy as np # pip install numpy

import os
os.system("cls") if os.name == "nt" else os.system("clear")

import time

#################################
### MACHINE PARAMETERS
#################################

# Raise Pen to Travel
    # Spindle command actuates the servo.
    # Add small pause (G04) to ensure pen moves fully before XY motion.
gRaise = f"M03S50\nG04P0.1"

# Lower Pen to Write
    # Spindle command actuates the servo.
    # Add small pause (G04) to ensure pen moves fully before XY motion.
gLower = f"M03S25G04P01"

# Pen "Off"
    # Turn off servo.
gStop = f"M5"

#################################
### DRAWING PARAMETERS
#################################

# XY Origin of the Machine
    # Uses this real-world cooriante to the place the iamge origin
drawOrigin = np.array([0,0]) 

# Image Origin (XY) As:
    # Top-Left: -1,1
    # Top-Right: 1,1
    # Center: 0,0
    # ... et cetera.
imageOrigin = np.array([-1,1])

# Target Image Height in [mm]
plotHeight = 100 # [mm]

# Drawing Density
    # How many circles, Xs, or other drawn elements per real-world mm
    # Will be used to scale computer image to real-world coords
drawDensity = 2 # [Drawn elements per mm]

#################################
### LOAD AND CONFIGURE IMAGE
#################################

# Open the image and convert to 'L' mode (grayscale)
img = Image.open('weenie.png').convert('L')

# Modifies 'img' in-place to fit within 300x300 while keeping aspect ratio
img.thumbnail((plotHeight*drawDensity, plotHeight*drawDensity), resample=Image.Resampling.LANCZOS)

# Convert the image to four levels of grey
    # Floor divide the 8-bit color (256 [0-255]) greyscale values into 2-bit (4 [0-3]) greyscale values
    # Multiply by 85 to re-scale 2-bit color onto 8-bit color scale.
# img = img.point(lambda pt: (pt // 64) * 85)
img = img.point(lambda pt: (pt // 64))

print(f"New image width: {img.width}")
print(f"New image height: {img.height}")

# Method B: Convert to NumPy array for bulk reading
pixel_matrix = np.array(img)

#################################
### MAKE PLOTTER COORDS
#################################

# plotHeight ALREADY DEFINED ABOVE
plotWidth = img.width / drawDensity

print(f"Creating plot coords for {plotWidth}, {plotHeight} [mm width x mm height].")

print(f"Image Origin: {imageOrigin[1]}")

imageOriginX = imageOrigin[0]
imageOriginY = imageOrigin[1]

numElmX = int(plotHeight * drawDensity) # Number of drawn elements in the X direction
numElmY = int(plotWidth * drawDensity)

xAxis = np.linspace(0, plotWidth * (imageOriginX * -1), numElmX-1)
yAxis = np.linspace(0, plotHeight * (imageOriginY * -1), numElmY-1)

plotCoords = np.meshgrid(xAxis, yAxis) # tuple
plotCoords = np.dstack(plotCoords)

print(f"image shape: {pixel_matrix.shape}")
print(f"plotCoords shape: {plotCoords.shape}")

# exit()

xInd = 0
yInd = 0
for row in plotCoords: # contains all x coordiantes for one y coordinate
    for coord in row: # get a single xy coordinate
        # print(coord)
        greyscaleValue = pixel_matrix[yInd,xInd]
        print(f"X Index: {xInd}, Y Index: {yInd}, Greyscale Value: {greyscaleValue}")
        time.sleep(0.1)
        yInd += 1
    xInd += 1