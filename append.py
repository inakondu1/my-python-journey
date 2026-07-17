'''
lasswork 2: Updating the Temperature Dataset

Imagine you are collecting room temperature data over a few hours to
 train an AI thermostat. You start with a list of recorded temperatures
  (in degrees Celsius).

Here is your starting list:
Python

temps = [15, 18, 20, 22]

Your Task:
Write a Python script that does the following:

    Create the temps list.

    A new temperature reading of 24 degrees just came in.
     Append this new temperature to the end of your list.

    You notice the second temperature in your list (18) was recorded incorrectly. 
    It was actually 19 degrees. Change that value in the list to 19.

    Print the final list to the screen so we can see the updated data.

    Print the new total number of readings in your list using len()
    '''
temps = [15, 18, 20, 22]
temps.append(24)
temps[1] = 19
print(temps)
print(len(temps))