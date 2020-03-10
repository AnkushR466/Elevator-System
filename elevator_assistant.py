# Importing time library for using sleep function
import time

import pyttsx3    
engine = pyttsx3.init()  
engine.say('Hello, how may I help you.') 
  
# run and wait method, it processes the voice commands.  
engine.runAndWait() 


Total_floors = 5
lift_l = 0

# Using while loop for taking continous input form user
while(True):
    def up(current_f, destination_f):

# For going up ...
        if destination_f >= current_f:
            time.sleep(1)
            print("G O I N G   U P")
            engine.say('Going Up')
            engine.runAndWait()
            diff = destination_f - current_f
            for i in range(current_f + 1, destination_f + 1):
                print(i)
                time.sleep(1)

            if destination_f == current_f:
                print("You are on the same floor")
                engine.say('You are on the same floor')
                engine.runAndWait()
            else:
                time.sleep(1)
                print("You have reached on {} floor".format(destination_f))
                engine.say('You have reached on your destination')
                engine.runAndWait()
                time.sleep(1)
                print("D o o r s   A r e   O p e n i n g")
                engine.say('Doors are opening')
                engine.runAndWait()
                time.sleep(2)
                lift_l = destination_f
                print("Lift current loacation is : {}".format(lift_l))

# For going down ...
        elif destination_f <= current_f:
            time.sleep(1)
            print("G O I N G   D O W N")
            engine.say('Going Down')
            engine.runAndWait()
            diff = abs(destination_f - current_f)

            for i in range(current_f - 1 ,  destination_f - 1, -1):
                print(i)
                time.sleep(1)

            if destination_f == current_f:
                print("You are on the same floor")
                engine.say('You are on the same floor')
                engine.runAndWait()
            else:
                time.sleep(1)
                print("You have reached on {} floor".format(destination_f))
                engine.say('You have reached on your destination')
                engine.runAndWait()
                time.sleep(1)
                print("D o o r s   A r e   O p e n i n g")
                engine.say('Doors are opening')
                engine.runAndWait()
                time.sleep(2)
                lift_l = destination_f
                print("Lift current loacation is : {}".format(lift_l))


# If we are on 0th floor we can only see up button else both
    if lift_l == 0:
        call_lift = input("Press 'u' button to go up : ")        

    else:
        call_lift = input("press U to go up or D to go down : ")

# Calling lift on any floor
    if call_lift == "u" or call_lift == "d":
        print("H E L L O   W E L C O M E   T O   T H E   L I F T")
        engine.say('Welcome to the lift')
        engine.runAndWait()

        current_f = int(input("Enter your current floor "))

        if lift_l == current_f:
            print("Lift is on the same floor")
            engine.say('Lift is on the same floor')
            engine.runAndWait()
            time.sleep(2)
            print("D o o r s  A r e   O p e n i n g")
            engine.say('Doors are opening')
            engine.runAndWait()
        elif lift_l > current_f:
            print("Lift is comming down")
            engine.say('Wait Please, While lift is Comming Down')
            engine.runAndWait()
            time.sleep(2)
            print("D o o r   A r e   O p e n i n g")
            engine.say('Doors are opening')
            engine.runAndWait()
        else:
            print("Lift is comming up")
            engine.say('Wait Please, While lift is Comming up')
            engine.runAndWait()
            time.sleep(2)
            print("D o o r s   A r e   O p e n i n g")
            engine.say('Doors are opening')
            engine.runAndWait()

        time.sleep(2)
        destination_f = int(input("On which floor you want to go: "))
        time.sleep(2)
        print("D O O R S   A R E   C L O S I N G")
        engine.say('Doors are closing')
        engine.runAndWait()
        if destination_f > 5:
                print("Sorry the building have 5 floors only")
                engine.say('Sorry, the building have only 5 floors')
                engine.runAndWait()
        else:
                up(current_f, destination_f)
                lift_l = destination_f
                
