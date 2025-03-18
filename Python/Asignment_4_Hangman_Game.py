# HANGMAN GAME

a = "Taha"

guessed_letter = []

while True:
  guess = input("Enter one letter: ")
  if guess in a:
    guessed_letter.append(guess)

  display_word = ""

  for i in a:
    if i in guessed_letter:
      display_word += i
    else:
      display_word += "_"

  print(display_word)

  if (a == display_word):
    print("You guessed the correct word")
    break

