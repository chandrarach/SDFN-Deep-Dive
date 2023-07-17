import time


import random


def msg_echo(msg):
    print(msg)
    time.sleep(2)


def intro():
    # Greet the Player and offer few choices to play the game #
    msg_echo("You find yourself standing in an open field,"
             "filled with grass and yellow wildflowers.\n")
    msg_echo("Rumor has it that a wicked fairie is somewhere around here, and"
             " has been terrifying the nearby village.\n")
    msg_echo("In front of you is a house.\n")
    msg_echo("To your right is a dark cave.\n")
    msg_echo("In your hand you hold your trusty (but not "
             "very effective) dagger.\n")
    msg_echo("Enter 1 to knock on the door of the house,"
             " Enter 2 to peer into the cave\n")


#   OFFER THE MAIN OPTIONS AVAILABLE TO PLAY THE GAME #
def select_options():
    choices = ["1", "2"]   # list of Options available #
    # reply = input("Please enter 1 or 2 only.\n")
#   reply=random.randint(1,2) # randomly selects #
# msg_echo("Enter either the digit 1 or the digit 2 ONLY!"
#  " Nothing else is allowed to continue.\n")
    reply = input("Please enter 1 or 2 only.\n")
    while (reply not in choices):
        # msg_echo(" You Must Enter either the digit 1 or the digit 2 ONLY! "
        #          "Nothing else is allowed to continue.\n")
        reply = input("Please enter either 1 or 2 only.\n")
    if reply == "1":
        choose_knock()
    elif reply == "2":
        choose_cave()    # Select the option to look into the cave#


#   WHAT HAPPENS WHEN THE PLAYER KNOCKS THE HOUSE DOOR   #
def choose_knock():
    choices = ["1", "2"]
    msg_echo("You approach the door of the house.\n")
    msg_echo("You are about to knock when the door opens & "
             "out steps a dragon.\n")
    msg_echo("Eep! This is the dragon's house!\n")
    msg_echo("The dragon attacks you!\n")
    msg_echo("You feel a bit under-prepared for this, what with "
             "only having a tiny dagger.\n")
    msg_echo("Would you like to (1) fight or (2) run away?\n")
    re_reply = input("Please enter 1 or 2 only.\n")
    while re_reply not in choices:
        msg_echo("Pl. Enter 1 OR 2 ONLY to continue.\n")
        re_reply = input("Please enter 1 or 2 only.\n")
    if re_reply == "1":
        choose_fight()  # Select the option to fight with the dragon
    elif re_reply == "2":
        msg_echo("You run back into the field. Luckily, "
                 "you don't seem to have been followed.\n")
        select_options()  # Back 2 Select the options #


#  WHAT HAPPENS WHEN THE USER SELECTS TO ENTER THE CAVE  #
def choose_cave():
    choices = ["1", "2"]
    msg_echo("You peer cautiously into the cave.\n")
    msg_echo("It turns out to be only a very small cave.\n")
    msg_echo("Your eye catches a glint of metal behind a rock.\n")
    msg_echo("You have found the magical Sword of Ogoroth!\n")
    msg_echo("You discard your silly old dagger and take "
             "the sword with you.\n")
    msg_echo("You walk back out to the field.\n")
    msg_echo("Enter 1 to knock on the door of the house."
             " Enter 2 to peer into the cave.\n")
    re_reply = input("Please enter 1 or 2 only.\n")
#   Prompt the User to type ONLY 1 or 2 proceed with the game  #
    while (re_reply not in choices):
        msg_echo(" You Must Enter either the digit 1 or the digit 2 ONLY! "
                 "Nothing else is allowed to continue.\n")
        re_reply = input("Please enter either 1 or 2 only.\n")
    if re_reply == "1":
        choose_fight()
    elif re_reply == "2":
        choose_cave()


#  WHAT HAPPENS WHEN THE USER SELECTS TO FIGHT WITH THE DRAGON  #
def choose_fight():
    choices = ["y", "n","Y","N"]
    msg_echo("You do your best...\n")
    msg_echo("but your dagger is no match for the dragon.\n")
    msg_echo("You have been defeated!\n")
    answer = input("Would you like to play again? (y/n)\n").lower()
#   KEEP PROMPTING THE USER UNTIL THE USER TYPES Y/y/N/n- ONLY #
    while (answer not in choices):
        msg_echo("You Must Enter y OR Y OR n OR N ONLY!"
                 " Nothing else is allowed to continue.\n")
        answer = input("Please enter y or Y " 
                       " or N or n only.\n").lower()
#     END LOOP IF USER INPUT SATISFIES ONE OF THE AVAILABLE OPTIONS #
    if answer == "y":
        msg_echo(" Excellent! Let us play Again!\n")
        Total_Run()   # Play game again from the beginning
    elif answer == "n":
        msg_echo("Thanks for playing! See you next time.\n")
# Terminate the game  #


# CONSOLIDATE THE GAME BY CALLING THE INDIVIDUAL SEGMENTS IN SEQUENCE   #
def Total_Run():
    intro()
    select_options()


#     START PLAYING THE GAME    #
Total_Run()

