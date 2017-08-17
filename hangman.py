import random

# make a list of words
words = [
  'ruby',
  'python',
  'javascript',
  'elm',
  'angular',
  'react',
  'haskell',
  'swift',
  'elixir'
]

while True:
  start = input("Press enter to start or Q to quit")
  if start.lower() == 'q':
    break

  secret_word = random.choice(words)
  bad_guesses = []
  good_guesses = []
  
  while len(bad_guesses) < 7 and len(list(secret_word)) != len(good_guesses):
    for letter in secret_word:
      if letter in good_guesses:
        print(letter, end='')
      else:
        print('_', end='')

    print('')
    print("Strikes {}/7 guesses".format(len(bad_guesses)))
    print('')

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
      print("You can only guess one letter at a time")
      continue
    elif guess in bad_guesses or guess in good_guesses:
      print("You've already guessed that letter")
    elif not guess.isalpha():
      print("You can only guess letters")
      continue

    if guess in secret_word and guess not in good_guesses:
      occurence = secret_word.count(guess)
      good_guesses.append(guess * occurence)
      if len(good_guesses) == len(list(secret_word)):
        print("You win! The word was {}".format(secret_word))
        break
    else:
      bad_guesses.append(guess)

  else:
    print("Sorry, better luck next time! The word was {}".format(secret_word))
