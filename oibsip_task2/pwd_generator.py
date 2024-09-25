#!/usr/bin/env python3
"""
This module provides a simple command-line password generator with error handling.
It generates random passwords based on user-defined criteria such as
length and character types (letters, numbers, symbols), while handling invalid inputs.
"""

# Importing the necessary modules
import random  # For generating random characters
import string  # For accessing different character sets (letters, digits, punctuation)

def get_password_length():
    """
    Get the desired password length from the user with error handling.
    
    Returns:
    int: Desired password length
    """
    while True:  # Loop until valid input is provided
        try:
            # Asking user for password length and converting it to an integer
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:  # Check if length is less than 4
                print("Password length must be at least 4 characters.")  # Inform user of invalid input
            else:
                return length  # Return the valid password length
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle invalid input (non-integer)

def get_yes_no_input(prompt):
    """
    Get a yes/no input from the user with error handling.
    
    Args:
    prompt (str): The prompt to display to the user

    Returns:
    bool: True if user inputs 'y', False if 'n'
    """
    while True:  # Loop until valid input ('y' or 'n') is provided
        user_input = input(prompt).lower()  # Convert input to lowercase
        if user_input in ['y', 'n']:  # Check if the input is either 'y' or 'n'
            return user_input == 'y'  # Return True for 'y' and False for 'n'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")  # Handle invalid input

def get_user_preferences():
    """
    Get user preferences for password generation with error handling.
    
    Returns:
    tuple: (password_length, use_letters, use_numbers, use_symbols)
    """
    length = get_password_length()  # Get password length from the user
    use_letters = get_yes_no_input("Include letters? (y/n): ")  # Ask if letters should be included
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")  # Ask if numbers should be included
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")  # Ask if symbols should be included
    
    return length, use_letters, use_numbers, use_symbols  # Return user preferences

def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    Generate a random password based on user preferences.
    
    Args:
    length (int): Desired password length
    use_letters (bool): Include letters in the password
    use_numbers (bool): Include numbers in the password
    use_symbols (bool): Include symbols in the password

    Returns:
    str: Generated password
    """
    character_set = ''  # Initialize an empty character set
    if use_letters:
        character_set += string.ascii_letters  # Add letters to the character set if selected
    if use_numbers:
        character_set += string.digits  # Add numbers to the character set if selected
    if use_symbols:
        character_set += string.punctuation  # Add symbols to the character set if selected

    if not character_set:  # If no character type is selected
        return "Error: No character set selected. Please include at least one character type."

    # Randomly select characters from the character set to form the password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password  # Return the generated password

def main():
    """
    Main function to run the password generator with error handling.
    """
    print("Welcome to the Password Generator!")  # Greeting message
    
    while True:  # Keep running until the user chooses to exit
        # Get user preferences for the password
        length, use_letters, use_numbers, use_symbols = get_user_preferences()
        # Generate the password based on user preferences
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        # If an error message is returned, display it and continue
        if password.startswith("Error"):
            print(password)
            continue
        
        # Display the generated password
        print(f"Your generated password is: {password}")
        
        # Ask if the user wants to generate another password
        if not get_yes_no_input("Do you want to generate another password? (y/n): "):
            print("Thank you for using the Password Generator. Goodbye!")  # Farewell message
            break  # Exit the program

# Ensures the script runs only if it's executed directly (not imported as a module)
if __name__ == "__main__":
    main()