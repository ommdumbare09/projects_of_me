import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hi' in command:
                command = command.replace('Alexa','')
                print(command)
    except:
        pass
    return command



def run_hi():
    command = take_command()
    print(command)
    #play youtube songs or videos
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+song)
        pywhatkit.playonyt(song)

    # display time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('current time is '+ time)


    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,3)
        print(info)
        talk(info)

    elif 'what' in command:
        person = command.replace('what', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)

    elif 'How' in command:
        person = command.replace('How', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)

    elif 'Who' in command:
        person = command.replace('Who', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'Where' in command:
        person = command.replace('Where', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)


    # display date with voice command
    elif 'date' in command:
        talk('sorry, I have headache')

    elif 'are you single' in command:
        talk('I am in ralationship with wifi')

    #tells a joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke)

    else:
        talk('Please try again')


#while True:
run_hi()

