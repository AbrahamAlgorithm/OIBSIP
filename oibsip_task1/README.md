# Voice Assistant - Voxia

This project is a semi-advanced voice assistant in Python. It can perform tasks based on voice commands, such as responding to "Hello, Hi or Hey", telling the current date and time, searching the web (Google) for information, telling interesting fact, sending email, and playing video on YouTube.

## Features

- Responds to greetings.
- Provides today's date in month, day and year format.
- Tells the current time in minutes, hours and seconds.
- Searches the web (Google) for information and can read out the information based on user queries.
- Plays video on YouTube.
- Sends email.
- Tells interesting fact, one at a time.

## Requirements

- Python 3.11.5

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AbrahamAlgorithm/OIBSIP.git
cd oibsip_task1
```

### 2. Create and Activate a Virtual Environment

#### On Windows

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# If you encounter an execution policy error, temporarily change the policy before activating the environment
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

#### On macOS/Linux

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate
```

### 3. Install Dependencies

After activating the virtual environment, install the required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure the virtual environment is activated in your terminal.
2. Run the `voice_assistant.py` file:

   ```bash
   python voice_assistant.py
   ```

3. The voice assistant will initialise and start listening for your commands.

## Functionality

- **Greeting Response**: The assistant will respond to "Hello, Hi or Hey" with a greeting and it if you don't include any of those words, it still will respond.
- **Time/ Date Response**: It immediately tells you the current date and time after the greeting.
- **Web Search**: Make sure whatever your query is, includes the word "information".
- **Plays Video on YouTube**: Just say the name of the YouTube video you want to play.
- **Sends Email**: Make sure whatever your query is, include the words "send" and "email".
- **Interesting Fact/ General Knowledge**: Make sure whatever your query is, includes either "fact" or "facts".

## Example Commands

- "Hello", "Hi", "Hey", "Hi Asiri", "Who goes there", etc.
- "Search for Python tutorials"
- "Dear Young Woman" or "Play me Dear Young Woman"
- "Can you send an email for me?"
- "Can you tell me an interesting fact?"