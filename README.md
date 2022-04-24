# In-Car-Reg-Checker
 
This Reg Checker uses PyTesseract, PiCamera, and the UK Government's VES API - this piece of software is designed exclusively for UK Number plates.

A demonstration of the Reg Checker in action can be found here - https://youtu.be/OR75He9u3Ac

## How it works

1. The system will capture an image using PiCamera
2. The image will be processed to extract a number plate (finding a yellow rectangle)
3. The image is grayscaled so that it can be read by [PyTesseract](https://pypi.org/project/pytesseract/), an OCR Tool for python
4. The resultant text is scanned for a valid number plate (as defined by LLNN LLL, where L is letter and N is number).
5. The system then queries the UK Government VES API for information on this number plate.

## Dependencies
This project uses
- PiCamera
- PyTesseract OCR
- UK VES API (Vehicle Enquiry Service API)

## Issues

This program has many typical performance issues that come from image processing and OCR - one particular drawback is using PiCamera for this implementation, as typical FPS of a raspberry pi camera is very low. Work needs to be done to increase the performance of this system.

Another drawback of this system is reliability - at the moment, the system will take the first numberplate it reads as correct, when in reality there is a very good change it is incorrect, a majority polling system would assist in the accuracy of this system, although may increase the time to recognise each number plates.

## Potential Uses

This program was originally intended for mobile use on the road to detect untaxed vehicles, but this could very easily be extended to security implementations, such as tracking commonly seen vehicles to potentially flag stalkers.


