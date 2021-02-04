"""
Lists Introduction

This will introduce you to lists and the basics of using them. Working with lists to follow.
"""

# Lists can be made out of anything and not have to be related. Remember that lists indexing starts with 0 not 1.

_cars = ['mustang', 'corvette', 'f150', 'silverado']
print(_cars) # will print out list.
print()

# You can access certain elements within a list using index.

print(_cars[0]) # should echo out mustang.
print()
print(_cars[3]) # should echo out silverado.
print()

# You can modify lists using elements referenced in the variables section.

print(_cars[1].title()) # should print out Corvette.
print()

# If you have a long list, but need the last item in the list, you can use [-1] without knowing the index number. See example.
print(_cars[-1])
print()

# You can place list items into variables or strings.

_favorite_car = _cars[0]
_car_message = f"The {_cars[0].title()} is my dream car."

print(_favorite_car)
print()
print(_car_message)
print()

# The nice thing about lists is you can modify them with code if you need to.
# You can append to the list and will add at the end. In our case when we append to the _cars list that has four already this would be the fifth, but as you remember our lists start at zero so this will be index value four.

_cars.append('ram 1500') # this will add ram 1500 to the list at index 4.
print()

print(_cars)
print()

# What if I wanted to change that? I can change index 4 to anything I want.

_cars[4] = "impala"
print(_cars)
print()

# If you need to delete an item, it is easy to do so.

del _cars[4] # deletes impala
print(_cars)
print()

# If you can add to the list in any position that you want.

_cars.insert(0, "ram 1500") # this add ram 1500 at the beginning of the list.
_cars.insert(3, "escape") # this adds escape in the middle of the list.
print(_cars)
print()

# The pop() method is neat because it removes the item from the list but not from the playing field, here is an example.

_popped_vehicle = _cars.pop() # will remove the last item in the list
_identified_vehicle = _cars.pop(3) # will remove item index 3 from the list
print(_cars) # as you can see that two of the items are removed, but you can still use them.
print(_popped_vehicle)
print(_identified_vehicle)
print()

# You can also remove a specific item from the list as well.

_removed_car = 'mustang'
_cars.remove(_removed_car)
print(_cars)
print()

# You can also sort a list, let's put our cars back together and sort them.

_cars = ['ram 1500', 'mustang', 'corvette', 'escape', 'f150', 'silverado', 'impala', 'navigator']

_sorted_list = ['ram 1500', 'mustang', 'corvette', 'escape', 'f150', 'silverado', 'impala', 'navigator']
_sorted_list.sort()
print(_sorted_list)
print()

# You can also sort in the reverse direction

_sorted_list_revered = ['ram 1500', 'mustang', 'corvette', 'escape', 'f150', 'silverado', 'impala', 'navigator']
_sorted_list_revered.sort(reverse=True)
print(_sorted_list_revered)
print()

# You can temporarily sort a list without changing the true list.

print(sorted(_cars))
print()

# You can reverse the order of the list
_cars.reverse() # rervese the order
print(_cars)
print()
_cars.reverse() # reverts back to original order

# To find the length of a list
_cars_length = len(_cars)
print(_cars_length)
print()
