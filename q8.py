'''Challenge 7: The Security Guard (Password Loop)

Imagine you are writing the code for a phone lock screen. The phone is locked, and the program must keep asking for the password until the user types the correct one.

Your Goal:
Write a program that keeps asking the user to enter a password.

    If they type the wrong password, it should tell them "Incorrect password. Try again!" and ask them again.

    If they type the correct password (let's make the correct password "python123"), it should print "Access Granted!" and stop the program.

Your clues & structure:

    The Secret: Set a variable correct_password = "python123".

    The Guess: Start a variable called user_guess and set it to an empty string "" so we have something to compare.

    The Loop: Start a while loop that runs while the user_guess is not equal to the correct_password.

        Note: In Python, "not equal to" is written as !=.

    Inside the Loop:

        Ask the user for their guess using input().

        Use an if statement: if their guess is not the correct one, print the error message.

    Outside the Loop:

        Print "Access Granted!" (This will only run once they finally type the correct password and break out of the loop!).
        '''

password = 'python123'

user_guess = ""

while user_guess != password:
    user_guess = input("Enter the password: ")
    

    if user_guess == password:
    
        print('access granted')
    else:
        print('invalid password: try again. ')



