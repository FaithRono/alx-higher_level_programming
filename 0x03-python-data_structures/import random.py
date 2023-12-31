import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Ensure the upper bound is greater than the lower bound
    while upper_bound <= lower_bound:
        print("Upper bound must be greater than the lower bound.")
        upper_bound = int(input("Enter the upper bound of the range: "))
    
    print(f"Think of a number between {lower_bound} and {upper_bound}.")
    input("Press Enter when you're ready...")

    feedback = ''
    while feedback != 'c':
        guess = random.randint(lower_bound, upper_bound)
        print(f"Is your number {guess}?")
        feedback = input("Enter 'H' if the guess is too high, 'L' if too low, or 'C' if correct: ").upper()

        if feedback == 'H':
            upper_bound = guess - 1
        elif feedback == 'L':
            lower_bound = guess + 1

    print(f"The computer guessed your number, {guess}, correctly!")

# Start the game
guess_number()
