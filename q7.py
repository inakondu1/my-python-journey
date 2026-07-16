
'''Challenge 8: The Security Gate (PIN Code Access)

This is very similar to the password lock, but this time, we are using a numeric PIN code (like on an ATM).

Your Goal:
Write a program that protects a bank account.

    The correct PIN is 1998 (which is an integer).

    The program must keep asking the user to enter their 4-digit PIN.

    If they enter the wrong PIN, print: "Wrong PIN. Try again!" and let the loop run again.

    If they enter the correct PIN, print: "Pin accepted. Welcome to your account!" and stop the loop.

Your clues & structure:

    The Secret PIN: Set correct_pin = 1998.

    The User's Guess: Start a variable user_guess = 0.

    The Loop: Run a while loop that keeps going while user_guess is not equal to correct_pin (while user_guess != correct_pin:).

    Inside the Loop:

        Ask the user to input their PIN. Remember to convert this input to an integer using int(), since PINs are numbers!

        Put an if statement inside the loop: if user_guess != correct_pin, print the "Wrong PIN. Try again!" message.
'''


correct_pin = 1998
user_guess = 0

while user_guess != correct_pin:
    user_guess = int(input('enter your pin: '))

    if user_guess == correct_pin:
        print('access granted')
    else:
        print('Wrong PIN. Try again!')