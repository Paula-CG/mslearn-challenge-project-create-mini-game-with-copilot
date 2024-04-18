# write code that plays rock, paper, scissors with the user
# first, ask the user to input their choice
# then, randomly generate a choice for the computer (rock, paper, or scissors)
# finally, determine the winner of the game
# print the result of the game to the console
# if the user wants to play again, repeat the process
# if the user does not want to play again, print "Goodbye!" to the console
# keep track of how many times the user wins
# use the input() function to get the user's choice
# use the random.choice() function to generate a random choice for the computer
# use a while loop to keep playing the game until the user decides to stop
# use an if statement to determine the winner of the game
# use a dictionary to store the possible choices for the game
# use the break statement to exit the loop if the user decides to stop playing
# use the print() function to display the result of the game to the console
# use the print() function to display "Goodbye!" to the console when the user decides to stop playing

# Main entry point of the program
if __name__ == "__main__":
    # Import the random module
    import random

    # Define the possible choices for the game
    choices = ["rock", "paper", "scissors"]
    # Define the number of times the user wins
    user_wins = 0

    # play the game until the user decides to stop
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # check if the user's choice is valid
        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # randomly generate a choice for the computer
        computer_choice = random.choice(choices)

        # determine the winner of the game
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")

            # increment the number of times the user wins
            user_wins += 1
        else:
            print("You lose!")

        while True:
            # ask the user if they want to play again
            play_again = input("Do you want to play again? (yes or no): ").lower()

            # if the user didn't enter "no" or "yes", print an error message
            if play_again != "no" and play_again != "yes":
                print("Invalid choice. Please enter yes or no.")
                continue
            else:
                break

        # exit the loop if the user decides to stop playing
        if play_again != "yes":
            # print the number of times the user wins
            print(f"You won {user_wins} time{'s' if user_wins != 1 else ''}.")
            print("Goodbye!")
            break
