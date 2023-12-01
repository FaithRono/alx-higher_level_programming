import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    guess_again = 'yes'
    
    while guess_again.lower() in ('yes', 'y'):
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
    
        # Ensure the upper bound is greater than the lower bound
        while upper_bound <= lower_bound:
            print("Upper bound must be greater than the lower bound.")
            upper_bound = int(input("Enter the upper bound of the range: "))
    
        print(f"Think of a number between {lower_bound} and {upper_bound}.")
        input("Press Enter when you're ready...")

        feedback = ''
        while feedback != 'c' and feedback != 'stop':  # Added 'stop' condition
            guess = random.randint(lower_bound, upper_bound)
            print(f"Is your number {guess}?")
            feedback = input("Enter 'H' if the guess is too high, 'L' if too low, 'C' if correct, or 'stop' to end the game: ").upper()

            if feedback == 'H':
                upper_bound = guess - 1
            elif feedback == 'L':
                lower_bound = guess + 1

        if feedback == 'stop':
            break  # Exit the game loop if 'stop' is entered

        print(f"The computer guessed your number, {guess}, correctly!")
        guess_again = input("\nDo you want to play again? (yes/no): ").lower()

    print("\nThanks for playing GUESS NUMBER!")

# Start the game
guess_number()
