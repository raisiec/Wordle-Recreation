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
  
pickRandomWord()

lives = 3

for i in range(lives):
  print(lives)
  guess = input("Guess the five-letter word.")

  if guess == answer:
    print("Yes.")
    break
  else:
    print("No.")

  lives = lives - 1

print("The correct answer is: " + answer)

# End
