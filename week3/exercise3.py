"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
from __future__ import division
from __future__ import print_function
from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nwelcome to the advanced guessing game!")
    print("A number between _ and _ ?")
    # lowerBound = raw_input("Enter a lower bound: ")
    # upperBound = raw_input("Enter an upper bound: ")
    while True:
        lowerBound = raw_input("Please enter a lower bound which is a valid integer: ")
        if str(lowerBound).isdigit():
            break
    while True:
        upperBound = raw_input("Please enter an upper bound which is a valid integer: ")
        if str(upperBound).isdigit() and int(upperBound) > int(lowerBound):
            break
    #    while upperBound <= lowerBound:
    #    upperBound = raw_input("Enter a number higher than lower bound: ")
    #    if upperBound >= lowerBound:
    #        break
    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        while True:
            guessedNumber = raw_input("guess a valid number: ")
            if str(guessedNumber).isdigit():
                break

        print("you guessed {},".format(guessedNumber),)

        while True:
            if str(guessedNumber).isdigit() == False:
                guessedNumber = raw_input("Guess a valid integer pls: ")
            elif int(guessedNumber) < lowerBound or int(guessedNumber) > upperBound:
                guessedNumber = raw_input("That's outside of the range. Guess again: ")
            else:
                break

        if int(guessedNumber) == int(actualNumber):
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif int(guessedNumber) < int(actualNumber):
            print("too small, try again ")
        else:
            print("too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
