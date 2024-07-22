#Day 2: 30 days of Python Programming
"""
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
"""

first_name = 'Federico'
last_name = 'Hayes'
full_name = 'Federico Hayes Tronfi'
country = 'Argentina'
city = 'Caba'
age = 22
year = 2024
is_married = False
is_true = True
is_light_on = False

first_name, last_name, age, country, city = 'Federico', 'Hayes', 22, 'Argentina', 'Caba' 

print(first_name, last_name, age, country, city)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)

print("\n")

"""
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division
"""

#pongo pocos porque despues el tipo de dato se repite
print(type(full_name))
print(type(country))
print(type(age))
print(type(is_married))

print('\n')

print(len(first_name))

print("\n")

print(len(first_name), len(last_name))

print("\n")

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

print('\n')

diff = num_two - num_one
print(diff)

print('\n')

product = num_one * num_two
print(product)

division = num_one/num_two
print(division)

reminder = num_two % num_one
print(reminder)

exp = num_one ** num_two
print(exp)

floor_division = num_one//num_two
print(floor_division)

"""
The radius of a circle is 30 meters.
    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.
"""

circle_radius = 30

area_of_circle = 3.14 * 30**2
print(area_of_circle)

circum_of_circle = 2 * 3.14 * 30
print(circum_of_circle)

rad = float(input("¿Cual es el radio del circulo? "))
area_of_circle_rad = 3.14 * rad**2
print(area_of_circle_rad)

"""
Use the built-in input function to get first name, last name, country and age from a user and store the 
value to their corresponding variable names Run help('keywords') in Python shell or in your file to 
check for the Python reserved words or keyword
"""

firstName = input("¿Cual es tu nombre? ")
lastName = input("¿Cual es tu apellido? ")
country2 = input("¿De que pais eres? ")
age2 = input("¿Cual es tu edad? ")

print("El nombre es: ", firstName)
print("El apellido es: ", lastName)
print("El pais es: ", country2)
print("La edad es: ", age2)

help('keyword')