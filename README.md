# Elevator-System
## Introduction
This is a code for the real time working of a elevator [lift]. It is designed for the secnario where we have 1 user who is gonna use the elevator.
In this code we have some advance elevator functionalities like elivator assicstant, who will ask you by saying some greetings like "Welcome, How can I help you?" This code is written in python language.

So here, this code is devided into some parts:
* Calling elevator
* Decideing elevaor moving location like up or down
* For giving voice to program by ussing "Pyttsx3"

## Pre-Reuesties
To run this python file user should have installed:
* Python latest version
* "pyttsx3" Python Text To Speech library
* "pywin32"

And here we are good to go.

## More About Segements
### Speeking feature 
For this perticular feature. We used Python Text To Speach "PYTTSX3" library.

```
# importing library

import pyttsx3    
engine = pyttsx3.init()  
engine.say('Hello, how may I help you.')

# run and wait method, it processes the voice commands.

engine.runAndWait()
```


