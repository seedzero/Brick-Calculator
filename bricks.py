#!/usr/bin/env python3
from termcolor import cprint  # pip3 install termcolor

VERSION = 0.6


def usage():
    helpstring = "\nType 'c' before a number for brick length to corner " \
                 "or 'o' for width of opening.\n\n" \
                 "Input                         Output\n" \
                 "=====                         ======\n" \
                 "4                             4 bricks is 950\n" \
                 "950                           4 bricks exactly.\n" \
                 "c5                            5 bricks to corner is 1200\n" \
                 "o6                            6 brick opening is 1450"
    print(helpstring)


def bricksInLength(bl):
    num_bricks = 0
    bl = bl - 230
    num_bricks += 1
    brick_remainder = bl % 240
    brick_with_mortar = bl - brick_remainder
    num_bricks += int(brick_with_mortar / 240)
    if num_bricks == 1 and brick_remainder <= 119:
        unit = " brick"
    else:
        unit = " bricks"
    if brick_remainder == 120:
        cprint(str(num_bricks) + " and a half bricks.", "green")
    elif brick_remainder == 0:
        cprint(str(num_bricks) + unit + " exactly.", "green")
    elif brick_remainder == 20:
        cprint(str(num_bricks) + " brick opening", "blue")
    elif brick_remainder == 140:
        cprint(str(num_bricks) + " and a half brick opening", "blue")
    elif brick_remainder == 10:
        cprint(str(num_bricks) + unit + " to corner (" + str(num_bricks) +
               unit + " plus 10mm mortar)", "yellow")
    elif brick_remainder == 130:
        cprint(str(num_bricks) + " and a half bricks to corner (" +
               str(num_bricks) + " and a half bricks plus 10mm mortar)",
               "yellow")
    else:
        brick_string = str(num_bricks)
        if brick_remainder > 120:
            brick_remainder -= 120
            brick_string = brick_string + " and a half"
        part_brick = brick_remainder / 230
        cprint("Not a standard length. " + brick_string + unit + " with " +
               "remainder of " + str(int(brick_remainder)) + ", which is " +
               str(part_brick) + " of a brick.", "red")


def bricksToLength(bl):
    brick_length = 230
    if bl.is_integer():
        brick_length = brick_length + ((int(bl) - 1) * 240)
        return(brick_length)
    else:
        if bl - int(bl) == .5:  # Check to make sure half brick only
            brick_length = brick_length + ((int(bl) - 1) * 240 + 120)
            return(brick_length)
        else:
            print("Cannot calculate " + str(bl - int(bl)) + " of a brick.")


def unitString(n, op=False):
    if n - int(n) == .5:
        if op is False:
            return "and a half bricks"
        else:
            return "and a half brick"
    elif n == 1 or op is True:
        return "brick"
    elif n.is_integer():
        return "bricks"
    else:
        return "whoops"


def calculateOpening(o):
    if validNumber(o):
        cprint(str(int(o)) + " " + unitString(o, op=True) + " opening is " +
               str(bricksToLength(o) + 20), "blue")


def calculateCorner(c):
    if validNumber(c):
        cprint(str(int(c)) + " " + unitString(c) + " to corner is " +
               str(bricksToLength(c) + 10), "yellow")


def calculateLength(l):
    if validNumber(l):
        if l >= 230:
            bricksInLength(l)
        else:
            cprint(str(int(l)) + " " + unitString(l) + " is " +
                   str(bricksToLength(l)), "green")
        return True
    else:
        return False


def validNumber(n):
    if n - int(n) == .5 or n - int(n) == 0:
        return True
    else:
        print("Invalid Number")
        return False

cprint("\nBrick Calculator v" + str(VERSION) + " by Keith Irvine",
       "grey", "on_red")
print("Type 'h' for help or 'q' to quit")

while True:
    userInput = input("\nLength in mm or # of bricks >> ")
    prefix = userInput[0].lower()
    if prefix == "o" or prefix == "c":
        try:
            float(userInput[1:])
            if prefix == "o":
                calculateOpening(float(userInput[1:]))
            if prefix == "c":
                calculateCorner(float(userInput[1:]))
        except:
            print(userInput[1:] + " isn't a number dumbass")
        continue
    if userInput.lower() == "help" or userInput.lower() == "h":
        usage()
        continue
    if userInput.lower() == "quit" or userInput.lower() == "q":
        print("quit")
        print("")
        break
    try:
        float(userInput)
        calculateLength(float(userInput))
    except:
        print("Invalid input: '" + userInput + "', Type 'h' for help.\n")
