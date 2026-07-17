'''
Imagine you have a list representing the daily energy consumption 
(in kilowatt-hours, or kWh) of a building over 5 days. You need to find out the 
total energy used across all 5 days.

Here is your dataset:
Python

energy_used = [12, 15, 10, 18, 14]

Your Task:
Write a Python script that does the following:

    Create the energy_used list.

    Create a tracker variable named total_energy outside the loop and set it to 0.

    Use a for loop to go through the energy_used list.

    Inside the loop, add each daily number to your total_energy tracker.

    Outside the loop (after it is completely finished running), print the final
     total with a clean message like: "The total energy used is: [result] kWh".

Watch your indentation carefully so the final print statement waits until
 the loop is totally done! Paste your code here when you're ready.
 '''
energy_used = [12, 15, 10, 18, 14]

total_energy = 0
for name in  energy_used:

    total_energy = total_energy + name

print(f"The total energy used is: {total_energy}")
