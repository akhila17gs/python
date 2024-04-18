command = ""
car_start=False

while True:
    command = input(">").lower()
    if command == "start":
        if car_start == False:
            print("Car Started...")
            car_start = True
        else:
            print("Car is already started...")
    elif command== "stop":
        if car_start == True:
            car_start = False
            print("Car Stopped...")
        else:
            print("Car is already stopped...")
    elif command == "help":
        print(''' 
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command=="quit":
        break
    else:
        print("Sorry,I don't understand that :( ")
