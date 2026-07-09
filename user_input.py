


''' Topic 2: Dynamic Math (Handling User Input)In real software, 
numbers are rarely fixed. We usually get numbers from users
 (like your tip calculator example).As you learned earlier, input() takes everything 
 as text (a string). To do calculations, you must wrap the input inside 
 a conversion tool:int() changes text into a whole number (integer)
  like 5 or 60.float() changes text into a decimal number (floating-point) 
  like 19.99 or 5.0.

  Your ChallengeLet's build a dynamic Hourly Wage Calculator.
  Write a script that:Asks the user for their hourly wage 
  (e.g., 25.50) using input().Asks the user for the number of hours they worked this week
   (e.g., 40) using input().Calculates their total weekly earnings.Prints the result.
  '''
hourly_wage = float(input('input your hourly wage: '))

numbers_work = int(input('numbers of hours worked this week: '))

total_input = hourly_wage * numbers_work 

print(total_input)