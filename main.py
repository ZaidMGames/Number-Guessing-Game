import random



#Allows player to actually setup the game themselves
def setup ():
  global n
  global d
  global numb
  global life
  life = 10
  print("\nWelcome to the Number Guessing game  ")
  print("First off, I want you to choose your range  ")
  n =input("\nType in the minimum number you want me to guess from   ")
  d =input("Now type in the maximum number you want me to guess from   ")
  numb = random.randint(int(n),int(d))

#Game itself
def guessing():
  global life
  guess = input ("\nTry guess a number between " + n  + " and " + d + " ")
  while int(guess) != int(numb) and life > 1:
    if int(guess) < int(numb):
      print ("\nThat guess is too low")
      life = life - 1
      print(" You now have " + str(life))
      guess = input ("\n Try again  ")
    elif int(guess) > int(numb):
      print ("\nThat guess is too high")
      life = life - 1
      print(" You now have " + str(life))
      guess = input ("\n Try again  ")

#Response once player has either won or lost all lives
def checking():
  global again
  if int(life) > 1 :
    print("\nWELL DONE you finished with " + str(life) + " Lives left")
    print("the number was "+ str(numb))
    again = input ("Wanna play again? y/n  ")
  else:
    print("\nLMFAO YOU DIDN'T GET IT")
    print("the number was "+ str(numb))
    again = input ("Wanna play again? y/n  ")


#Beginning of the actual Code
setup()
guessing();
checking()


#Restart Game or Close Program options here
while  again.lower() == "y":
  setup()
  guessing();
  checking()

if again.lower() == "n":
  print ("\nThanks for Playing, Have a good rest of your day, Bye bye now ")

