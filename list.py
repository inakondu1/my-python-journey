'''
magine you are preparing data to train a machine learning model that 
predicts house prices. You have a list of house prices (in thousands of dollars)
 recorded from a local neighborhood.

Here is your list:
Python

prices = [120, 340, 250, 80, 500, 210]

Your Task:
Write a Python script that does the following:

    Create the prices list.

    Find the total number of houses in your dataset using len() and print it.

    Print the price of the very first house in the list.

    Print the price of the fifth house in the list (be careful with the computer's
     counting rule!).

    Bonus Challenge: Calculate the sum of the first house and the last house in the 
    list, and print the result.
    '''
price = [120, 340, 250, 80, 500, 210]
total_number = len(price)
print(total_number)
print(price[0])
print(price[4])
sum = price[0] + (price[5])
print(sum)


