#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

## Lab 30, The Larch....err the while loop.
#  Setting variables to default "starting" values.  

round = 0

# Creating while loop.  For 3 rounds of guessing, with special extra guesses answer.

while True:
    round = round + 1

    print('Finish the movie title, "Monty Python\'s The Life of ______"')

    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif answer == 'The Larch':
        print('Nobody expects the Spanish Inquisition!')
        print("Sorry!  Try, Try again!")
        round = round - 1
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else: print("Sorry! Try again!")

