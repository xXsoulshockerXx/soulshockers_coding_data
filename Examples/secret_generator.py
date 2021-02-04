"""
Secret Generator

This is a program that well randomly generate a secure password.
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
# Initialize Program
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
import random

password = "" # empty variable #

# A function do shuffle all the characters of a string #
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# Generate 5 Uppercase Letters #

for uppercase in range(5):
    uppercase = chr(random.randint(65,90))
    password = password + uppercase

# Generate 5 Lowercase Letters #

for lowercase in range(5):
    lowercase = chr(random.randint(97,122))
    password = password + lowercase

# Generate 5 Numbers #

for number in range(5):
    number = chr(random.randint(48,57))
    password = password + number

# Generate 5 Punctuation #

punctuation = [chr(33), chr(64), chr(35), chr(36), chr(37), chr(94), chr(38), chr(42)] # will generate these ! @ # $ % ^ & * #

for punc in range(5):
    punc = punctuation[random.randint(0,7)]
    password = password + punc

# Generate password using all the characters, and shuffled in at random. #
password = shuffle(password)

# Ouput #
print(password)