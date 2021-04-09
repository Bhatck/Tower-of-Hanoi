winlist = ['99']
pin1 = ['99']
pin2 = ['99']
pin3 = ['99']
win = False
# game loop
x = int(input("how many discs?: "))
while x > 0:
    pin1.append(str(x))
    winlist.append(str(x))
    x = x - 1
print(winlist, pin1)
while True:
    if not win:
        inp = str(input()).strip()  # user input used by the mess of code below
        inpl = inp.split(",")
        # move discs from one pin to another
        # TODO: optimize the way this mess works
        if inpl[0] == "1":
            if inpl[1] == "2" and pin1[-1] < pin2[-1]:
                tempvalue = str(pin1[-1])
                pin1.pop(-1)
                pin2.append(tempvalue)
            elif inpl[1] == "3" and pin1[-1] < pin3[-1]:
                tempvalue = str(pin1[-1])
                pin1.pop(-1)
                pin3.append(tempvalue)
        elif inpl[0] == "2":
            if inpl[1] == "1" and pin2[-1] < pin1[-1]:
                tempvalue = str(pin2[-1])
                pin2.pop(-1)
                pin1.append(tempvalue)
            elif inpl[1] == "3" and pin2[-1] < pin3[-1]:
                tempvalue = str(pin2[-1])
                pin2.pop(-1)
                pin3.append(tempvalue)
        elif inpl[0] == "3":
            if inpl[1] == "1" and pin3[-1] < pin1[-1]:
                tempvalue = str(pin3[-1])
                pin3.pop(-1)
                pin1.append(tempvalue)
            elif inpl[1] == "2" and pin3[-1] < pin2[-1]:
                tempvalue = str(pin3[-1])
                pin3.pop(-1)
                pin2.append(tempvalue)

        # determine if the player has won
        if pin2 == winlist or pin3 == winlist:
            win = True
            print("you have won!")
            input()
            break

# TODO: make a better way to display the contents of the pins
    print('pin 1:', pin1, "\npin 2:", pin2, '\npin 3:', pin3)  # show the contents of the pins on screen
