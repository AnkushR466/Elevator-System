import time
Total_floors = 5
lift_l = 0
while(True):
    def up(current_f, destination_f):

        if destination_f >= current_f:
            time.sleep(1)
            print("G O I N G   U P")
            diff = destination_f - current_f
            for i in range(current_f + 1, destination_f + 1):
                print(i)
                time.sleep(1)

            if destination_f == current_f:
                print("You are on the same floor")
            else:
                time.sleep(1)
                print("You have reached on {} floor".format(destination_f))
                time.sleep(1)
                print("D o o r   A r e   O p e n i n g")
                time.sleep(2)
                lift_l = destination_f
                print("Lift current loacation is : {}".format(lift_l))

        elif destination_f <= current_f:
            time.sleep(1)
            print("G O I N G   D O W N")
            diff = abs(destination_f - current_f)
            # print("df ",destination_f)
            # print("cf ",current_f)
            for i in range(current_f ,  destination_f - 1, -1):
                print(i)
                time.sleep(1)

            if destination_f == current_f:
                print("You are on the same floor")
            else:
                time.sleep(1)
                print("You have reached on {} floor".format(destination_f))
                time.sleep(1)
                print("D o o r   A r e   O p e n i n g")
                time.sleep(2)
                lift_l = destination_f
                print("Lift current loacation is : {}".format(lift_l))


    if lift_l == 0:
        call_lift = input("Press 'u' button to go up : ")

    else:
        call_lift = input("press U to go up or D to go down : ")

    if call_lift == "u" or call_lift == "d":
        print("H E L L O   W E L C O M E   T O   T H E   L I F T")

        current_f = int(input("Enter your current floor "))

        if lift_l == current_f:
            print("Lift is on the same floor")
            time.sleep(2)
            print("D o o r   A r e   O p e n i n g")
        elif lift_l > current_f:
            print("Lift is comming down")
            time.sleep(2)
            print("D o o r   A r e   O p e n i n g")
        else:
            print("Lift is comming up")
            time.sleep(2)
            print("D o o r   A r e   O p e n i n g")

        time.sleep(2)
        destination_f = int(input("On which floor you want to go: "))
        time.sleep(2)
        print("D O O R S   A R E   C L O S I N G")
        if destination_f > 5:
                print("Sorry the building have 5 floors only")
        else:
                up(current_f, destination_f)
                lift_l = destination_f
