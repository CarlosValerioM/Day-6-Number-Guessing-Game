#!/usr/bin/env python3
"""
numberGuessingGame.py - A simple number guessing game.

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/08
License: MIT
Dependencies: None (built-in functions only)

Description:
This script is a number guessing game where the user has to guess a randomly generated number between 1 and 100.
It takes the following user input:
1. The user's guess for the number.

The script provides feedback on whether the guess is too low, too high, or correct.
The game continues until the user guesses the correct number and displays the number of attempts taken.

Usage:
Run the script and follow the prompts:
    python numberGuessingGame.py

Example Output:
    Welcome to the Number Guessing Game!
    I have selected a number between 1 and 100. Try to guess it.
    Enter your guess: 50
    Too low!
    Enter your guess: 75
    Too high!
    Enter your guess: 62
    Congratulations! You guessed the number.
"""
import random  # Import the random module to generate a random number.

# Function to compare the user's guess with the randomly generated number.
def compareNumber(randomNumber, numberGuess):
    if randomNumber == numberGuess:  # If the guessed number matches the random number
        print(f"Congratulations! You won! The number is: {randomNumber}")
        return True  # Return True to indicate the correct guess
    elif randomNumber > numberGuess:  # If the guessed number is too low
        print(f"{numberGuess} is too low!")
        return False  # Return False to continue the game
    elif randomNumber < numberGuess:  # If the guessed number is too high
        print(f"{numberGuess} is too high!")
        return False  # Return False to continue the game
    else:  # This condition will never be reached, but it's a safeguard
        print("ERROR, try again.")

# Main function to run the game
def main():
    randomNumber = random.randint(0, 500)  # Generate a random number between 0 and 500
    guessed = False  # Variable to track if the number has been guessed correctly

    while not guessed:  # Loop until the correct number is guessed
        numberGuess = int(input("Guess the number: "))  # Get user's guess as an integer
        guessed = compareNumber(randomNumber, numberGuess)  # Check if the guess is correct

# Ensures the script runs only if it's executed directly, not imported as a module
if __name__ == '__main__':
    main()