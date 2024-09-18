#!/usr/bin/env python3
"""
This module provides a simple command-line password generator.

It generates random passwords based on user-defined criteria such as
length and character types (letters, numbers, symbols).
"""

import random
import string

def get_user_preferences():
    """
    Get user preferences for password generation.

    Returns:
    tuple: (password_length, use_letters, use_numbers, use_symbols)
    """
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
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
        return "Error: No character set selected"

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    """
    Main function to run the password generator.
    """
    print("Welcome to the Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()