'''
Challenge 5: Precise Cutting ToolAn automated factory blade cuts metal sheets. 
The blueprint says a sheet must be exactly 10.8 inches long. However, 
the machine software has a safety setting that always rounds the number down to the
 nearest whole integer.Write a script that takes 10.8, rounds it down, 
 and prints the result.Expected output: 10
'''


import math

floor_val = math.floor(10.8)
print(floor_val)