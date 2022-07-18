import datetime
import webbrowser

import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[7].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        talk("Good Morning")
    elif hour >= 12 and hour <= 18:
        talk("Good Afternoon")
    else:
        talk("Good Evening")

    bot_name = "Bhai"
    talk(f"I am your bot {bot_name}, how can I help you?")

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "siri" in command:
                command = command.replace("siri", "")
                print(command)
    except:
        pass
    return command


def run_siri():
    command = take_command()
    print(command)

    if "wikipedia" in command:
        talk("Searching Wikipedia...")
        wiki = command.replace("wikipedia", "")
        info = wikipedia.summary(wiki, sentences=2)
        print(info)
        talk(info)

    elif "play" in command:
        song = command.replace("play", "")
        print(song)
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "how are you" in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current time is", time)
        talk("current time is" + time)

    elif "open google" in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif "exit" in command:
        talk("Thanks for giving me your time")
        exit()

    else:
        talk("please repeat the command")


while True:
    run_siri()
