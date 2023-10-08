import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

from tkinter import *

iota = Tk()
iota.geometry("760x800")

iota.title("IOTA: Powered by Trinity")

def order():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")

            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    engine.setProperty("rate", 150)

    engine.say(audio)

    engine.runAndWait()


def Day():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def Time():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
    time = str(datetime.datetime.now())
    hour = int(time[11:13])
    if hour > 1 and hour < 12 :
        speak(" Good Morning Sir, I am IOTA. Tell me how may I help you")
    elif hour>12 and hour < 17 :
        speak(" Good Afternoon Sir, I am IOTA. Tell me how may I help you")
    elif hour > 17 and hour < 20 :
        speak(" Good Evening Sir, I am IOTA. Tell me how may I help you")
    else:
        speak(" Good Night Sir, I am IOTA. Tell me how may I help you")



def Take_query():
    Hello()
    while (True):
        query = order().lower()

        if "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "open youtube" in query:

            speak("Opening Youtube")
            webbrowser.open("www.youtube.com")
            continue

        elif "which day it is" and "tell me the day" in query:
            Day()
            continue

        elif "tell me the time" and "tell me the time" in query:
            Time()
            continue

        elif "bye" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "exit" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "stop" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "ok bye" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "dont help me" in query:
            speak("Bye. Have a nice day, sir.")

            exit()
        elif "end program" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "finish" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "wind up" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "terminate the program" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "close" in query:
            speak("Bye. Have a nice day, sir.")
            exit()
        elif "are you a human" in query:
            speak("No, I am an virtual Assistant")
            continue
        elif "open instagram" in query:
            speak("Opening instagram")
            webbrowser.open("www.instagram.com")
            continue

        elif "open twitter" in query:
            speak("Opening twitter")
            webbrowser.open("www.twitter.com")
            continue

        elif "open codezinger" in query:
            speak("Opening code-zinger")
            webbrowser.open("www.codezinger.com")
            continue
        elif "show me funny videos" in query:
            speak("Opening youtube for funny videos")
            webbrowser.open("https://www.youtube.com/results?search_query=funny+videos")
            continue

        elif "tell me a fact" in query:
            speak("Here's a fact... the word karate means empty hand in japanese")
            continue

        elif "tell me a fact" in query:
            speak("wikipedia says that Koalas can sleep up to 20 hours a day")
            continue

        elif " what is a virtual Assistant" in query:
            speak(
                "According to google, A virtual assistant is generally self-employed and provides professional administrative, technical, or creative assistance to clients remotely from a home office.")
            continue

        elif "what is an AI" in query:
            speak(
                "According to britannica , Artificial intelligence is intelligence demonstrated by machines, as opposed to natural intelligence displayed by animals including humans.")
            continue
        elif "tell me more about yourself" in query:
            speak(
                "Iam IOTA virtual assistant, I can help you to automate your day-to-day computer tasks such as sending emails, fetching information about anything from Wikepedia, display web-based documents to the users, etc. ")
            continue

        elif "tell me one more fact" in query:
            speak("Another fact for you - In wikipedia it says, There are over 6,500 languages spoken in the world")
            continue

        elif "who are your owners" in query:
            speak("I am daughter of Trinity")
            continue
        elif "who made you" in query:
            speak("I am daughter of Trinity")
            continue
        elif "tell about yourself" in query:
            speak("I am daughter of Trinity")
            continue
        elif "present yourself to sir" in query:
            speak("Hi Sir, this is IOTA. i am a virtual assistant made by Team trinity. I can perform several such as opening google, youtube, and different websites. I can tell you the current day and time and more things.")
            continue

        elif "tell me your name" in query:
            speak("I am IOTA. Your virtual Assistant")
            continue
        elif "how old are you" in query:
            speak("It depends on how you look at it. Trinity was found in 23 december 2021, but i was launched in 8th febuary 2022")
            continue
        elif "are you male or female" in query:
            speak("I'm all-inclusive")
        elif "whats your gender" in query:
            speak("I'm all-inclusive")


# if _name_ == '_main_':
#     Take_query()

# from tkinter import *
# iota=Tk()
# iota.geometry("400x400")
#
# iota.title("IOTA:")
def activate_submit():
    if var.get()==1:
        bttn['state']=NORMAL
    elif var.get()==0:
        bttn['state']=DISABLED
    else:
        print('something went wrong!')
var = IntVar()
cb = Checkbutton(
    iota,
    text="Allow Microphone",
    onvalue=1,
    offvalue=0,
    variable=var,
    font=("time", 16),
    command=activate_submit,
    fg='black',
    activebackground='green'
    )
# cb.pack(pady=50)
cb.grid(row=8,column=1)



dwnd1 = PhotoImage(file='hd3.png')
dwnd = PhotoImage(file='image.png')
lbl1=Label(image=dwnd1)
lbl1.grid(row=0,column=0)
dwnd2 = PhotoImage(file='head.png')
lbl2=Label(image=dwnd2)
lbl2.grid(row=0,column=1)

bttn =Button(iota, activebackground='red',relief="raised",width=200,image=dwnd,command=Take_query,state=DISABLED)
# bttn.pack(pady=40)
bttn.grid(row=9,column=1)
Button(iota,text="EXIT",font="lucid 9 bold",activebackground='red',activeforeground='black',command=exit, width=10, height=2).grid(row=10,column=1)

iota.mainloop()