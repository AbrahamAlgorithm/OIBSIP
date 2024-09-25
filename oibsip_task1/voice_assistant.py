from selenium_web import info
import pyttsx3 as p
import speech_recognition as sr
from send_email import *
from YT_automation import *
import datetime
import randfacts
import yagmail

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "morning"
    elif hour >= 12 and hour < 16:
        return "afternoon"
    else:
        return "evening"

r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)  #made use of google api
    print(text)

greetings = ["hello", "hi", "hey"]

if any(greeting in text.lower() for greeting in greetings):
    speak(f"Hi Abraham, good {wish_me()}. My name is Voxia and I'm your Voice Assistant.")
else:
    speak("Sorry, I didn't catch that but no worries")

def get_date_and_time():
    today_date = datetime.datetime.now()
    date_announcement = today_date.strftime("%A, %B %d, %Y")
    time_announcement = today_date.strftime("%I:%M %p")
    seconds_announcement = today_date.strftime("%S")
    speak(f"Today is {date_announcement} and it's currently {time_announcement} with {seconds_announcement} seconds.")

get_date_and_time()

speak("How are you doing today?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("Thanks for asking, I am doing just fine!")
speak("What can I do for you at the moment?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("What exactly do you need information about?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    print("Searching {} on Google".format(infor))
    speak("Searching {} on Google".format(infor))

    assist = info()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("Which video do you want me to play for you?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    print("Playing {} on YouTube".format(vid))
    speak("Playing {} on YouTube".format(vid))

    assist = poem()
    assist.play(vid)

elif "send" and "email" in text2:
    speak("I am happy to send the email for you")

    with sr.Microphone() as source:
        print("clearing background noise...")
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        try:
            email_content = r.recognize_google(audio)
            print(f"Email content: {email_content}")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

    print("Sending e-mail now via Gmail".format(text2))
    speak("Sending e-mail now via Gmail".format(text2))

    send_email(email_content)

elif "fact" or "facts" in text2:
    speak("Sure Abraham,")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

speak("You're welcome. Anything else?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

exit_response = ["no", "not at all", "not at the moment"]   #acceptable4 exit response

if any(response in text.lower() for response in exit_response):
    print("Alrighty, I'm going to sleep now. Bye!")
    speak("Alrighty, I'm going to sleep now. Bye!")
else:
    print("Bye!")
    speak("I didn't hear you but I'm going to sleep anyways. Bye!")

exit(0)