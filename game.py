import time
import random

weapons = ["A dagger\n", "A hammer\n", "A flying star\n", "A knife\n",
           "A spear\n", "An axe\n"]
my_weapon = random.choice(weapons)


def play_game():
    intro()
    choose()
    choose_again()
    one_more_game()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        elif option2 == response:
            break
        else:
            print("No option like this.")
    return response


def intro():
    print_pause("You find yourself standing in an open field, filled "
                "with grass "
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) weapon.")
    print_pause("Your weapon is going to be in this part...")
    print_pause("Let's see...\n")
    print_pause(my_weapon)
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")


def game_over():
    print_pause("Your weapon is no match for the wicked fairie...")
    print_pause("You are not strong enough against the fairie!")
    print_pause("You have been defeated!")
    print_pause("GAME OVER")


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and steps a wicked fairie.")
    print_pause("Eeep! This is the wicked fairie's house.")
    print_pause("The wicked fairie attacks you!")
    print_pause("You feel a bit under-prepared for this, with only having "
                "a tiny weapon...")
    print_pause("...but you do your best...")


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old weapon and take a sword with you.")
    print_pause("You walk back out to the field.\n")
    print_pause("You have got the sword! You are strong enough now!")
    print_pause("You come back to the house with your new weapon.")
    print_pause("The fairie is scared and run away.")
    print_pause("It was a good choice to peer into the cave!")
    print_pause("You won!")
    one_more_game()


def choose_again():
    print_pause("You should run away to the cave, before you die.")
    print_pause("Maybe there is something for you.")
    response = valid_input("Would you like to go to the CAVE or "
                           "just keep FIGHTING?\n"
                           "Please enter cave or fighting.\n",
                           "fighting", "cave")
    if "fighting" in response:
        game_over()
        one_more_game()

    elif "cave" in response:
        cave()
        one_more_game()


def choose():
    response = valid_input("(Please enter 1 or 2).\n",
                           "1", "2")
    if response == '1':
        house()
        choose_again()

    elif response == '2':
        cave()

    else:
        return response


def one_more_game():
    response = valid_input("Would you like to play one more?\n"
                           "Please enter yes or no.\n",
                           "yes", "no")
    if response == 'no':
        print_pause("Thank you for playing with my game! "
                    "See you next time! Bye!")
        exit(0)

    elif response == 'yes':
        print_pause("OKAY, let's play one more!")
        intro()
        choose()


play_game()
