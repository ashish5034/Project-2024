import random as rd

# *********************************************************************************************************
# import random: This line imports the random module, which is used to generate random choices for the computer's selection.
# *********************************************************************************************************

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

# *********************************************************************************************************
# def determine_winner(user_choice, computer_choice):: This line defines a function named determine_winner that takes two parameters: user_choice and computer_choice. This function determines the winner of the game based on the choices made by the user and the computer.

# if user_choice == computer_choice:: This line checks if the user's choice is the same as the computer's choice. If they are equal, it returns "It's a tie!".

# elif (user_choice == 'rock' and computer_choice == 'scissors') or \: This line checks for various combinations where the user wins: rock beats scissors, paper beats rock, and scissors beat paper.

# else:: This line handles the case where none of the above conditions are met, which means the user loses the game.
# *********************************************************************************************************

def main():
    choices = ['rock', 'paper', 'scissors']
    play_again = 'yes'

# *********************************************************************************************************
# def main():: This line defines the main function of the program where the game logic is implemented.

# choices = ['rock', 'paper', 'scissors']: This line creates a list containing the possible choices for the game: rock, paper, and scissors.

# play_again = 'yes': This line initializes the variable play_again to 'yes', indicating that the user wants to play the game at least once.
# *********************************************************************************************************

    while play_again.lower() == 'yes':
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in choices:
            print("Invalid choice. Please enter either rock, paper, or scissors.")
            continue
        
        computer_choice = rd.choice(choices)

# *********************************************************************************************************
# while play_again.lower() == 'yes':: This line starts a while loop that continues as long as the user wants to play again. The .lower() method is used to convert the input to lowercase to handle cases where the user enters 'Yes' or 'YES' instead of 'yes'.

# user_choice = input("Enter your choice (rock, paper, scissors): ").lower(): This line prompts the user to enter their choice (rock, paper, or scissors) and stores it in the user_choice variable. The .lower() method is used to convert the input to lowercase for consistency.

# if user_choice not in choices:: This line checks if the user's choice is not one of the valid options. If it's not, it prints a message informing the user of the invalid choice and continues to the next iteration of the loop using the continue statement.

# computer_choice = random.choice(choices): This line randomly selects an item from the choices list to represent the computer's choice.
# *********************************************************************************************************
        
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

# *********************************************************************************************************
# play_again = input("Do you want to play again? (yes/no): "): This line prompts the user to decide whether they want to play the game again. The user's input is stored in the play_again variable.
# *********************************************************************************************************

        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    main()
