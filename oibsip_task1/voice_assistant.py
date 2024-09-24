#!/usr/bin/env python3
"""
Voice Assistant Module

This module implements a basic voice assistant that can respond to simple voice commands.
It uses speech recognition to interpret user input and text-to-speech to provide responses.

The assistant can perform tasks such as greeting the user, telling the time and date,
and performing basic web searches.
"""

import speech_recognition as sr
import pyttsx3
import datetime
import requests
import sys

class VoiceAssistant:
    """
    A class representing a basic voice assistant.

    This class encapsulates the functionality of the voice assistant,
    including speech recognition, text-to-speech, and command processing.
    """

    def __init__(self):
        """
        Initialize the voice assistant with speech recognition and text-to-speech engines.
        """
        self.recognizer = sr.Recognizer()
        try:
            self.engine = pyttsx3.init()
        except ImportError:
            print("Error: pyttsx3 not found. Make sure it's installed.")
            sys.exit(1)
        except RuntimeError:
            print("Error: Failed to initialize the text-to-speech engine.")
            print("Make sure you have the necessary system dependencies installed.")
            print("On Ubuntu/Debian, try: sudo apt-get install libespeak1 espeak")
            sys.exit(1)

    def listen(self):
        """
        Listen for user input through the microphone.
        
        Returns:
            str: The recognized speech as text, or an empty string if recognition fails.
        """
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return ""

    def speak(self, text):
        """
        Convert text to speech and play it.
        
        Args:
            text (str): The text to be spoken.
        """
        print(f"Assistant: {text}")
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            primt("Error: failed to speak. Check audio output")

    def process_command(self, command):
        """
        Process the user's command and respond accordingly.
        
        Args:
            command (str): The user's command as text.
        """
        if "hello" in command:
            self.speak("Hello! How can I help you?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
        elif "date" in command:
            current_date = datetime.date.today().strftime("%B %d, %Y")
            self.speak(f"Today's date is {current_date}")
        elif "search" in command:
            query = command.replace("search", "").strip()
            self.web_search(query)
        else:
            self.speak("I'm sorry, I don't understand that command.")

    def web_search(self, query):
        """
        Perform a basic web search using the DuckDuckGo API.
        
        Args:
            query (str): The search query.
        """
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["Abstract"]:
                self.speak(data["Abstract"])
            else:
                self.speak("I'm sorry, I couldn't find any relevant information.")
        else:
            self.speak("I'm sorry, I encountered an error while searching.")

    def run(self):
        """
        Run the voice assistant in a loop, continuously listening for commands.
        """
        self.speak("Hello! I'm your voice assistant. How can I help you?")
        while True:
            command = self.listen()
            if command:
                self.process_command(command)

if __name__ == "__main__":
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)