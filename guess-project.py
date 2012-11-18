# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


# initialize global variables used in your code
import random
import simplegui

player_number = 0

# define event handlers for control panel
def enter(inp):
    global player_number
    player_number = int(inp)
    get_input(player_number)

def range100():
    # button that changes range to range [0,100) and restarts
    ran100 = random.randint(0, 100)
    global comp_number
    comp_number = ran100
    return comp_number

def range1000():
    # button that changes range to range [0,1000) and restarts
    ran1000 = random.randint(0, 1000)
    global comp_number
    comp_number = ran1000
    return comp_number

def get_input(guess):
    # main game logic goes here
    if player_number > comp_number:
        print "Low !!"
    elif player_number < comp_number:
        print "High !!"
    else:
        print "Correct !!"
    
# create frame
f = simplegui.create_frame("Guess", 200, 200)

# register event handlers for control elements
f.add_input("Enter a number:",enter, 100)
f.add_button("Range 0-100",range100, 100)
f.add_button("Range 0-1000",range1000, 100)
f.add_button("Restart",range100, 100)

# start frame
range100()

# always remember to check your completed program against the grading rubric