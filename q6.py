'''
Challenge 5: Evens and Odds (Loops + If/Else)

Let's write a program that counts from 1 to 6, but tells us whether each number 
is Even or Odd.

How to check if a number is even or odd in Python:
We use the modulo operator (%), which finds the remainder of a division.

    If a number divided by 2 has a remainder of 0 (number % 2 == 0), it is Even.

    Otherwise, it is Odd.

Your Goal:
Write a program that prints this exact output:
'''
number = 1

while number <= 6:
    if number % 2 == 0:
        print(number, 'even number')
    else:
        print(number, 'odd number')
    
    # We add 1 at the very end of each turn
    number = number + 1