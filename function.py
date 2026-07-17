'''
Let's combine your new knowledge of functions with the loop logic you just mastered. 
You are going to build a reusable function that calculates the total energy used from 
any list of data we give it.

Your Task:
Write a Python script that does the following:

    Define the function: Use def to create a function called calculate_total.
     It should accept one parameter (input) called dataset.

    Inside the function:

        Create a tracker variable named calculate_totaltotal and set it to 0.

        Use a for loop to go through the dataset.

        Add each number to your total tracker.

        After the loop finishes, use the return keyword to send the final total back out.

    Test the function:

        Outside of the function, create this list of data: july_energy = [10, 20, 15, 30]

        Call your function by passing july_energy into it, save the returned answer 
        into a variable named result, and print it out!
        '''

def calculate_total(dataset):
    total = 0
    for number in dataset:
        total = total + number
    return total

# --- Outside the function now ---
july_energy = [10, 20, 15, 30]
result = calculate_total(july_energy)
print(f"The total energy is: {result}")