# Authors: Kingsley + Raisie
# Date: 19/3/2022
# Topic: Wordle text-based lesson

import random

words = ["there", "queen", "aloft", "dream", "raise"]

# Create a function for choosing the random word
def pickRandomWord():
  global answer
  answer = words[random.randint(0, len(words) - 1)]
  print(answer)

def checkHint(guess, answer):
  for i in range(5):
    if (answer[i] == guess):
      return True
  return False

  
#Raisie is making the CheckWord function now.
def checkWord():
  hint_list = ""
  for i in range(5): 
    if (guess[i] == answer[i]): #'i' is a variable, it comes from the for-loop
      print("*")
    elif checkHint(guess[i], answer): # check if the char is on the answer list
      print("o")
    else:
      print("?") #Checking if its wrong


lives = 3
pickRandomWord() #Pick Random Word Before Guessing

for i in range(lives):
  print(lives)
  guess = input("Guess the five-letter word.")

  checkWord()

  if guess == answer:
    print("Yes.")
    break
  else:
    print("No.")

  lives = lives - 1

print("The correct answer is: " + answer)

# End
