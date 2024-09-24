# Random Password Generator

This repository contains a command-line password generator that allows users to create random passwords based on customizable criteria. The generator includes error handling for invalid inputs and ensures that users can specify password length, and whether to include letters, numbers, and symbols.
It aims to help beginners learn Python by incorporating concepts such as randomisation, user input validation, and character set handling.


## Features
- Customize password length (minimum of 4 characters).
- Option to include letters, numbers, and symbols.
- Error handling for invalid inputs (e.g., non-numeric values for length).
- Ability to generate multiple passwords in a single session.

## Getting Started

### Prerequisites

- Python 3.10.12

### Installation

1. Clone this repository to your local machine:
    ```bash
    git clone  https://github.com/AbrahamAlgorithm/OIBSIP.git
    ```

2. Navigate to the directory containing the script:
    ```bash
    cd oibsip_task2
    ```

3. Run the Python script:
    ```bash
    ./pwd_generator.py
    ```
   Make sure to give the script execute permission if needed:
    ```bash
    chmod +x pwd_generator.py
    ```

4. Follow the on-screen prompts to generate a password:
    - Enter the desired password length.
    - Choose whether to include letters, numbers, and/or symbols.
    - The program will generate a random password based on your preferences.

5. After the password is generated, you can choose to generate another password or exit the program.

## Example Usage

```bash
$ ./password_generator.py
Welcome to the Password Generator!
Enter the desired password length (minimum 4): 12
Include letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n
Your generated password is: A9djsf8Ka9lw
Do you want to generate another password? (y/n): n
Thank you for using the Password Generator. Goodbye!
