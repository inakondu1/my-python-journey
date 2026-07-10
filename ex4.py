'''

Challenge 4: The Shipping ContainerA small business is shipping heavy statuettes. 
Each statuette weighs exactly 16 kilograms.First, find the square root of 16 to 
find out how many statuettes fit in a standard row.Next, because of a shipping fee adjustment,
 take that result and round it up to the nearest whole integer (even if it's already a whole
  number!).Expected final output: 4
  '''
import math

root_val = math.sqrt(16)

ceil_val = math.ceil(root_val)
print(ceil_val)