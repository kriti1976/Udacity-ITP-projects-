import time

def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)

import random    


def intro(litem, choice):
    print_pause("You are going to the school and find a "
                "book on your way, after touching"
                " it you are surrounded "
                "with big trees and wildflowers.\n")
    print_pause("On a board you read that a " + choice + 
                " is somewhere around here, "
                "and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your left is a wide cave.\n")
    print_pause("You have a bag with a blunt knife which is not "
                " very effective.\n")

def still(litem, choice) :
    if "spear" in litem :
        print_pause("\nYou stand and wait for a while.")
        print_pause("\nThe " + choice + " comes and you "
                    " run away. \n")
                    
    else:
        print_pause("\nYou stand and wait for a while.")
        print_pause("\nThe " + choice + " comes and you "
                    "try to run away, and while running " 
                    + choice +" is left far behind."
                    "You find the great spear of Loki.\n")
        print_pause("\nYou walk back out to the field with spear.\n")
        litem.append("spear")
    area(litem, choice)
        
    


def darkcave(litem, choice) :
    if "spear" in litem :
        print_pause("\nYou go cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " stuff. It's an empty cave now. So you"
                    " walk back to field. \n")
    else:
        print_pause("\nYou go cautiously into the cave.")
        
        print_pause("\nYour eye catches something shiny behind a "
                    "rock.")
        print_pause("\nYou have found the magical Spear of Loki!.\n")
        print_pause("\nYou walk back out to the field with spear.\n")
        litem.append("spear")
    area(litem, choice)


def hut(litem, choice):
    print_pause("\nYou approach the door of the hut.")
    print_pause("\nWhen you knock the door "
                "opens and out steps a " + choice + ".")
    print_pause("\n This is the " + choice + "'s hut!")
    print_pause("\nThe " + choice + " attacks you!\n")
    if "spear" not in litem:
        print_pause("You are frightened , "
                    "as you only have a blunt knife,"
                    "But you stand to fight. \n")
    while True:
        c2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if c2 == "1":
            if "spear" in litem:
                print_pause("\nAs the " + choice + " moves to attack, "
                            "you attack with your new spear.")
                print_pause("\nThe Spear of Loki shines brightly in "
                            "your hand as you attack. ")
                            
                print_pause("\n The " + choice + " gets hurt ")
                print_pause("\nYou have saved the town of the " + choice +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your knife is no match for the "
                            + choice + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if c2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you are not followed.\n ")
                        
            area(litem, choice)
            break



def area(litem, choice):
    print_pause("Enter 1 to knock on the door of the hut.")
    print_pause("Enter 2 to go into the cave.")
    print_pause("Enter 3 wait for "+ choice+ " to come.")
    
    while True:
        c1 = input("(Please enter 1 or 2 or 3.)\n")
        if c1 == "1":
            hut(litem, choice)
            break
        elif c1 == "2":
            darkcave(litem, choice)
            break
        elif c1== "3":
            still(litem, choice)
            break



def play_again():
    again = input("Would you like to play again? (yes/no)").lower()
    if "yes" in again :
        print_pause("\n\nGreat! \n\n")
        play_game()
    elif "no" in again :
        print_pause("\n\nThanks for playing! Meet you soon.\n\n")
    


def play_game():
    litem = []
    choice = random.choice(["dragon", "wildlizard", "halfwolf", "gtroll"])
    intro(litem, choice)
    area(litem, choice)


play_game()