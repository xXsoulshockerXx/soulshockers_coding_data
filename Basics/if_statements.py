"""
IF Statements

In programming, often enough it involves examinating a set of conditions and deciding on the actions to take.
"""

# IF statements work as you expect and come in a variety. In this example, we will set a variable and check to see if it is true or false.
favorite_movie = 'Avenger\'s Endgame' # sets the variable. This is a statement.
print(favorite_movie == 'Avenger\'s Endgame') # Using a double equals sign, you are asking if a variable is this or that. So it will respond with True or False.
print(favorite_movie == 'Iron Man') # this will return false because that is not the correct value.
print()

# Python is case sensitive most of the time. So if the cases don't match then it won't pull the right results unless you modify the variable as shown below.
print(favorite_movie == 'Avenger\'s Endgame') # The cases match so it will return true.
print(favorite_movie == 'avenger\'s endgame') # The cases don't match so it will return false.
print(favorite_movie.lower() == 'avenger\'s endgame') # By using the lower() function removes the case and will return true.
print()

# Here we can see some differences using IF statements inside for loops.
foods = ['hot dogs', 'cake', 'salmon', 'Dr. Pepper Burger', 'Sweet N Spicy Burger']
for food in foods:
    if food == 'cake':
        print(food.upper())
    else:
        print(food.title())
print()

# You can also just as easily check for inequality.
requested_age = 19
min_age = 21
ages = [17, 19, 22, 34, 42, 50]

if requested_age != min_age:
    print('The age does not match.')
print()

for age in ages:
    if age <= min_age:
        print(f"You are not old enough. Your age is: {age}. The minimum age is {min_age}!")
    elif age >= min_age:
        print(f'You are {age}, welcome to the club.')
print()

print(ages[0] == 17) # check to see if age is 17.
print()

print(ages[0] < min_age) # checks to see if age is less than min_age
print(ages[0] <= min_age) # checks to see if age is less than or equal to min_age
print(ages[0] > min_age) # checks to see if it is greater that min_age
print(ages[0] >= min_age) # checks to see if it greater than or equal to min_age
print()

print(ages[0] >= min_age and ages[1] >= min_age) # this is a multi condition check. Should return false on both.
print(ages[2] >= min_age and ages[3] >= min_age) # this is a multi condition check. Should return true on both.
print()

# You can check to see if the value is in the list
print(19 in ages) # should return true
print()

# You can also check to see if a user is in the a list too
end_users = ['John', 'Oliver', 'Mary', 'Jim', 'Grace']
temporary_users = ['John', 'Jim']

for user in end_users:
    if user not in temporary_users:
        print(f"{user.title()} is an end user.")
    elif user in temporary_users:
        print(f"{user.title()} is a temporary user.")
print()

# Boolean Expressions are true/false variables that keep track of certain conditions.
overtime_allowed = False
overtime_allowed2 = True
employees_hours = (40, 38, 25, 50, 42, 36)
employees = ('John', 'Oliver', 'Mary', 'Jim', 'Grace', 'Harry')
employee_index = 0
employee_index2 = 0

if overtime_allowed == False:
    for hours in employees_hours:
        if hours > 40:
            print(f'{employees[employee_index].title()} is over 40 hours and not approved.')
            employee_index += 1
        elif hours <= 40:
            print(f'{employees[employee_index].title()} has met their hours.')
            employee_index += 1
print()
if overtime_allowed2 == True:
    for hours in employees_hours:
        if hours > 40:
            print(f'{employees[employee_index2].title()} is over 40 hours and is approved.')
            employee_index2 += 1
        elif hours <= 40:
            print(f'{employees[employee_index2].title()} has met their hours.')
            employee_index2 += 1
print()

# You can also chain if statements
employee_index3 = 0

for hours in employees_hours:
    if hours >= 20:
        print(f'{employees[employee_index3].title()} is at or above 20 hours.')
        #employee_index3 += 1
    if hours <= 40:
        print(f'{employees[employee_index3].title()} is at or below 40 hours.')
        #employee_index3 += 1
    if hours > 40:
        print(f'{employees[employee_index3].title()} is above 40 hours.')
        #employee_index3 += 1
    employee_index3 += 1
print()

# Still using the employees variable here

employee_index4 = 0

for hours in employees_hours:
    if hours >= 20 and hours <= 30:
        print(f'{employees[employee_index4].title()} is a part time worker.')
    if hours > 30 and hours <= 40:
        print(f'{employees[employee_index4].title()} is a full time employee.')
    if hours > 40 and hours <= 50:
        print(f'{employees[employee_index4].title()} is a supervisor.')
    employee_index4 += 1
print()

employee_index5 = 0

for hours in employees_hours:
    if hours >= 20 and hours <= 30:
        print(f'{employees[employee_index5].title()} is a part time worker.')
    if hours > 30 and hours <= 40:
        print(f'{employees[employee_index5].title()} is a full time employee.')
    if hours > 40 and hours <= 50:
        print(f'{employees[employee_index5].title()} is a supervisor.')
    employee_index5 += 1
print()

# Here is another chain example involving hot dogs. Copy this and change the amount of hot dogs to get a different result.
hotdogs = 20

if hotdogs <= 4:
    print("We are almost out of hot dogs for our event.")
elif hotdogs > 25:
    print("We have more hot dogs than people for our event.")
else:
    print("There is just enough hot dogs to feed everyone in our event.")

print()

# You can check to see if a list is not empty

superhero_list = []

if superhero_list:
    for hero in superhero_list:
        print(f'{hero.title()} is on the list.')
    print('That\'s everyone on the list.')
else:
    print('Appears you don\'t have anyone to attend your party.')
print()

# Here you can use multiple lists

superhero_list = ['Batman', 'Robin', 'Superman', 'Spider-Man', 'Iron Man', 'Nightwing', 'Deadpool']
anit_heroes = ['Deadpool']

for hero in superhero_list:
    if hero in anit_heroes:
        print(f'Sorry, but {hero.title()} is not a superhero.')
    else:
        print(f'{hero.title()} is a superhero.')
print()