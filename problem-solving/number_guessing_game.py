# # Number Guessing Game

# Create a Python console-based number guessing game.

# The program should have a secret number:

# ```python
# secret_number = 73
# ```

# The player must try to guess the secret number.

# ### Game Rules

# * The player has a maximum of **7 valid attempts**.
# * If the player's guess is greater than the secret number, display:

# ```text
# Too High
# ```

# * If the player's guess is smaller than the secret number, display:

# ```text
# Too Low
# ```

# * If the player guesses the correct number, display:

# ```text
# Correct!
# ```

# and show the number of attempts used.

# * If the player uses all 7 attempts without guessing correctly, display:

# ```text
# Game Over!
# The number was 73.
# ```

# ### Input Validation

# The program must handle invalid input correctly.

# A guess is considered invalid if:

# * The user enters something that is not an integer.
# * The user enters a number outside the range `1–100`.

# Invalid inputs **must not count as attempts**.

# The program should continue asking the user for a valid guess.

# ### Requirements

# * Use a `while` loop as the main game loop.
# * Track the number of valid attempts.
# * Do not allow more than 7 valid attempts.
# * Validate the user's input.
# * The game should stop immediately when the correct number is guessed.
# * The game should end when the player reaches the maximum number of valid attempts.

# ### Example

# ```text
# Guess the number (1-100): 50
# Too Low

# Guess the number (1-100): 90
# Too High

# Guess the number (1-100): 73
# Correct!
# You won in 3 attempts.
# ```

import random

secret_number = random.randint(1, 100)

i = 0
guess = 0

print ("Welcome to the Number Guessing Game!\n"
"Try to guess the secret number between 1 and 100.\n")


while guess != secret_number and i < 7 :
    guess = input("Enter your guess from 1 to 100 : \n"
    "( you have only 7 Attempts)  ")

    if not guess.isdigit() :
        print("\nit must be integer\n")
        continue

    guess = int(guess)
    
    if guess < 1 or guess > 100 :

        print("\nit must be between 1 to 100\n")
        continue

    else :

        if guess > secret_number :
            print("\nToo High\n")
            i+=1

        elif guess < secret_number :
            print("\nToo Low\n")
            i+=1
            
        else :
            print("\nYou are right !\n")
            print(f"You won in {i+1} attempts.")
            break

else :
    print("\nGame Over!")
    print(f"The number was {secret_number}.")