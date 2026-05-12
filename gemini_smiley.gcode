(Smiley Face 50mm x 50mm)
(G-Code for GRBL Pen Plotter)

G21 (Metric units)
G90 (Absolute positioning)
F800 (Platting speed)

(--- Start Sequence: Pen Up ---)
M03 S50
G04 P0.1

(--- Path 1: Outline Circle ---)
(Center: 25, -25 | Radius: 25)
G0 X25 Y0 (Move to top center)
M03 S25 (Pen Down)
G04 P0.1
G2 X25 Y0 I0 J-25 (Clockwise full circle)
M03 S50 (Pen Up)
G04 P0.1

(--- Path 2: Left Eye ---)
(Center: 15, -15 | Small circle)
G0 X15 Y-12
M03 S25 (Pen Down)
G04 P0.1
G2 X15 Y-12 I0 J-3
M03 S50 (Pen Up)
G04 P0.1

(--- Path 3: Right Eye ---)
(Center: 35, -15 | Small circle)
G0 X35 Y-12
M03 S25 (Pen Down)
G04 P0.1
G2 X35 Y-12 I0 J-3
M03 S50 (Pen Up)
G04 P0.1

(--- Path 4: The Smile ---)
(Arc from 10, -30 to 40, -30)
G0 X10 Y-30
M03 S25 (Pen Down)
G04 P0.1
G2 X40 Y-30 I15 J0 (Arc with center offset)
M03 S50 (Pen Up)
G04 P0.1

(--- End: Return to Home ---)
G0 X0 Y0
M05 (Spindle/Laser Off)