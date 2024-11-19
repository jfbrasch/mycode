#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Lab 29 Challenge (step 10), 
		A program that prompts a user for a numeric score, then returns the letter grade associated with that score.
		A (100 to 90)
		B (89 to 80)
		C (79 to 70)
		D (69 to 60)
		F (59 and below)"""


message = 'Your letter grade is a'

# wrap grade in a float() to accept any number
grade = float(input("What was your numeric score?"))

#if input value determine letter grade.
if grade >= 90:
     message = message + "n A."
elif grade >= 80:
     message = message + " B."
elif grade >= 70:
     message = message + " C."
elif grade >= 60:
     message = message + " D."
else:
     message = message + "n F."

print(message)

