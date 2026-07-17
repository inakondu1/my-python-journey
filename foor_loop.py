'''
Write a Python script using a for loop that does the following:

    Create the bills list.

    Use a for loop to look at each bill one by one.

    Inside the loop, multiply each bill by 2 (maybe energy prices doubled this month!)
     and print out the new amount.

Your output on the screen should look something like this:
Plaintext

New bill: 100
New bill: 160
New bill: 220
New bill: 140

Keep your indentation in mind for the code inside the loop. Paste your code here 
whenever you are ready!Write a Python script using a for loop that does the following:

    Create the bills list.

    Use a for loop to look at each bill one by one.

    Inside the loop, multiply each bill by 2 (maybe energy prices doubled this month!) and print out the new amount.

Your output on the screen should look something like this:
Plaintext

New bill: 100
New bill: 160
New bill: 220
New bill: 140

Keep your indentation in mind for the code inside the loop. Paste your code here whenever you are ready!

'''
bills = [50, 80, 110, 70]

for x in bills:
    new_bill = x * 2  # Keeps our 'bills' list safe!
    print(f"New bill: {new_bill}")