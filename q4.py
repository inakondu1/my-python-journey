'''
Write a program that counts down from 5 down to 1, and then prints "Blast off!"
 at the very end.

Your clues for this one:

    The Start: Start your variable at 5.

    The Condition: You want to keep looping while your variable is greater than 0 (> 0).

    The Step: Instead of adding, you need to subtract 1 each time 
    (number -= 1 or number = number - 1).

Give this a try in your editor, see if you can get it to count backwards,
 and paste your code when you are ready!
 '''
data = 5

while data >= 0:
    print(data)

    data = data - 1
print('Blast off!')

