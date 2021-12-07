import time
import random
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox


def play_game(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} the right number? enter: H for high or L for low or C for correct ").lower()

        if feedback == "h":
            high = high - 1
        elif feedback == "l":
            low += 1
    else:
        print("Correct")


name = input("What is you name befor we begin? ")
print(f"You are so Welcome{name}lets's begin ")
adventure = input(
    "Welcome to an adventure let's begin...type left or right to see some adventures workout(left/right) ").lower()
if adventure == "right":
    work = input("You are on the road side, type walk to have a walk or turn to turn back to go back (walk/turn) ").lower()

    if work == "walk":
        walk_time = input("For how long would you wanna walk? ")

        if walk_time.isdigit():
            walk_time = int(walk_time)

        else:
            print("You need to input a number next time pls ")

        for seconds in range(walk_time, 0, -1):
            print(seconds)
            time.sleep(1)
            print("You walking for over", seconds, "seconds now")
        walk = input(("Would you walk again sire(yes/no) ")).lower()
        if walk == "yes":
            while True:
                walk_again = input("For how long do you wanna walk? ")
                if walk_again.isdigit():
                    walk_again = int(walk_again)
                    for seconds in range(walk_again, 0, -1):
                        print(seconds)
                        time.sleep(1)
                        print("You are rewalking in", seconds, "seconds")
                        quit()
                else:
                    print("Please enter a number")
                    continue
        elif walk == "no":
            rest_time = input("You really need to rest... would like to sit(yes/no)").lower()
            if rest_time == "yes":
                game_time = input("Grab a chair and sit bro... would you like to play a game sire/ma(yes/no)").lower()
                if game_time == "yes":
                    type_of_game = input("What type of game would you like to play...(guessing game/ paper game/computer guess )? ").lower()
                    if type_of_game == "guessing game":
                        rand_range = input("Enter a number? ")
                        if rand_range.isdigit():
                            rand_range = int(rand_range)
                            if rand_range <= 0:
                                print("Please enter a higher number nextime... ")
                        else:
                            print("Please enter a number nextime ")
                            quit()
                        random_number = random.randint(0, rand_range)
                        guess = 0
                        while True:
                            guess += 1
                            user_input = input("Enter a guessing number? ")

                            if user_input.isdigit():
                                user_input = int(user_input)
                            else:
                                print("Please enter a number...")
                                continue
                            if user_input == random_number:
                                print("You won! ")
                                break
                            elif user_input > random_number:
                                print("You are above the guessing number ")
                            elif user_input < random_number:
                                print("Number is below the guessing number ")
                            else:
                                print(f"You guessed in {guess} times ")
                    elif type_of_game == "paper game":
                        user_wins = 0
                        computer_wins = 0
                        options = ["paper", "rock", "scissors"]
                        while True:
                            user_input = input("enter rock/paper/scissors or q to quit ").lower()
                            if user_input == "q":
                                print("You won ", user_wins, "Times")
                                print("Computer ", computer_wins, "Times")
                                quit()
                            if user_input not in options:
                                continue
                            random_number = random.randint(0, 2)
                            computer_pick = options[random_number]
                            print("computer pick", computer_pick, ".")
                            if user_input == "rock" and computer_pick == "scissors":
                                print("You dem won! ")
                                user_wins += 1
                            elif user_input == "paper" and computer_pick == "rock":
                                print("You dem won! ")
                                user_wins += 1
                            elif user_input == "paper" and computer_pick == "scissors":
                                print("You dem won! ")
                                user_wins += 1
                            else:
                                print("You lost!")
                                computer_wins += 1
                    elif type_of_game == "computer guess":
                        guess_number = input("Enter a number for the computer to guess ")
                        if guess_number.isdigit():
                            guess_number = int(guess_number)
                        play_game(guess_number)
                    else:
                        print("Invalid input")
                        quit()
                else:
                    print("Nice job see you some other time...")
                    quit()
        else:
            print("Invalid input")
    elif work == "turn":
        print("Nice walk you need some rest ")
    else:
        print("Inavlid input")
