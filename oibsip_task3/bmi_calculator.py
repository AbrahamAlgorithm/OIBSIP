#!/usr/bin/env python3
"""
This module provides a BMI (Body Mass Index) calculator with user interaction.

It will calculate the BMI based on user input for weight and height,
and categorizes the result into standard health ranges.
"""

def calculate_bmi(weight, height):
    """
    Calculate the BMI given weight and height.

    Args/Params:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: Calculated BMI rounded to two decimal places
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def categorize_bmi(bmi):
    """
    This function categorize the BMI into standard health ranges.

    Args/Params:
    bmi (float): Calculated BMI value

    Returns:
    str: BMI category (Underweight, Normal Weight, Overweight, or Obesity)
    """
    if bmi < 16.0:
        return "underweight (Severe Thinness)"
    elif 16.0 <= bmi < 17.0:
        return "underweight (Moderate Thinness)"
    elif 17.0 <= bmi < 18.5:
        return "underweight (Mild Thinness)"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight (Pre-obese)"
    elif 30.0 <= bmi < 35.0:
        return "Obesity (Class I)"
    elif 35.0 <= bmi < 40.0:
        return "Obesity (Class II)"
    else:
        return "Obesity (Class III)"


def main():
    """
    This is the main function that contains the primary 
    logic to run the BMI calculator.
    """
    print("Welcome to the BMI Calculator!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's calculate your BMI.")

    while True:  # allows the program to run continuously until the user decides to exit.
        while True:
            try:
                weight = float(input("Kindly enter your weight in kilograms: "))
                height = float(input("Kindly enter your height in meters: "))
                if weight <= 0 or height <= 0:
                    raise ValueError  # Used to trigger the exception
                break
            except ValueError:
                print("Invalid input. Please enter positive numbers for weight and height.")

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        print(f"Dear {name}, your BMI is {bmi:.2f} and you are categorized as {category}.")

        # Ask the user if they want to calculate again
        while True:
            exit_prompt = input("Would you like to calculate another BMI? (yes/no): ").strip().lower()
            if exit_prompt in ('yes', 'y'):
                break  # repeat the BMI calculation
            elif exit_prompt in ('no', 'n'):
                print("Thank you for using the BMI Calculator. Goodbye!")
                return  # exit the program
            else:
                print("Invalid input. Please enter 'yes/no'.")


if __name__ == "__main__":
    main()