

#how many degree should we heat it up by: e
room = 15

while room < 22:
    add = input('how many degree should we heat it up by: ')
    room = room + int(add)

    # 1. Check inside the loop if they went over 22
    if room > 30: 
        print('too high, reduce it to below 30 and above 22 degrees')
        remove = input('how many do you want to reduce it by: ')
        room = room - int(remove)
        print(f'it has been reduced, it is now {room}')
        
    # 2. If they didn't go over, just show the progress
    else:
        print(f'The room is now {room} degrees.\n')

# 3. This runs ONLY when the loop is completely done and we are safely at 22
print(f'total reached! {room} Turning off the heater')