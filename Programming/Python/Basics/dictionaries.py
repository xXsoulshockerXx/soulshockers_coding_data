"""
Dictionaries

Using dictionaries will allow you to connect pieces of related information. By utilizing dictionaries, you can store almost limitless amount of information.
"""

# A simple dictionary can store informaion about a particular instance or subject.

employee_0 = {
    'name': 'Jerry',
    'age': 25,
    'position': 'sales'
}

# to access information in the dictionary

print(employee_0['age'])
print()

# Dicitinaries are dynamic and you can add to it at any time.

employee_0['working_days'] = 'Monday, Wednesday, Friday'
print(employee_0)
print()

# you can create an empty one and modify it that way too

employee_1 = {}

employee_1['name'] = 'Jim'
employee_1['age'] = 32
employee_1['position'] = 'maintenance'
employee_1['working_days'] = 'Third Shift'

print(employee_1)
print()

# You can also get keys and values separately.
print('Employee 1 Keys:')
for employee_1_key in employee_1.keys():
    print(employee_1_key)

print()

print('Employee 1 Values:')
for employee_1_value in employee_1.values():
    print(employee_1_value)

print()

# You can also delete information you no longer need

del employee_1['working_days']

print(employee_1)
print()

# Now because we deleted working_days key pair, if you try to call for it, the program will error out. So here is how you deal with it.

print(employee_1.get('working_days', 'No days assigned.')) # using .get() will check to see if it exists and copy the value, if not then it will display a message.
print()

# Individual dictionaries contain a variety of information but can't hold information for other dictionaries. So we create a list and hold the dictionaries in.

employee_list = []

# make two temp employees
for employee_number in range(2):
    new_employee = {'position': 'temp', 'working_days': 'Tuesday Thursday Saturday'}
    employee_list.append(new_employee)

# make two full time employees
for employee_number in range(2):
    new_employee = {'position': 'full-time', 'working_days': 'Monday Tuesday Wednesday Thursday Friday Saturday'}
    employee_list.append(new_employee)

# show employees
for employees in employee_list:
    print(employees)

print()

# show how many employees there are
print(f"Total number of employees: {len(employee_list)}")
print()

# By doing this, we can modify the list in sections we want. In this case, let's promote our temp works to part-time workers

for employees in employee_list:
    if employees['position'] == 'temp':
        employees['position'] = 'part-time'
        employees['working_days'] = 'Monday Wednesday Friday'
    print(employees)

print()

# List inside a dictionary

employee_2 = {
    'name': 'Justin',
    'age': 25,
    'position': 'manager',
    'shift': 'second',
    'working_days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
}
print(f"Employee: {employee_2['name']}")
print(f"Age: {employee_2['age']}")
print(f"Position: {employee_2['position']}")
print()
print('Employee days of work:')
for employee_2_days in employee_2['working_days']:
    print(f"\t{employee_2_days}")

print()

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #
# Dictionary inside of a Dictionary
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@ #

employees_dictionary = {
    "greg": {
        'age': 32,
        'position': 'manager',
        'shift': 'second',
        'working_days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    },
    "jessie": {
        'age': 25,
        'position': 'employee',
        'shift': 'third',
        'working_days': ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday']
    }
}

for dictionary_employee, dictionary_employee_info in employees_dictionary.items():
    print(f'Employee Name: {dictionary_employee.title()}')
    print(f"\n\tPosition: {dictionary_employee_info['position'].title()}")
    print(f"\n\tCurrent shift: {dictionary_employee_info['shift'].title()}")
    
    print('\n\tWorking Days:')
    for day_working in dictionary_employee_info['working_days']:
        print(f'\t\t{day_working.title()}')

    print()

