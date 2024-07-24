import random as rd
import string as str

# *********************************************************************************************************
# import random : This imports the rd module, which contains functions for generating rd numbers.
# import string: This imports the str module, which contains various str constants and functions.
# *********************************************************************************************************

def generate_password(length):
    # Define the characters to use for generating the password
    characters = str.ascii_letters + str.digits + str.punctuation

# *********************************************************************************************************
# def generate_password(length):: This defines a function named generate_password that takes one parameter length, which specifies the desired length of the password.

# characters = str.ascii_letters + str.digits + str.punctuation: This concatenates three str constants from the str module: str.ascii_letters (lowercase and uppercase letters), str.digits (digits 0-9), and str.punctuation (common punctuation characters).
# *********************************************************************************************************
 
    # Generate the password
    password = ''.join(rd.choice(characters) for _ in range(length))
    
    return password

# *********************************************************************************************************   
#  password = ''.join(rd.choice(characters) for _ in range(length)): This line generates the password. It uses a generator expression within the join() method to randomly choose characters from the characters string length times. The random.choice() function randomly selects a character from the characters string each time it's called. The join() method then concatenates these randomly chosen characters into a single string.
# return password: This line returns the generated password
# *********************************************************************************************************
  
def main():
    print("Random Password Genereator By Ashish Mahamuni")
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
