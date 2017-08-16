def hows_the_parrot():
  print("He's pining for the fjords!")

hows_the_parrot()

def lumberjack(name, pronoun):
    print("{}'s a lumberjack and {}'s OK!".format(name, pronoun))

#lumberjack("Jeffrey", "he")
#lumberjack("Lola", "she")

def average(num1, num2):
  return (num1+num2) / 2

avg = average(2, 6)
#print(avg)

# Exceptions

try:
  count = int(input("Give me a number: "))
except ValueError:
  print("Thats not a number!")
else:
  print("Hi" * count)