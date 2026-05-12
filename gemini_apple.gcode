(Segmented Apple Logo - 50x50mm - Servo Pen Lift)
(Origin: Top Left, Offset to 50, -50)
(Pen Lift: M03 S50, Pen Lower: M03 S25)
(Pause: 100ms)

G21 ; Set units to mm
G90 ; Absolute positioning
M03 S50 ; Ensure pen is up
G4 P0.1 ; Wait 100ms

(--- Initial Move to Offset ---)
G0 X50.00 Y-50.00

(--- Part 1: Main Body Outline ---)
G0 X91.00 Y-62.00
M03 S25 ; Pen Down
G4 P0.1 ; Wait 100ms
G1 X80.00 Y-60.00 F800
G1 X72.00 Y-63.00
G1 X64.00 Y-60.00
G1 X54.00 Y-63.00
G1 X50.00 Y-75.00
G1 X52.00 Y-95.00
G1 X62.00 Y-112.00
G1 X72.00 Y-110.00
G1 X84.00 Y-112.00
G1 X94.00 Y-95.00
G1 X91.00 Y-87.00
G1 X88.00 Y-82.00
G1 X93.00 Y-72.00
G1 X91.00 Y-62.00
M03 S50 ; Pen Up
G4 P0.1 ; Wait 100ms

(--- Part 2: The Leaf ---)
G0 X72.00 Y-61.00
M03 S25 ; Pen Down
G4 P0.1
G1 X76.00 Y-53.00
G1 X84.00 Y-50.00
G1 X80.00 Y-57.00
G1 X72.00 Y-61.00
M03 S50 ; Pen Up
G4 P0.1

(--- Part 3: Horizontal Dividers ---)
(Divider 1)
G0 X51.00 Y-72.00
M03 S25
G4 P0.1
G1 X93.00 Y-72.00
M03 S50
G4 P0.1

(Divider 2)
G0 X50.00 Y-80.00
M03 S25
G4 P0.1
G1 X89.00 Y-80.00
M03 S50
G4 P0.1

(Divider 3)
G0 X50.00 Y-88.00
M03 S25
G4 P0.1
G1 X91.00 Y-88.00
M03 S50
G4 P0.1

(Divider 4)
G0 X53.00 Y-96.00
M03 S25
G4 P0.1
G1 X94.00 Y-96.00
M03 S50
G4 P0.1

(Divider 5)
G0 X57.00 Y-104.00
M03 S25
G4 P0.1
G1 X89.00 Y-104.00
M03 S50
G4 P0.1

(--- Finish ---)
G0 X50 Y-50 ; Return to starting offset
M05 ; Spindle/Servo Stop