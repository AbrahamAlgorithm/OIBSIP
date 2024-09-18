#!/usr/bin/env python3
"""
This module provides a BMI (Body Mass Index) calculator with user interaction.

It calculates the BMI based on user input for weight and height,
and categorizes the result into standard health ranges.
"""

def calculate_bmi(weight, height):
    """
    Calculate the BMI given weight and height.

    Args:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: Calculated BMI rounded to two decimal places
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def categorize_bmi(bmi):
    """
    Categorize the BMI into standard health ranges.

    Args:
    bmi (float): Calculated BMI value

    Returns:
    str: BMI category (Underweight, Normal Weight, Overweight, or Obese)
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    """
    Main function to run the BMI calculator with user interaction.
    """
    print("Welcome to the BMI Calculator!")
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's calculate your BMI.")

    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            height = float(input("Please enter your height in meters: "))
            if weight <= 0 or height <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter positive numbers for weight and height.")

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)
    print(f"{name}, your BMI is {bmi} and you are categorized as {category}.")


if __name__ == "__main__":
    main()