elif adventure == "left":
    worker = input("You are heading to the river/desert would you like to swim or go back(river/desert)? ").lower()
    if worker == "river":
        river = input("We are at the river bank...would you like to swim or catch fish(swim/catch fish)").lower()
        if river == "swim":
            swim = input("You are about to swim...for how long would you like to swim? ")
            if swim.isdigit():
                swim = int(swim)
            for seconds in range(swim, 0, -1):
                print(seconds)
                time.sleep(1)
                print("You've been swiming for over ", seconds)
            print("Time is over sir/ma lets go out of the river")
            again = input("Would you like to swim again(yes/no) ").lower()
            if again == "yes":
                while True:
                    again1 = input("For how long would you like to swim ")
                    if again.isdigit():
                        again1 = int(again1)
                    for seconds in range(again1, 0, -1):
                        print(seconds)
                        time.sleep(1)
                        print("Wow nice swiming ")
                    again2 = input("Would you like to swim again (yes/no)").lower()
                    if again2 == "yes":
                        continue
                    else:
                        print("You need to catch fish this time around dude...")
                        break
            elif again == "no":
                print("Ok Sire/Ma you need to go and catch some fish ")
            else:
                print("Invalid input ")
                quit()
        elif river == "catch fish":
            catch_fish = input(
                "You are about to catch fish what type of fish would you like to catch(tillapia/shark)").lower()
            if catch_fish == "shark":
                print(
                    "You are about to catch a shark pls life jacket is very important if you don't wanna wear a life jacket do go for tillapia ")
                shark = input("Would you like to proceed for the shark hunt(yes/no)").lower()
                if shark == "yes":
                    print("You have 60 seconds to catch ")
                    for seconds in range(60, 0, -1):
                        print(seconds)
                        time.sleep(1)
                        print("You've got", seconds, "left")
                    print(
                        "You've catch for 60 seconds, due to gov't policies you cant proceed with catching it, need to visit the desert ....")
                    quit()
                elif shark == "no":
                    print("Nice to see you at th beach do enjoy the rest of the day ")
                else:
                    print("Invalid input ")
            elif catch_fish == "tillapia":
                tillapia1 = input("Wow you chose the simplest fishing type shall we(yes/no) ").lower()
                if catch_fish == "yes":
                    tillapia = input("For how long would you like to hunt some fishes ")
                    if tillapia.isdigit():
                        tillapia = int(tillapia)
                    for seconds in range(tillapia, 0, -1):
                        print(seconds)
                        time.sleep(1)
                    print("You've catch alot sire/ma ")
                    print("We have less fishes here pls proceed to the desert ")
                    quit()
                elif catch_fish == "no":
                    print("Do visit the desert sire/ma ")
                else:
                    print("Invalid input pls visit the desert sire/ma")
                    quit()
            else:
                print("Invalid input ")
        else:
            print("Invalid input")
    elif worker == "desert":
        desert = input("You are about to have a desert walk, would you like to walk?(yes/no)").lower()
        if desert == "yes":
            desert1 = input("For how long would you like to work...?")
            if desert.isdigit():
                desert1 = int(desert1)
            for seconds in range(desert1, 0, -1):
                print(seconds)
                time.sleep(1)
                print("You've being walking for over", seconds, )
            print("You've walked over sometimes now...desert policies you walk little ,I think you need to take a ride if you are with one..")
            ride = input("Do you have one (Yes/No)").lower()
            if ride == "yes":
                command = ""

                started = False

                breaked = False

                accelerate = False

                move = False

                while True:

                    command = input(">>").lower()

                    if command == "start":

                        if started:

                            print("car is already started!")

                        else:

                            started = True

                            print("about to start the car sit back and relax for count down ")

                            for seconds in range(10, 0, -1):
                                print(seconds)

                                time.sleep(1)

                            print("car started...")

                    elif command == "stop":

                        if not started:

                            print("car is already stop!")

                        else:

                            started = False

                            print("car stopped")

                    elif command == "break":

                        if breaked:

                            print("car is already on break please take is easy!!")

                        else:

                            breaked = True

                            print("car on hold type move to release the car break!")

                    elif command == "move":

                        if move:

                            print("car is moving already")

                        else:

                            move = True

                            print("car about to move...")

                            for seconds in range(5, 0, -1):
                                print(seconds)

                                time.sleep(1)

                            print("car is on release type accelerate to accelerate the car")

                    elif command == "accelerate":

                        if accelerate:

                            print("moving faster pls apply your seat belt")

                        else:

                            accelerate = True

                            print(
                                "moving on gear one,type accelerate to switch on the next gear when the engine sound chnages")

                    elif command == "help":

                        print("""
                        WELCOME TO AI

                    PLS FOLLOW THE COMMANDS FOR EASY USE

                START: TYPE START TO START THE CAR
                STOP: TYPE STOP TO STOP THE CAR
                BREAK:TYPE BREAK TO HOLD THE CAR
                MOVE:TYPE MOVE TO RELEASE THE CAR FROM BREAK
                ACCELERATE: TYPE ACCELERATE TO MOVE
                QUIT: TYPE QUIT TO EXIT THE CAR
                """)

                    elif command == "quit":

                        print(
                            "hope you enjoyed the ride, looking forward to see you some other time use your finger print to exit the car door")

                        break

                    else:

                        print("invalid input type help to know the key commands")
            elif ride == "no":
                print(" Sorry Sir/Ma let's go back for you are dehydrated..")
                water = input(" Would you like to drink wate(yes/no)").lower()
                if water == "yes":
                    food=["pure water ","bootle water ", "stream water "]
                    def order():
                        if (x.get()==1):
                            print("You ordered for Purewater")
                        elif(x.get()==2):
                            print("You ordered for bootle water")
                        elif(x.get()==3):
                            print("You ordered for Stream wtaer")
                    windows=Tk()
                    x=IntVar()
                    for index in range(len(food)):
                        radiobutton=Radiobutton(windows,
                                                text=food[index],
                                                padx=25,
                                                variable=x,
                                                value=index,
                                                font=("Italic",20),
                                                command=order)
                        radiobutton.pack(anchor=W)

                    windows.mainloop()
                elif water == "no":
                    print(" It means you really wanna go back so let's go sire/ma")
                    quit()
                else:
                    print(" Invalid input...")
            else:
                print("Invalid input...")
        elif desert == "no":
            market = input(" Would you like to go to the market for feed? (Yes/No)").lower()
            if market == "yes":
                print(" Okay let's goan take some snacks ")
                food = ["Shushi", "Bugger", "Ice cream", "Chinese bread"]


                def order():
                    if (x.get() == 0):
                        print("You ordered for Shushi")
                    elif (x.get() == 1):
                        print("You ordered for Bugger")
                    elif (x.get() == 2):
                        print("You ordered for Ice cream")
                    else:
                        print("You ordered for Chinese bread")


                windows = Tk()
                windows.title("Menu List")
                x = IntVar()
                for index in range(len(food)):
                    radiobutton = Radiobutton(windows,
                                              text=food[index],
                                              variable=x,
                                              value=index,
                                              padx=25,
                                              command=order,
                                              font=("Italic", 20))
                    radiobutton.pack(anchor=W)
                windows.mainloop()
            elif market == "no":
                paint = input("Would you like to go for painting house? (yes/no) ").lower()
                if paint == "yes":
                    def submit():
                        color=colorchooser.askcolor()
                        print(color)
                        hexcolor=color[1]
                        print(hexcolor)
                        windows.config(bg=hexcolor)
                    windows=Tk()
                    windows.geometry("420x420")
                    button=Button(windows,
                                  text="choose color",
                                  command=submit)
                    button.pack()
                    windows.mainloop()
                elif paint == "no":
                    print("You need to check your temperature ")
                    def submit():
                        print("your temperature is "+ str(scale.get())+ " degree(s) C")
                        if (scale.get()>37):
                            print("Your body Temperature is so high you really need to see your doctor ")
                        elif (scale.get()<15):
                            print("Your body Temperature is so cold you need to see your doctor")
                        else:
                            print("Yeah your body Temperature is okay ")
                    windows=Tk()
                    scale=Scale(windows,
                                from_=100,
                                to=0,
                                length=600,
                                tickinterval=10,
                                troughcolor="blue",
                                font=("Arial",25),
                                fg="black",
                                bg="red")
                    scale.pack()
                    button=Button(windows,
                                  text="Submit",
                                  command=submit)
                    button.pack()

                    windows.mainloop()
                else:
                    print("Wrong input sire/ma ")
                    quit()
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input pls rerun the program to have effective done in it ")
else:
    print("Invalid input")