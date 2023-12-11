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
      display += letters
  else:
    display += "_"
    return display

def wordle():
  max_attempt = 6
  guessed_letters = []
  attempt=0
  secret_word = choose_word()

  print("Welcome to Wordle!")
  print(display_word(secret_word, guessed_letters))
  
  while attempt < max_attempt:
      guess=input("Enter your guess!:").lower()
      if len(guess)==1 and guess.isalpha():
          if guess in guessed_letters:
                        print("you already guessed that letter. try again")
          elif guess in secret_word:
            print("corret!")

      guessed_letters.append(guess)
  else:
      print("Inncorect!")
      attempt +=1

      print(display_word(secret_word, guessed_letters))


  if set(guessed_letters) == set(secret_word):
    print("congrautulations! you guessed the word!:", secret_word)
    

    print("attempts left:", max_attempt - attempt)
  else:
    print("invaild input. plesae enter a single letter")

    if attempt == max_attempt:
      print("sorry your out of attempts. the word was:", secret_word)

wordle()
