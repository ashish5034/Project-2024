import random

def choose_word():
    word_list = ["python", "hangman", "computer", "programming", "game", "developer", "challenge"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while True:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect!")
        
        print("Attempts left:", attempts)
        print(display_word(word, guessed_letters))
        
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break
        
        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", word)
            break
        
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()

if __name__ == "__main__":
    hangman()
