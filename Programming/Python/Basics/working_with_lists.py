"""
Working with Lists

This will be a more indepth with Lists.
"""

# # Looping a list # #

dogs = ['husky', 'malamute', 'german sheppard']
for dog in dogs:
    print(dog)

print()

for dog in dogs:
    print(f"{dog.title()} is a good dog.")

print()

# Using the range() function, you can generate a series of numbers into a list and use them.

for number in range(1, 10):
    print(number)

print()

# You may have noticed that when it outputs this function it only counts to 9. A weird off-by-one behavior result in Python. If you wanted to go to 10 you would do:
for number2 in range(1, 11):
    print(number2)

print()

# You can also define a range as well

numbers = list(range(1, 11))
print(numbers)
print()

# You can skip numbers in a range list.
skip_numbers = list(range(2, 21, 2)) # startes at two, ends at twenty and skips every two numbers.
print(skip_numbers)
print()

skip_numbers2 = list(range(1, 21, 3)) # startes at one, ends at twenty and skips every three numbers.
print(skip_numbers2)
print()

# Exponents, you can use lists and numbers to multiply. Using ** to represent exponents
exponent_numbers = []
for number3 in range(1, 11):
    exponent_number = number3 ** 2
    exponent_numbers.append(exponent_number)
print(exponent_numbers)
print()

# With Python, you can use it to find the Min, Max, and Sum of numbers in a list. Basically using statistics

the_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(the_numbers)) # should be 0
print(max(the_numbers)) # should be 9
print(sum(the_numbers)) # should be 45
print()

# The following is a list comprehension. Instead of using 3 to 4 lines of code for a function, you can simplify it. Write the variable, then assign a value for the range and send it to the second power.

exponents = [exp**2 for exp in range(1, 11)]
print(exponents)
print()

# # Slicing a List # #
people = ['Tony Stark', 'Col. Jack O\'Neill', 'Master Chief', 'Arthur Morgan', 'Castiel']
print(people)
print(people[0:2]) # starts at index 0 and ends at index 2
print(people[2:4]) # starts at index 2 and ends at index 4
print(people[:3]) # without an beginning indication, it will start at index 0 and end at index 3
print(people[2:]) # starts at index 2 and goes all the way to the end
print(people[-3]) # prints out the last three characters in the list
print()

print("These are Fictional People, however, still pretty Cool:")
for person in people[:3]: # selects the first 3 index
    print(person.title())
print()

# # Copying a List # #
# Often you might want to make changes to a list but without modifying the original list. Instead of re-writing lines of code, you can copy it.

favorite_songs = ['Dreams', 'World\'s Apart', 'Gypsy', 'Carry on My Wayward Son']
print('My favorite songs are:')
print(favorite_songs)
print()

friends_favorite_songs = favorite_songs[:] # by doing [:] selects all thing the list and adds it to the new list. If you don't use [:] then the list would equal eachother and any changes would affect both lists equally.
friends_favorite_songs.append('Sweet Child of Mine')
print(friends_favorite_songs)
print()

# # Tuples # #
# Is a list where items cannot change. Essentially an immutable list. Looks exactly like a standard list, however, instead of square brackets you use parentheses. While these are simple data structures, use them when you don't want values to change during the life of a program.

lyrics = ('Thunder only happens when it\'s raining.', 'Player\'s only love you when they\'re playing.')
for lyric in lyrics:
    print(lyric)
print()


# Now you can write over a tuple by defining new items in the same variable. It won't error out.
lyrics = ('Carry on, my wayward son.', 'There will be peace when you are done.', 'Lay your weary head to rest.', 'Don\'t you cry no more.')
for lyric in lyrics:
    print(lyric)
print()