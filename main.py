import random

life = 10
def setup ():
  print("Welcome to the Number Guessing game  ")
print("First off, I want you to choose your range  ")
n =input(" Type in the minimum number you want me to guess from   ")
d =input("Now type in the maximum number you want me to guess from   ")
numb = random.randint(int(n),int(d))

def guessing():
  global life
  guess = input ("Try guess a number between " + n  + " and " + d + " ")
  while int(guess) != int(numb) and life > 1:
    if int(guess) < int(numb):
      print ("That guess is too low")
      life = life - 1
      print(" You now have " + str(life))
      guess = input ("That was not the right number lol, Try again  ")
    elif int(guess) > int(numb):
      print ("That guess is too high")
      life = life - 1
      print(" You now have " + str(life))
      guess = input ("That was not the right number lol, Try again  ")
  



#Beginning of the actual Code
setup()
guessing();

if int(life) > 1 :
  print("WELL DONE you finished with " + str(life) + " Lives left")
  print("the number was "+ str(numb))
  again = input ("Wanna play again? y/n  ")
else:
  print("LMFAO YOU DIDN'T GET IT")
  print("the number was "+ str(numb))
  again = input ("Wanna play again? y/n  ")


#Need to fix this part below 
if again.lower() == "y":
  setup()
  guessing();
