#2022-2-5 Wordle Recreation (No GUI)
#Authors: Kingsley & Raisie
#Coding language : Python 3

#Import Stuff
import random
#from tkinter import Tk, Canvas

#List of 5 Letter Words
global words
words = ["aloft", "heart", "queen", "those", "learn"]

#Make the variables needed
global lives
lives = 6
answer = 0

#Define the functions need
def pickRandomWord():
  #First, pick a number as 'num'
  num = random.randint(0, 4)

  #Then, in the 'words' array, find 'num' and put it in 'answer'
  global answer
  answer = words[num]

def checkHint(guess, answer):
  for i in range(5):
    if (answer[i].lower() == guess.lower()):
      return True
  return False

def checkWord():
  hint_list = ''
  for i in range(5):
    if (guess[i].lower() == answer[i].lower()):
      hint = "*"
    elif checkHint(guess[i], answer):
      hint = "o"
    else:
      hint = "?"
    hint_list = hint_list + hint
  print(hint_list)

pickRandomWord()

#Main Loop
while (lives > 0):
  print("Lives left: ", lives)
  print("Your hints are (* = Right Letter and Right Place, o = Right Letter but Wrong Place, ? = nothing.")
  guess = input("Guess the five-letter word!")  

  checkWord()

  if guess == answer:
    print("You win!")
    break 
  else:
    print("You Lose, try again!")
    lives -= 1

#End of code