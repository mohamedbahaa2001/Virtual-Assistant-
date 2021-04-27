import speech_recognition as sr
import pyaudio
import pyttsx3
import wikipedia
import pywhatkit
import webbrowser
import time
import pyautogui as gui
import datetime
import pyjokes
from email.message import EmailMessage
import smtplib
import pytube
import config


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def send_message():
    say("please enter the massege and the phone number")
    numbers = {int(input("enter the phone number here: "))}
    message = str(input("enter your message for whatsapp: "))

    interval = 2
    # position1 = 941, 432
    # position2 = 942, 534
    for number in numbers:
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(number, message)
        webbrowser.open(url)
        time.sleep(15)
        gui.press('enter')
        say("message sent successfully")
        time.sleep(interval)


author = config.Name.name  # input("enter your name: ")
# author = 'Mohamed'  # input("enter your name: ")
machine_name = "alex"  # input("Enter your Assistant name: ")
listener = sr.Recognizer()
# say("I am here Sir")
# say("Hello sir I am {}".format(machine_name))
say("how can i help you sir")


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(config.Login.email, config.Login.password)
    email = EmailMessage()
    email['from'] = config.Login.email
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


contacts = {'me': 'mohamedbahaa22.22@gmail.com'}


def get_email_info():
    say("who do you want to send the email to")
    name = get_info()
    receiver = contacts[name]
    print(receiver)
    say('what is the subject of the email')
    subject = get_info()
    say('what is the content of the message')
    message = get_info()
    send_email(receiver, subject, message)
    say('do you want to send another email ?')
    more_email = get_info()
    if 'yes' in more_email:
        get_email_info()
    else:
        run_max()


def say_hello():
    say('who do you want to say hello to')
    guest = get_info()
    say('hello' + guest)
    say('do you want me to say hello to some one else ?')
    answer = get_info()
    if 'yes' in answer:
        say_hello()
    else:
        run_max()


def commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                command = command.replace('alex', '')

    except Exception as ex:
        print(ex.message)
    return command


def run_max():
    command = commands()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        say('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        clock = datetime.datetime.now().strftime('%I:%M %p')
        print(clock)
        say('current time is' + clock)
        say('what else should i do for you sir')
    elif 'whatsapp message' in command:
        try:
            send_message()
            say('message sent')
            say('what else should i do for you sir')
        except:
            say('failed to send the message')
    elif 'tell me about' in command:
        person = command.replace('tell me information about', '')
        info = wikipedia.summary(person, 12)
        print(info)
        say(info)
        say('what else should i do for you sir')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        say(joke)
        say('what else should i do for you sir')
    elif 'hello my friend' in command:
        say("hello sir how can i help you")
    elif 'send email' in command:
        get_email_info()
        say('email sent')
        say('what else should i do for you sir')
    elif 'how are you' in command:
        say('i am good sir what about you')
    elif 'i am fine' in command:
        say('glad to know that')
    elif 'my friend' in command:
        say_hello()
    elif 'are you here' in command:
        say('i am always here for you sir')
    elif 'download video' in command:
        say('enter the video link to download')

        url = input("enter the URL: ")

        video = pytube.YouTube(url)

        stream = video.streams.get_by_itag(22)
        say('downloading')
        print("Donwloading...")
        stream.download(filename="TDiffusion, drift & barrier voltage")
        say("done")
        print('done')
    else:
        say("please say it again i didn't hear you")


while True:
    run_max()
