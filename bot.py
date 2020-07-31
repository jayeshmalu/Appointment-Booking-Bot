import re
import numpy as np
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from gtts import gTTS
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
list2 = ["1:30", "2:30", "3:30","4:30","4","4:15"]
list1 = ["Jayesh", "-" , "Malu","abc","ac","-"]
msgname=[]
msgrecord=[]
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Your voice not recognized...")
        speak("Speak again...")        
          
        return takeCommand()
    return query


def execute(): 

    speak("Welcome, I am Bot, for Appointment booking, which of the following help you want?")
    print("\nAppointment / Message ?") 
    speak("Do you want to book an appointment, or, do you want to record message?")
   
    query = takeCommand().lower()
    print(query)
    #print(re.split(' ',list2[1]))

    if query=='appointment':
        print("\nAt what time you want to book an appointment ?")
        speak("At what time you want to book an appointment ?")

        check = takeCommand().lower()
        check = int(check)
        if check>100:
            check = (str(int(check/100))+ ":"+ str(int(check%100)) )

        print(check)
        index = 0
        flag = 0
        flag1 = 0
        no = 1
        for app in list2:
            x = re.split(':',app)
            if check == app and list1[index] == "-":
                print("\nAppointment is available at : " + check)
                #print(check)
                speak("Appointment is available.")
                
                print("\nDo you want to book appointment at this time ? Yes/No ")
                speak("Do you want to book appointment at this time ?")
                ask = takeCommand().lower() 
                print(ask)
                if ask == "yes":
                    print("\nBy what name you want to book this appointment?")
                    speak("By what name you want to book this appointment?")
                    name1 = takeCommand().lower() 
                    print(name1)
                    list1[index]= name1
                    msg2 = "\nAppointment is booked by {0} at {1}"
                    print(msg2.format(list1[index],list2[index]))
                    speak("Thank you for booking Appointment")
                    no = 0 
            
                flag=0
                break
        
            elif int(x[0]) >= int(check) and list1[index] == "-":
                print("\nSorry, this appointment is already booked, next appointment is available at : " + app)
                #print(app)
                speak(f"Sorry, this appointment is already booked, next appointment is available at {app}")
                
                print("\nDo you want to book appointment at this time ? Yes/No")
                speak("Do you want to book appointment at this time ?")
                ask = takeCommand().lower()
                print(ask)
                if ask == "yes":
                    print("\nBy what name you want to book this appointment?")
                    speak("By what name you want to book this appointment?")
                    name1 = takeCommand().lower() 
                    print(name1)
                    list1[index]= name1
                    msg2 = "\nAppointment is booked by {0} at {1}"
                    print(msg2.format(list1[index],list2[index]))
                    print("\nThank you for booking Appointment")
                    speak("Thank you for booking Appointment")    
                    no = 0    
                flag=0
                break
        
            else:
                flag=1  
                      
            index = index+1
        if flag == 1:
            print("\nSorry, Appointment is not available at this time {check}")
            speak(f"Sorry, Appointment is Not available at this time {check}")
    
        if no == 1:
            print("\nDo you want to see all available Appointments ? Yes/No ")
            speak("Do you want to see all available Appointments ? ")
            answer = takeCommand().lower()
            print(answer)
            count=0
            count1=0
            if answer == "yes":
                for element in list1:
                    if element == "-":
                        msg = "\nAppointment at {} is free"
                        print(msg.format(list2[count]))
                    count = count + 1
                print("\nAt what time you want to book Appointment ? ")
                speak("At what time you want to book Appointment ? ")
                time = takeCommand().lower() 
                time = int(time)
                if time > 100:
                    time = (str(int(time/100))+ ":"+ str(int(time%100)) )
                print(time)

                for element1 in list2:
                    if element1 == time:
                        print("\nBy what name you want to book that Appointment?")
                        speak("By what name you want to book that Appointment?")
                        name = takeCommand().lower() 
                        print(name)
                        list1[count1]=name
                        msg1 = "\nAppointment is booked by {0} at {1}"
                        print(msg1.format(list1[count1],list2[count1]))
                        print("\nThank you for booking Appointment")
                        speak("Thank you for booking Appointment")
                        flag1=1    
                    count1 = count1 + 1
                if flag1 == 0 :
                    print("\nSorry Already this Appointment is booked")
                    speak("Sorry Already this Appointment is booked")
            elif answer == "no":
                print("Thank you for visiting !")
                speak("Thank you for visiting")
        else:
            print("\nThank you for visiting !")
            speak("Thank you for visiting")

    elif query=='message':
        print("\nCan you please tell me your name ?")
        speak("Can you please tell me your name ?")
        mname = takeCommand().lower() 
        print(mname)
        msgname.append(mname)
        print("\nSpeak, your message is recording...")
        speak("Speak, your message is recording...")
        mmsg = takeCommand().lower()
        print(mmsg) 
        msgrecord.append(mmsg)
        print("\nYour message has been recorded, Contact you shortly")
        speak("Your message has been recorded, Contact you shortly")

    elif query=='login':
        print("\nHello, can you please tell me your id ?")
        speak("Hello, can you please tell me your id ?")
        user = takeCommand().lower() 
        print(user)
        print("Your password ?")
        speak("Your password ?")
        password = takeCommand().lower() 
        print(password)
        if user == 'jayesh' and password=='jrm':
            print("\nFollowing are your appointments: ")
            speak("Following are your appointments: ")
            arr1 = np.array(list2)
            arr2 = np.array(list1)
            arr5 = np.stack((arr1, arr2), axis=1)
            print(arr5)
            print("\nFollowing are messages for you: ")
            speak("Following are messages for you: ")
            arr3 = np.array(msgname)
            arr4 = np.array(msgrecord)
            arr6 = np.stack((arr3, arr4), axis=1)
            #print(msgname)
            #print(msgrecord)
            print(arr6)

        else:
            print("\nInvalid Id or Password")
            speak("Invalid Id or Password")
    else:
        print("\nInvalid choice")
        speak("Invalid choice")      

if __name__ == "__main__":
    execute()

