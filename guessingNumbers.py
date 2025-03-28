import random

secret_number = 9 # Set the secret_number variable here (between 1 and 10)
guess = 0
 #Initialize the guess variable here with a value of 0

while guess not secret_number: # Add the while loop condition here
	guess = int(input("guess the secret_number:"))
	print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)