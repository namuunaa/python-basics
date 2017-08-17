import random

# generate a random number
# user needs to guess the number
def game():
  secret_number = random.randint(1, 10)

  guess_count = 3

  while guess_count > 0:
    try:
      guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
      print("Not a number!")
    else:
      guess_count -= 1
      if guess == secret_number:
        print("Congratulations! The secret number was {}".format(secret_number))
        break
      elif guess > secret_number:
        print("Your guess is too high! Try again. You have {} guesses left.".format(guess_count))
      elif guess < secret_number:
        print("Your guess is too low! Try again. You have {} guesses left.".format(guess_count))
      else:
        print("That was not a number! Try again")

  else:
    print("Sorry! The number was {}.".format(secret_number))
  play_again = input("Wanna play again? y/n ")
  if play_again.lower() == 'y':
    game()
  else:
    print("BYE")


game()