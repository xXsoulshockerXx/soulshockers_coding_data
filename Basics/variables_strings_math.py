"""
Variables, Strings, & Mathematics

This is an introduction to variables, strings, and math with Python. This is the basics and will go in depth later on.
"""

# This is a comment
# This is a print function. This will print on screen anything listed.
# When coding Python, you don't need to ; at the end like other code platforms.
print('Hello World')
print()

# Variables
# Variables are case sensitive and are treated differently depending on the case and/or spelling.
# You can use numbers in the variable's name as long a it doesn't start with one.
# It is typically accepted to start a new variable with an underscore.
# It's not a requirement but helps to identify and to clean up code.
# In these examples, I will mix it up to show how confusing it can sometimes get.
_testVariable = 'test'

# Let's check out the new variable
print(_testVariable)
print()

# Let's add a few more variables and play around
_classic_price = .5
_UScurrency = True
_type_of_coin = "cents"
_bananas = 25
_totalPrice = _bananas * _classic_price

# To print out multiple variables you can do it a few ways
print(_bananas, "bananas")
print()
print(_classic_price, _bananas)
print()

# You can attach two or more variables together by calling them with a + in between. Or you can add text in "".
print("I am buying", _bananas, "bananas at", _classic_price, _type_of_coin + ".")
print()
print("The price is:", _totalPrice, _type_of_coin + ".")

# If you are going to have multiple lines, you can implement the blockquote method.
_quote1 = '''This is a blockquote using three single quotation marks.
This is the second line in the quote.
Here is the third line. Isn't this cool?'''

_quote2 = """This is a blockquote using three double quotation marks.
It basically does the same thing.
However, it is really cool."""

print()
print(_quote1)
print()
print(_quote2)
print()

message = "Hello World"
string1 = "This is a string. It can be more defined like a sentance."
string2 = 'This can also be a string.'
flexible_string = 'I tweeted "Python is my favorite language" on Twitter.'
flexible_string1 = "To most people the name 'Python' is referred to the snake."
flexible_string2 = "The coding language Python's community is vast and resourceful."

print(message)
print(string1)
print(string2)
print(flexible_string)
print(flexible_string1)
print(flexible_string2)
print()

name = "ashton carter"
name2 = "Ashton Carter"

print(name.title()) # prints out Ashton Carter
print(name2.upper()) # prints out ASHTON CARTER
print(name2.lower()) # prints out ashton carter
print()

first_name = "ashton"
last_name = "carter"
full_name = f"{first_name} {last_name}" # this is a format string or f-string. use f before quotations and python will setup the rest.
print(f"Hello, {full_name.title()}!")
print()

# To add new lines or tabs in 
# \n is new line
# \t is new tab
print("Languages:\n\tEnglish\nSpanish\nItalian")
print()

favorite_language ='English '
favorite_language1 =' Italian '

# To remove whitespace

print(favorite_language.rstrip())
print(favorite_language1.lstrip()) # removes from left side.
print(favorite_language1.strip()) # removes from both sides
print()

# Python can do math, even order of operations

math = 2 + 3
math1 = 3 - 2
math2 = 2 * 3
math3 = 3 / 2

print(math)
print(math1)
print(math2)
print(math3)
print()

_complex_math = 3
_complex_math0 = 2
_complex_math1 = 6
_complex_math2 = 9
_complex_math3 = 24

print("This next format will process this formula: [(3 + 2) / 6 + 9]")
_complex_formula = (_complex_math + _complex_math0) / _complex_math1 + (_complex_math2 * _complex_math3)
print(_complex_formula)
print()

# In this example you should have gotten 216.
# You can covert numbers to floats or integers.
print(float(12))
print(int(10.4))
print(float(int(15.5)))
# You should get 12.0, 10, and 15 respectively.
print()

# Let's convert _complex_formula into an integer.

print(int(_complex_formula))
print()

math4 = 2 + 3*4
math5 = (2 + 3) * 4

print(math4)
print(math5)
print()

# Python can do decimals and floats. Will do what you expect, however, sometimes you might get arbitrary numbers.

math6 = 0.1 + 0.1
math7 = 2 * 0.2
math8 = 0.2 + 0.1
math9 = 3 * 0.1

print(math6)
print(math7)
print(math8)
print(math9)
print()

# Python can do fractions as you expect.

math10 = 4/2

print(math10)

# When using long numbers you can place underscores and won't affect the output

math11 = 14_000_000

print(math11)
print()

# Constant values
# Python doesn't have default constant values, however, in all caps, variables will be treated as true values to never be changed.

_CONSTANT_MATH = 5_000

print(_CONSTANT_MATH)
print()

# Sometimes we may need to add a number to our variables in mid program. Easy way to do that is through += 1 system. See below.

math12 = 412
print(f"There are {math12} students enrolled in math.")
math12 += 20
print(f"There are {math12} students enrolled in math.")
print()

# This is an excerpt from 'The Zen of Python'. A library that you can import, make your code simple where possible.
import this

print()