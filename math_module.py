

'''
Let's use the math module to find the hypotenuse of a right-angled triangle using 
the Pythagorean theorem (\(a^2 + b^2 = c^2\)). To find \(c\), 
the formula is: \(\sqrt{a^{2}+b^{2}}\).Write a script that:
Implements import math at the top.Sets side a = 3 and side b = 4.
Calculates the sum of their squares (\(a^2 + b^2\)) using the exponent operator (**).
Uses math.sqrt() to find the square root of that sum.Prints the final hypotenuse result.
'''
import math

a = 3
b = 4

calculatea = a ** 2
calculateb = b ** 2  # Fixed: Changed the variable name to calculateb

# 2. This line now works perfectly!
sum_of_squares = calculatea + calculateb 

# 3. Find the square root
root_val = math.sqrt(sum_of_squares)

print(root_val)
