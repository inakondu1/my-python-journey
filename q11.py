'''
Challenge 9: The Smart Thermostat 🌡️

You are writing the software for a smart heater. The heater is turned off,
 and the room temperature starts at 15 degrees.
You want the heater to keep running and heating up the room until it reaches
 your target temperature of 22 degrees.

Your Goal:
Write a program that produces an output like this:
The room is currently 15 degrees.
How many degrees should we heat it up by? 3
The room is now 18 degrees.

How many degrees should we heat it up by? 2
The room is now 20 degrees.

How many degrees should we heat it up by? 2
The room is now 22 degrees.Challenge 9: The Smart Thermostat 🌡️

You are writing the software for a smart heater. The heater is turned off, and the room temperature starts at 15 degrees.
You want the heater to keep running and heating up the room until it reaches your target temperature of 22 degrees.

Your Goal:
Write a program that produces an output like this:


Target reached! Turning off the heater.
'''


room = 15

while room < 22 :
    add = input('how many degree should we heat it up by: ')
    room = room + int(add)

print(f'total reached! {room} Turning off the heater')
