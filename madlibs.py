def mad_libs_game():
    print("Welcome to the Complex Mad Libs Game!")
    play_again = 'yes'

    while play_again.lower() in ('yes', 'y'):
        # Prompts for different types of words
        adjective = input("Enter an adjective: ")
        animal = input("Enter an animal: ")
        verb = input("Enter a verb (past tense): ")
        adverb = input("Enter an adverb: ")
        noun = input("Enter a noun: ")
        place = input("Enter a place: ")
        celebrity = input("Enter a celebrity: ")

        # Story template with placeholders
        story = f"Once upon a time, there was a {adjective} {animal} that {verb} {adverb} through the {noun}. " \
                f"It arrived at {place} and met {celebrity}, who exclaimed, 'Wow, you are one adventurous {animal}!'"

        # Display the completed story
        print("\nYour Mad Libs story:")
        print(story)

        play_again = input("\nDo you want to play again? (yes/no): ")

    print("\nThanks for playing Mad Libs!")

# Run the Mad Libs game
mad_libs_game()
