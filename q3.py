'''

Challenge 3: The Movie Night Gatekeeper (Conditionals)

In the real world, programs need to make decisions based on data.
 This challenge tests how you use if, elif, and else to send a user down different paths.

Your Goal:
Write a Python script that simulates a movie theater's age restriction gatekeeper:

    Ask the user for their age (don't forget to convert it to an integer!).

    If they are 18 or older, print: "Enjoy the movie! Here is your ticket."

    If they are under 18, print: "Sorry, you must be 18 or older to watch this movie."

Tips to remember:

    Use if and else.

    Remember to use the greater-than-or-equal-to symbol (>=) to check if they are
     18 or older.

    Don't forget the colons (:) at the end of your if and else lines, and indent the 
    print statements underneath them!

Take your time with this one, type it out, and let me see your solution when 
you're ready!
'''

age = 18
user = (int(input('how old are you?  ')))
if user >= int(18):

    print(f'Enjoy the movie: here is your ticket')

else:
    print(f'sorry, you must be {age} or older to watch this movie')