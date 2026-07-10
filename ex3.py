'''


Challenge 3: The Budget AppAn app calculates that a user spent 25.99 dollars.
 The app design requires stripping away the cents completely by rounding the number down 
 to the nearest whole integer. Write a script to do this.Expected output: 25
 '''
import math

floor_val = math.floor(25.99)

print(floor_val)