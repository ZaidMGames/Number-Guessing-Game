from simple_colors import *
import random
from termcolor import colored


#Allows player to actually setup the game themselves
def setup():
    global n
    global d
    global numb
    global life
    life = 10
    print("\nWelcome to the " +
          colored("Number Guessing game", 'yellow', attrs=['bold']))
    print("First off, I want you to choose your range ")
    n = input("\nType in the minimum number you want me to guess from   ")
    d = input("Now type in the maximum number you want me to guess from   ")
    numb = random.randint(int(n), int(d))


#Game itself
def guessing():
    global life
    guess = input("\nTry guess a number between " + str(n) + " and " + str(d) +
                  "")

    while int(guess) != int(numb) and life > 1:
        if int(guess) < int(numb):
            print("\nThat guess is too low")
            life = life - 1
            print(" You now have " +
                  colored(str(life), 'red', attrs=['bold']) + " Lives")
            guess = input("\n Try again  ")
        elif int(guess) > int(numb):
            print("\nThat guess is", red("too high", ["bold"]))
            life = life - 1
            print(" You now have " +
                  colored(str(life), 'green', attrs=['bold']) + " Lives")
            guess = input("\n Try again  ")


#Response once player has either won or lost all lives
def checking():
    global again
    if int(life) > 1:
        print("\nWELL DONE you finished with " + str(life) + " Lives left", )
        print("           The number was " + str(numb))
        again = input("\nWanna play again? y/n  ")
    else:
        print("\nLMFAO YOU DIDN'T GET IT")
        print("           The number was " + str(numb))
        again = input("\nWanna play again? y/n  ")


#Beginning of the actual Code
setup()
guessing()
checking()

#Restart Game or Close Program options here
while again.lower() == "y":
    setup()
    guessing()
    checking()

if again.lower() == "n":
    print("\nThanks for Playing, Have a good rest of your day,", cyan("Bye bye now ",['bold']))
