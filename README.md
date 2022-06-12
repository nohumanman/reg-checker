# reg-checker
 
This uses PyTesseract, PiCamera, and the UK Government's VES API - this piece of software is designed for UK Number plates.

This project can be used to
- detect commonly spotted vehicles
- detect vehicles with no MOT
- detect vehicles with no Tax
- allow for data analysis of vehicle 'spots'

A demonstration of the Reg Checker in action can be found here - https://youtu.be/OR75He9u3Ac

## How it works

1. Program continously checks video feed to detect number plates.
2. Number plate is detected.
3. Number Plate Spotting is added to database of all viewed number plates
4. Database is searched for occurences of this number plate (designed to detect stalking)
5. VES API is queried and results are added to Number Plate Spotting.

This data is all viewable in a dashboard.
There is the option to be emailed with alerts of vehicles spotted with no MOT, no Tax, or who have been spotted an unusual amount of times.

## UML Diagram



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


