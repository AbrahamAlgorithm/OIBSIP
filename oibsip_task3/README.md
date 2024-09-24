# BMI Calculator

This project provides a Command Line Body Mass Index (BMI) calculator written in Python. It calculates user's BMI based on their weight and height inputs and categorizes the result into standard health ranges.

## Features

- User-friendly command-line interface
- Calculates BMI based on weight (in kilograms) and height (in meters)
- Categorizes BMI into standard health ranges
  - Classifies BMI into categories:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 ≤ BMI < 24.9
  - Overweight: 25 ≤ BMI < 29.9
  - Obesity: BMI ≥ 30
- Input validation to ensure positive numerical inputs

## Requirements

- Python 3.10.12

## Usage

1. Ensure you have Python 3.10.12 installed on your system.
2. Clone this repository or download the `bmi_calculator.py` file.
3. Open a terminal and navigate to the directory containing `bmi_calculator.py`.

    ```bash
   git clone https://github.com/AbrahamAlgorithm/OIBSIP.git
   cd oibsip_task3
   ```

4. Run the script using the command:

   ```bash
   python3 bmi_calculator.py
   ```

5. Follow the prompts to enter your name, weight, and height.
6. The program will display your calculated BMI and the corresponding health category.


## Example

```
Welcome to the BMI Calculator!
What's your name? Abraham 
Hello, Abraham! Let's calculate your BMI.
Please enter your weight in kilograms: 75
Please enter your height in meters: 1.92
Abraham, your BMI is 20.35 and you are categorized as Normal Weight.
```

## Code Style

This project adheres to the `pycodestyle` style guide (version 2.5).

## Resources
Below are the list of resources I used for this project, in APA7 Citation style:

- Calculator.net. (2019). BMI Calculator. Calculator.net. [https://www.calculator.net/bmi-calculator.html](https://www.calculator.net/bmi-calculator.html)
