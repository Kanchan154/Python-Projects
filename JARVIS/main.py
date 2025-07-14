import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (change to 0 for male)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
            print("You said:", command)
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        talk("Internet connection error.")
        return ""
    return command

def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'open google' in command:
        talk("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'open youtube' in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'stop' in command or 'exit' in command:
        talk("Goodbye!")
        exit()
    else:
        talk("I can search that on Google for you.")
        pywhatkit.search(command)

# Run continuously
if __name__ == "__main__":
    talk("Hello, I am Jarvis. How can I assist you?")
    while True:
        run_jarvis()
