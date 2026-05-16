# Code converts images into GCode
# Created by Jeff Costello (github: jdcostllo)
# Python 3.14.5

#################################
### IMPORTS
#################################

# pip install -r requirements.txt
from PIL import Image # pip install pillow
import numpy as np # pip install numpy

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

# Target Image Height
imageHeight = 100

# Drawing Density
    # How many circles, Xs, or other drawn elements per real-world mm
    # Will be used to scale computer image to real-world coords
drawDensity = 2 # [Element per mm]

#################################
### LOAD AND CONFIGURE IMAGE
#################################

# Open the image and convert to 'L' mode (grayscale)
img = Image.open('weenie.png').convert('L')

# Modifies 'img' in-place to fit within 300x300 while keeping aspect ratio
img.thumbnail((imageHeight*drawDensity, imageHeight*drawDensity), resample=Image.Resampling.LANCZOS)

img = img.point(lambda x: (x // 64) * 65)

# print(f"Width: {img.width}")
# print(f"Height: {img.height}")

# Method B: Convert to NumPy array for bulk reading
pixel_matrix = np.array(img)
# print(pixel_matrix)

#################################
### LOAD IMAGE
#################################

img.show()