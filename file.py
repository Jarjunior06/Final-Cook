# file hadler
#jas, JR
#11/29/23

import random
def choose_word():
  words = ["jazzy","pizza","juicy","exams","apple","biffy"]
  return random.choice(words)

def display_word(word, guessed_letters):
  display = ""
  for letters in word: 
  if letters in guessed_letters:
    display += letter
  else:
    display += "_"
    return display

def wordle():
  max attempts = 6
  guessed_letters + []
  word_to_guess = choose_word()

print("Welcome to Wordle!")

for attempt in range(max_attempts):
  print("\nAttempt", attempt + 1)
  current_display =
display_word(word_to_guess, guessed_letters)
print("Current Word:",,
current_display)

guess = input("Enter your guess:").lower()

      if len(guess) == 1 and 
guess.isalpha():
   guessed_letters.append(guess)

if set(guessed_letters) >=
set(word_to_guess):
       print("Congratulations! You guessed the correct word:", word_to_guess)
  break
else:
print("Invalid input. Please enter another single letter.")

else:
  print("Sorry, you ran out of attempts. The correct word was:", word_to_guess)
  if __name__ == "__main__":
    wordle()
