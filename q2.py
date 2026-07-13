'''
Challenge 2: The Age Calculator (Data Types & Math)

By default, everything a user types into an input() function comes into Python as 
a string (text). This challenge tests how you convert that text into a number
 so you can do math with it.

Your Goal:
Write a Python script that does the following:

    Ask the user what year they were born.

    Calculate how old they will turn by the end of this year (2026).

    Print a message telling them their age. For example: "You will turn 29 years old 
    this year!"
year = (input('what year where you born?: '))
born = 2026 - int(year)
print(f'you will become {born} years old this year')
Tips to remember:

    You will need to convert the user's input from a string to an integer
     (whole number) using int().

    The math formula will be: 2026 - birth_year.

Give it a shot, paste your code when you're done, and we'll see how it goes!
'''

year = (input('what year where you born?: '))
born = 2026 - int(year)
print(f'you will become {born} years old this year')