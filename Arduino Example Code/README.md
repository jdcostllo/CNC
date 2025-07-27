# `TMC2208_Simple.ino`, TMC2208 Stepper Example Code

For this file, connect your stepper motor and stepper driver to the Y-Axis of the CNC Shield. Review the following wepages and images for clarification about how to connect the motor.

## TMC2208 Stepper Motor Driver 

This driver has a library within the Arduino IDE with provided examples. Version 0.2.5 is latest at time of 
this README. The INO file `TMC2208_Simple.ino`, which can be found in this directory, is a modified version of the example code from the TMC2208 Arduino Library.

## Stepper

If you're using the ANET stepper motors Jeff provided, take careful note 
of the wiring, which can be found online 
[here](https://shop.anet3d.com/products/42-stepper-motor). Alternatively, 
a PDF of the web page can be found in this directory at 
`Anet42StepperMotorfor3DPrinter.webp`.

If you follow a CNC shield tutorial, included in the next section of this 
README, ignore the example wiring and do your own verification that the 
motor coils are wired correctly to the stepper driver. Incorrect wiring 
will result in unhinged and deranged movement of the stepper motor.

## CNC Shield

Some basic code can be found 
[here](https://www.aranacorp.com/en/using-an-arduino-cnc-shield-v3/). I 
suggest using this code only to identify the pins on the CNC shield and 
inputting those pin values into your own script, built from the TMC2208 
examples.

A better hardware explanation of the CNC shield can be found 
[here](https://www.zyltech.com/arduino-cnc-shield-instructions/).
