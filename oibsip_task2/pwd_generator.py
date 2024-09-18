#!/usr/bin/env python3
"""
This module provides a simple command-line password generator with error handling.

It generates random passwords based on user-defined criteria such as
length and character types (letters, numbers, symbols), while handling invalid inputs.
"""

import random
import string

def get_password_length():
    """
    Get the desired password length from the user with error handling.

    Returns:
    int: Desired password length
    """
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                print("Password length must be at least 4 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_yes_no_input(prompt):
    """
    Get a yes/no input from the user with error handling.

    Args:
    prompt (str): The prompt to display to the user

    Returns:
    bool: True if user inputs 'y', False if 'n'
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def get_user_preferences():
    """
    Get user preferences for password generation with error handling.

    Returns:
    tuple: (password_length, use_letters, use_numbers, use_symbols)
    """
    length = get_password_length()
    use_letters = get_yes_no_input("Include letters? (y/n): ")
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")
    
    return length, use_letters, use_numbers, use_symbols

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
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "Error: No character set selected. Please include at least one character type."

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    """
    Main function to run the password generator with error handling.
    """
    print("Welcome to the Password Generator!")
    
    while True:
        length, use_letters, use_numbers, use_symbols = get_user_preferences()
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password.startswith("Error"):
            print(password)
            continue
        
        print(f"Your generated password is: {password}")
        
        if not get_yes_no_input("Do you want to generate another password? (y/n): "):
            print("Thank you for using the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()