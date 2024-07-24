import random

def roll_dice(num_sides, num_rolls):
    print("Rolling", num_rolls, "dice with", num_sides, "sides:")
    for roll in range(num_rolls):
        result = random.randint(1, num_sides)
        print("Roll", roll + 1, ":", result)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            num_rolls = int(input("Enter the number of rolls: "))
            if num_sides <= 0 or num_rolls <= 0:
                raise ValueError("Number of sides and rolls must be greater than 0.")
            break
        except ValueError as ve:
            print("Invalid input:", ve)
    
    roll_dice(num_sides, num_rolls)

if __name__ == "__main__":
    main()
