from ctypes import cdll
import tkinter
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import socket
import os.path
from os import path
import smtplib
import itertools
import shutil
from ntpath import basename, splitext
import google
from word2number import w2n
import sys
import pyautogui
import pywhatkit
import keyboard
from keyboard import press
from keyboard import press_and_release
from requests import get
import pyjokes
#from newsapi import NewsApiClient
#import pycountry
import requests
import speedtest
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import time
import sqlite3
import gui
import threading
from tkinter import *
#from gui import

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

r3 = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output
    
    with sr.Microphone() as source:
        print("Listening...")
        gui.App.entry_2.insert("1.0","Listening..." +"\n")

        r2.pause_threshold = 1.5
        audio = r2.listen(source,phrase_time_limit=7)
        
    try:
        print("Recognizing...")    
        gui.App.entry_2.insert("1.0","Recognizing..." +"\n")
        query = r2.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        gui.App.entry_2.insert("1.0",f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        gui.App.entry_2.insert("1.0","Say that again please...\n")
        return "None"
    return query

def takecommand():
    with sr.Microphone() as source:
        print("Listening.....")
        gui.App.entry_2.insert("1.0","Listening.....\n")
        r2.pause_threshold = 1.5
        audio = r2.listen(source,phrase_time_limit=6)  #phrase_time_limit=5

    try:
        print("Recognizing....")
        gui.App.entry_2.insert("1.0","Recognizing....\n")
        query = r2.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        gui.App.entry_2.insert("1.0",f"User said: {query}\n")


    except Exception as e:
        print("Say that again please...") 
        gui.App.entry_2.insert("1.0","Say that again please...\n")
        return "None"                             #change accourding to the states
    return query.lower()
    
def takecommand_yes():
    with sr.Microphone() as source:
        print("Listening.....")
        gui.App.entry_2.insert("1.0","Listening.....\n")
        r2.pause_threshold = 1.5
        audio = r2.listen(source,phrase_time_limit=5)  #phrase_time_limit=5

    try:
        print("Recognizing....")
        gui.App.entry_2.insert("1.0","Recognizing....\n")
        query = r2.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        gui.App.entry_2.insert("1.0",f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        gui.App.entry_2.insert("1.0","Say that again please...\n")
        return "None"                             #change accourding to the states
    return query.lower()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    #speak("I am Alexa Sir. Please tell me how may I help you")  

def main():
    global pathc
    global pathc_desktop
    global pathc_documents
    global pathc_downloads
    global pathc_ss
    global administrator
    global conn
    global c
    global database1
    global new_drive
    global file_name
    global d
    global r
    global n
    global e
    global f
    global cd
    global numberoffiles
    global specify_pathc
    global specify_calling
    





    d=None
    cd=None
    specify_pathc=None
    specify_calling=None
    numberoffiles=None
    f=None
    n=None
    e=None
    r=None

    file_name=None
    new_drive=None

    administrator = None
    
   # gui.entry_2.config(text="Please Type out your Administrator Name so as to access user files:")
    speak("Hello User,I welcome")
    speak("Please Type out your Administrator Name so as to access user files")
    print("Please Type out your Administrator Name so as to access user files:")
    gui.App.entry_2.insert("1.0","Please Type out your Administrator\n Name so as to access user files:\n")

    def get_admin():
        global administrator
        administrator = gui.App.entry_1_str.get()
        gui.App.entry_1.delete(0,END)
        
    gui.App.button_2.config(command=get_admin)
    
    while administrator is None:
        pass
    
    wishMe()
        
    #administrator=str(input())
    pathc="C:\\Users\\" + administrator
    pathc_desktop="C:\\Users\\" + administrator + "\\Desktop"
    pathc_documents="C:\\Users\\" + administrator + "\\Documents"
    pathc_downloads="C:\\Users\\" + administrator + "\\Downloads"
    pathc_ss = "C:\\Users\\" + administrator + "\\Desktop\\Python"
    # gui.App.entry_2.config(text=pathc)
    gui.App.entry_2.insert(tkinter.END, pathc+"\n")
    # gui.App.entry_2.config(text=pathc_desktop)
    gui.App.entry_2.insert("1.0", pathc_desktop+"\n")
    #gui.App.entry_2.config(text=pathc_documents)
    gui.App.entry_2.insert("1.0", pathc_documents+"\n")
    # gui.App.entry_2.config(text=pathc_downloads)
    gui.App.entry_2.insert("1.0", pathc_downloads+"\n")
    # gui.App.entry_2.config(text=pathc_ss)
    gui.App.entry_2.insert("1.0", pathc_ss+"\n")
    database1 = 'test1.db'
    conn = sqlite3.connect(database1)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS FAVOURITE (CALL TEXT PRIMARY KEY NOT NULL,PATH TEXT NOT NULL)")
    print(pathc)
    print(pathc_desktop)
    print(pathc_documents)
    print(pathc_downloads)
    print(pathc_ss)

    while(1):
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r3.adjust_for_ambient_noise(source2)

                # listens for the user's input
                
                print("Call me Alexa")
                # gui.App.entry_2.config(text=msg)
                gui.App.entry_2.insert("1.0", "Call me Alexa"+"\n")

                r3.pause_threshold = 1
                audio2 = r3.listen(source2,phrase_time_limit=3.5)  #phrase_time_limit=3 train it to take input as soon as user stops saying

                # Using ggogle to recognize audio
                MyText = ''
                MyText = r3.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
                gui.App.entry_2.insert("1.0",MyText+"\n")

                if 'alexa' in MyText or 'siri' in MyText or 'ava' in MyText or 'zoya' in MyText or 'apple' in MyText or 'maya' in MyText:
                    speak('yes')
                    r1.adjust_for_ambient_noise(source2)
                    print('Listening....')
                    # gui.App.entry_2.config(text='Listening....')
                    gui.App.entry_2.insert("1.0", "Listening...."+"\n")

                    r1.pause_threshold = 1
                    audio3 = r1.listen(source2,phrase_time_limit=7.5)
                    # Using ggogle to recognize audio
                    MyNewText = ''
                    MyNewText = r1.recognize_google(audio3)
                    MyNewText = MyNewText.lower()
                    print("you said "+MyNewText)
                    gui.App.entry_2.insert("1.0","you said "+MyNewText+"\n")
                    solutionFinder(MyNewText)
                #SpeakText(MyText)
                
                elif 'sleep system' in MyText or 'deactivate system' in MyText:
                    speak("Thank you System Deactivated.")
                    sys.exit()          #error-coming

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            gui.App.entry_2.insert("1.0","Could not request results; {0}".format(e)+"\n")

        except sr.UnknownValueError:
            pass

        except sr.WaitTimeoutError:
            pass

 

def drive_name():
    #speak("Select From Specified Drive")
    #print("\n1 : D \n2 : E\n3 : C\n4 : Desktop\n5 : Documents\n6 : Downloads ") 
    drive_initialization = takecommand() #TO PREVENT LOOPING
    if ("1" in drive_initialization or "d drive" in drive_initialization or "one" in drive_initialization):   #all small cases due to lower() in takecommand() option
        return "d"
    elif ("tu" in drive_initialization or "e drive" in drive_initialization or "t w o" in drive_initialization or "2" in drive_initialization):
        return "e"
    elif ("3" in drive_initialization or "c drive" in drive_initialization or "three" in drive_initialization):
        return pathc
    elif ("4" in drive_initialization or "desktop" in drive_initialization or "desktops" in drive_initialization or "four" in drive_initialization):
        return pathc_desktop
    elif ("5" in drive_initialization or "documents" in drive_initialization or "document" in drive_initialization or "five" in drive_initialization):
        return pathc_documents
    elif ("6" in drive_initialization or "downloads" in drive_initialization or "download" in drive_initialization or "six" in drive_initialization):
        return pathc_downloads
    elif ("new drive" in drive_initialization):
        print("Please input Name of Drive")
        gui.App.entry_2.insert("1.0","Please input Name of Drive"+"\n")
        speak("Please input Name of Drive")
        def get_new_drive():
            global new_drive
            new_drive = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_new_drive)
    
        while new_drive is None:
            pass

        #new_drive = input()
        return new_drive
    else:
        print("Invalid Choice Please Select from specified Drive!")
        gui.App.entry_2.insert("1.0","Invalid Choice Please Select from specified Drive!"+"\n")
        speak("Invalid Choice Please Select from specified Drive!")
        return drive_name()
    
    
def returnfile(drivename,inp):
    counter = 0
    #print("If you want all the excel file, for example write .xlsx:\n")
    #drivename = input("Enter the specified Drive?\n")
    #inp = input("What are you looking for?:>\n")
    results = list(map(''.join, itertools.product(*zip(inp.upper(), inp.lower()))))
    #print(type(results))
    b=[]
    drive=drivename + ":\\"     
    thisdir = os.getcwd()
    for r, d, f in os.walk(drive): # change the hard drive, if you want
        for file in f:
            filepath = os.path.join(r, file)
            for i in results:
                if i in file:
                    counter += 1
                    b.append(os.path.join(r, file))
                    
    return b

def returnfile_c(drivename,inp):
    counter = 0
    #print("If you want all the excel file, for example write .xlsx:\n")
    #drivename = input("Enter the specified Drive?\n")
    #inp = input("What are you looking for?:>\n")
    results = list(map(''.join, itertools.product(*zip(inp.upper(), inp.lower()))))
    #print(type(results))
    b=[]    
    thisdir = os.getcwd()
    for r, d, f in os.walk(drivename): # change the hard drive, if you want
        for file in f:
            filepath = os.path.join(r, file)
            for i in results:
                if i in file:
                    counter += 1
                    b.append(os.path.join(r, file))
                    
    return b


def returnfilename():
    file_name=None
    print("\nSpecify Filename : ")  #speak
    gui.App.entry_2.insert("1.0","\nSpecify Filename : "+"\n")
    #file_name = input()
    def get_file_name():
        global file_name
        file_name = gui.App.entry_1_str.get()
        gui.App.entry_1.delete(0,END)
    gui.App.button_2.config(command=get_file_name)
    
    while file_name is None:
        pass
    
    print("\nIs it Right : ")
    gui.App.entry_2.insert("1.0","\nIs it Right : "+"\n")
    speak("Is it Right : ") #speak()
    cd = takecommand_yes()
    if "yes" in cd:
        return file_name 
    else:
        return returnfilename()
    
    
def returnfilename_withtext():
    print("\nSpecify Filename : ") 
    gui.App.entry_2.insert("1.0","\nSpecify Filename : "+"\n")  
    speak("Specify Filename : ")   #speak
    file_name = takecommand()
    print("\nIs it Right : ")
    gui.App.entry_2.insert("1.0","\nIs it Right : "+"\n")
    speak("Is it Right : ") #speak()
    cd = takecommand_yes()
    if "yes" in cd:
        return file_name 
    else:
        return returnfilename_withtext()

def destination_folder_copy_sf(filepathname):
    try:
        d=None
        print("enter drive\n")
        gui.App.entry_2.insert("1.0","Enter Drive"+"\n") 
        #d = input("Enter Drive")
        def get_d():
            global d
            d = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_d)
    
        while d is None:
            pass
        if (len(d)==int(1)):
            r=None
            # r = input("\nEnter Respective Root Folder : ")
            gui.App.entry_2.insert("1.0","\nEnter Respective Root Folder : "+"\n") 
            def get_r():
                global r
                r = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_r)
            while r is None:
                pass
            if "0" not in r and "zero" not in r and "ZERO" not in r:
                e=None
                #e = input("\nFolder in root folder : ")
                
                gui.App.entry_2.insert("1.0","\nFolder in root folder : "+"\n")
                def get_e():
                    global e
                    e = gui.App.entry_1_str.get()
                    gui.App.entry_1.delete(0,END)
                gui.App.button_2.config(command=get_e)
                while e is None:
                    pass
                if "0" not in e and "zero" not in e and "ZERO" not in e:
                    #f = input("\nBase Folder")
                    f=None
                    gui.App.entry_2.insert("1.0","\nBase Folder"+"\n")
                    def get_f():
                        global f
                        f = gui.App.entry_1_str.get()
                        gui.App.entry_1.delete(0,END)
                    gui.App.button_2.config(command=get_f)
                    while f is None:
                        pass
        file_name = basename(filepathname)
        print("\n" + file_name + "\n")
        gui.App.entry_2.insert("1.0","\n" + file_name + "\n"+"\n")  
        if(d=="desktop" or d=="desktops"):
            copypath = pathc_desktop + "\\" + file_name
            #print(copypath)
            shutil.copyfile(filepathname,copypath)
        elif(d=="documents"or d=="document"):
            copypath = pathc_documents + "\\" + file_name
            #print(copypath)
            shutil.copyfile(filepathname,copypath)
        elif(d=="downloads" or d=="download"):
            copypath = pathc_downloads + "\\" + file_name
            #print(copypath)
            shutil.copyfile(filepathname,copypath)
        elif(r == "0" or r=="ZERO" or r == "zero" ):
            copypath = d + ":\\" + file_name
            #print(copypath)
            shutil.copyfile(filepathname,copypath)
        elif (e == "0" or e=="ZERO" or e == "zero" ):
            copypath = d + ":\\" + r + "\\" + file_name
            #print(copypath)
            shutil.copyfile(filepathname,copypath)
        elif (f == "0" or f=="ZERO" or f == "zero" ):
            copypath = d + ":\\" + r + "\\" + e + "\\" + file_name
            #print(copypath) 
            shutil.copyfile(filepathname,copypath)
        else:
            copypath = d + ":\\" + r + "\\" + e + "\\" + f + "\\" + file_name
            #print(copypath) 
            shutil.copyfile(filepathname,copypath)  
            
    except Exception as e:
        print("Sorry No such Directory or path present")
        gui.App.entry_2.insert("1.0","Sorry No such Directory or path present"+"\n")  
        speak("Sorry No such Directory or path present")
            

def destination_folder_move_sf(filepathname):
    try:
        #d = input("Enter Drive")
        d=None
        gui.App.entry_2.insert("1.0","Enter Drive"+"\n") 

        def get_d():
            global d
            d = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_d)
        while d is None:
            pass
        if (len(d)==int(1)):
            #r = input("\nEnter Respective Root Folder : ")
            r=None
            gui.App.entry_2.insert("1.0","\nEnter Respective Root Folder : "+"\n") 
            def get_r():
                global r
                r = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_r)
            while r is None:
                pass
            if "0" not in r and "zero" not in r and "ZERO" not in r:
                #e = input("\nFolder in root folder : ")
                e=None
                gui.App.entry_2.insert("1.0","\nFolder in root folder : "+"\n")
                def get_e():
                    global e
                    e = gui.App.entry_1_str.get()
                    gui.App.entry_1.delete(0,END)
                gui.App.button_2.config(command=get_e)
                while e is None:
                    pass
                if "0" not in e and "zero" not in e and "ZERO" not in e:
                    # f = input("\nBase Folder")
                    f=None
                    gui.App.entry_2.insert("1.0","\nBase Folder"+"\n")
                    def get_f():
                        global f
                        f = gui.App.entry_1_str.get()
                        gui.App.entry_1.delete(0,END)
                    gui.App.button_2.config(command=get_f)
                    while f is None:
                        pass
        file_name = basename(filepathname)
        print("\n" + file_name + "\n")
        gui.App.entry_2.insert("1.0","\n" + file_name + "\n"+"\n")
        
        if(d=="desktop" or d=="desktops"):
            copypath = pathc_desktop + "\\" + file_name
            #print(copypath)
            shutil.move(filepathname,copypath)
        elif(d=="documents"or d=="document"):
            copypath = pathc_documents + "\\" + file_name
            #print(copypath)
            shutil.move(filepathname,copypath)
        elif(d=="downloads" or d=="download"):
            copypath = pathc_downloads + "\\" + file_name
            #print(copypath)
            shutil.move(filepathname,copypath)   
        elif(r == "0" or r=="ZERO" or r == "zero" ):
            copypath = d + ":\\" + file_name
            #print(copypath)
            shutil.move(filepathname,copypath)
        elif (e == "0" or e=="ZERO" or e == "zero" ):
            copypath = d + ":\\" + r + "\\" + file_name
            #print(copypath)
            shutil.move(filepathname,copypath)
        elif(f == "0" or f=="ZERO" or f == "zero" ):
            copypath = d + ":\\" + r + "\\" + e + "\\" + file_name
            #print(copypath) 
            shutil.move(filepathname,copypath)
        else:
            copypath = d + ":\\" + r + "\\" + e + "\\" + f + "\\" + file_name
            #print(copypath) 
            shutil.move(filepathname,copypath)    
            
    except Exception as e:
        print("Sorry No such Directory or path present")
        gui.App.entry_2.insert("1.0","Sorry No such Directory or path present"+"\n")
        speak("Sorry No such Directory or path present")     
            
        
def destination_folder_copy_mf(filepathname):
    try:
        #d = input("Enter Drive")
        d=None
        gui.App.entry_2.insert("1.0","Enter Drive"+"\n") 
        speak("Enter Drive")

        def get_d():
            global d
            d = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_d)
        while d is None:
            pass
        if (len(d)==int(1)):
            #r = input("\nEnter Respective Root Folder : ")
            r=None
            gui.App.entry_2.insert("1.0","\nEnter Respective Root Folder : "+"\n") 
            def get_r():
                global r
                r = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_r)
            while r is None:
                pass
            if "0" not in r and "zero" not in r and "ZERO" not in r:
                #e = input("\nFolder in root folder : ")
                e=None
                gui.App.entry_2.insert("1.0","\nFolder in root folder : "+"\n")
                def get_e():
                    global e
                    e = gui.App.entry_1_str.get()
                    gui.App.entry_1.delete(0,END)
                gui.App.button_2.config(command=get_e)
                while e is None:
                    pass
                if "0" not in e and "zero" not in e and "ZERO" not in e:
                    #f = input("\nBase Folder")
                    f=None
                    gui.App.entry_2.insert("1.0","\nBase Folder"+"\n")
                    def get_f():
                        global f
                        f = gui.App.entry_1_str.get()
                        gui.App.entry_1.delete(0,END)
                    gui.App.button_2.config(command=get_f)
                    while f is None:
                        pass
        basenames = []
        for name in filepathname:
            file_name = basename(name)
            basenames.append(file_name)
        print(basenames)
        gui.App.entry_2.insert("1.0",basenames+"\n")
        #print("230")
        cout = 0
        for base_name in basenames:
            print("\n" + base_name + "\n")
            gui.App.entry_2.insert("1.0","\n" + base_name + "\n"+"\n")
            if (d=="desktop" or d=="desktops" or d=="documents"or d=="document" or d=="downloads" or d=="download"):
                
                if(d=="desktop" or d=="desktops"):
                    copypath = pathc_desktop + "\\" + base_name
                    #print(copypath)
                    shutil.copyfile(filepathname[cout],copypath)
                elif(d=="documents"or d=="document"):
                    copypath = pathc_documents + "\\" + base_name
                    #print(copypath)
                    shutil.copyfile(filepathname[cout],copypath)
                elif(d=="downloads" or d=="download"):
                    copypath = pathc_downloads + "\\" + base_name
                    #print(copypath)
                    shutil.copyfile(filepathname[cout],copypath)    
            else:
                
                if(r == "0" or r=="ZERO" or r == "zero" ):
                    copypath = d + ":\\" + base_name
                    #print(copypath)
                    shutil.copyfile(filepathname[cout],copypath)
                elif (e == "0" or e=="ZERO" or e == "zero" ):
                    copypath = d + ":\\" + r + "\\" + base_name
                    #print(copypath)
                    shutil.copyfile(filepathname[cout],copypath)
                elif(f == "0" or f=="ZERO" or f == "zero" ):
                    copypath = d + ":\\" + r + "\\" + e + "\\" + base_name
                    #print(copypath) 
                    shutil.copyfile(filepathname[cout],copypath)
                else:
                    copypath = d + ":\\" + r + "\\" + e + "\\" + f + "\\" + base_name
                    #print(copypath) 
                    shutil.copyfile(filepathname[cout],copypath) 

            cout = cout + 1
            
    except Exception as e:
        print("Sorry No such Directory or path present")
        gui.App.entry_2.insert("1.0","Sorry No such Directory or path present"+"\n")
        speak("Sorry No such Directory or path present")
            
def destination_folder_move_mf(filepathname):
    try:
        #d = input("Enter Drive")
        d=None
        gui.App.entry_2.insert("1.0","Enter Drive"+"\n") 

        def get_d():
            global d
            d = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_d)
        while d is None:
            pass
        if (len(d)==int(1)):
            #r = input("\nEnter Respective Root Folder : ")
            r=None
            gui.App.entry_2.insert("1.0","\nEnter Respective Root Folder : "+"\n") 
            def get_r():
                global r
                r = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_r)
            while r is None:
                pass
            if "0" not in r and "zero" not in r and "ZERO" not in r:
                #e = input("\nFolder in root folder : ")
                e=None
                gui.App.entry_2.insert("1.0","\nFolder in root folder : "+"\n")
                def get_e():
                    global e
                    e = gui.App.entry_1_str.get()
                    gui.App.entry_1.delete(0,END)
                gui.App.button_2.config(command=get_e)
                while e is None:
                    pass
                if "0" not in e and "zero" not in e and "ZERO" not in e:
                    #f = input("\nBase Folder")
                    f=None
                    gui.App.entry_2.insert("1.0","\nBase Folder"+"\n")
                    def get_f():
                        global f
                        f = gui.App.entry_1_str.get()
                        gui.App.entry_1.delete(0,END)
                    gui.App.button_2.config(command=get_f)
                    while f is None:
                        pass
        basenames = []
        for name in filepathname:
            file_name = basename(name)
            basenames.append(file_name)
        #print(basenames)   
        cout = 0
        for base_name in basenames:
            print("\n" + base_name + "\n")
            gui.App.entry_2.insert("1.0","\n" + base_name + "\n"+"\n")
            if (d=="desktop" or d=="desktops" or d=="documents"or d=="document" or d=="downloads" or d=="download"):
                if(d=="desktop" or d=="desktops"):
                    copypath = pathc_desktop + "\\" + base_name
                    #print(copypath)
                    shutil.move(filepathname[cout],copypath)
                elif(d=="documents"or d=="document"):
                    copypath = pathc_documents + "\\" + base_name
                    #print(copypath)
                    shutil.move(filepathname[cout],copypath)
                elif(d=="downloads" or d=="download"):
                    copypath = pathc_downloads + "\\" + base_name
                    #print(copypath)
                    shutil.move(filepathname[cout],copypath)  
                    
            else:
                
                if(r == "0" or r=="ZERO" or r == "zero" ):
                    copypath = d + ":\\" + base_name
                    #print(copypath)
                    shutil.move(filepathname[cout],copypath)
                elif (e == "0" or e=="ZERO" or e == "zero" ):
                    copypath = d + ":\\" + r + "\\" + base_name
                    #print(copypath)
                    shutil.move(filepathname[cout],copypath)
                elif (f == "0" or f=="ZERO" or f == "zero"):
                    copypath = d + ":\\" + r + "\\" + e + "\\" + base_name
                    #print(copypath) 
                    shutil.move(filepathname[cout],copypath)   
                else:
                    copypath = d + ":\\" + r + "\\" + e + "\\" + f + "\\" + base_name
                    #print(copypath) 
                    shutil.move(filepathname[cout],copypath)   
                    
            cout = cout + 1
            
    except Exception as e:
        print("Sorry No such Directory or path present")
        gui.App.entry_2.insert("1.0","Sorry No such Directory or path present"+"\n")
        speak("Sorry No such Directory or path present")
        
def sf_operations(filepathname):
    while True:
        speak("Choose Operation to Perform")
        print("\n 1 : Open \n 2 : Copy \n 3 : Move \n 4 : Delete \n 5 : Quit") #takeCommand()
        gui.App.entry_2.insert("1.0","\n 1 : Open \n 2 : Copy \n 3 : Move \n 4 : Delete \n 5 : Quit"+"\n")
        option = takecommand()
        if "one" in option or "open" in option or "1" in option:
            try:
                os.startfile(filepathname)
                
            except Exception as e:
                print("No application is associated with the specified file for this operation")
                gui.App.entry_2.insert("1.0","No application is associated with the specified file for this operation"+"\n")
                speak("No application is associated with the specified file for this operation")
        elif "two" in option or "copy" in option or "2" in option:
            destination_folder_copy_sf(filepathname)
        elif "three" in option or "move" in option or "3" in option:
            destination_folder_move_sf(filepathname)
        elif "four" in option or "delete" in option or "4" in option:
            os.remove(filepathname)
            print("\nSuccessfully Removed " + filepathname )
            gui.App.entry_2.insert("1.0","\nSuccessfully Removed " + filepathname +"\n")
        elif "five" in option or "quit" in option or "exit" in option or "5" in option:
            break
        else:
            speak("Invalid Operation. Please Enter Valid Input")
            return sf_operations(filepathname)

def mf_operations(filepathname):
    while True:
        print("\n 1 : Open \n 2 : Copy \n 3 : Move \n 4 : Delete  \n 5 : Quit")
        gui.App.entry_2.insert("1.0","\n 1 : Open \n 2 : Copy \n 3 : Move \n 4 : Delete  \n 5 : Quit" +"\n") #takeCommand()
        speak("Choose Operation to Perform")
        option = takecommand()
        if "one" in option or "open" in option or "1" in option:
            try:
                for i in filepathname:
                    os.startfile(i)
                    
            except Exception as e:       
                print("No application is associated with the specified file for this operation")
                gui.App.entry_2.insert("1.0","No application is associated with the specified file for this operation" +"\n") 
                speak("No application is associated with the specified file for this operation")
                
        elif "two" in option or "copy" in option or "2" in option:
            destination_folder_copy_mf(filepathname)
        elif "three" in option or "move" in option or "3" in option: 
            destination_folder_move_mf(filepathname)
        elif "four" in option or "delete" in option or "4" in option:
            #os.remove(filepathname)
            for i in filepathname:
                os.remove(i)
                print("\nSuccessfully Removed " + i )
                gui.App.entry_2.insert("1.0","\nSuccessfully Removed " + i+"\n")
        elif "five" in option or "quit" in option or "exit" in option or "5" in option:
            break
        else:
            speak("Invalid Operation. Please Enter Valid Input")
            return mf_operations(filepathname)

def index_input():
    print("Specify Index Number : ")
    gui.App.entry_2.insert("1.0","Specify Index Number : "+"\n")
    speak("Specify Index Number : ")   #speak
    index_str = takecommand()
    print(index_str)
    gui.App.entry_2.insert("1.0",index_str+"\n")
    print("Is it right : ")
    gui.App.entry_2.insert("1.0","Is it right : "+"\n")
    speak("Is it Right : ") #speak()
    cd = takecommand_yes()   
    #print("353")
    if "yes" in cd:
        index_int = w2n.word_to_num(index_str)
        return index_int
    else:
        return index_input()  

def selection_operation():
    Operationto = takecommand() 
    print("Are you sure : ")
    gui.App.entry_2.insert("1.0","Are you sure : "+"\n")
    speak("Are you sure : ") #speak()
    cd = takecommand_yes()  
    #print("366")
    if "yes" in cd:
        return Operationto
    else:
        print("Please Say Again Operation to Perform")
        gui.App.entry_2.insert("1.0","Please Say Again Operation to Perform"+"\n")
        speak("Please Say Again Operation to Perform")
        return selection_operation()

def ImplementFileSearch():
    speak("Select From Specified Drive")
    print("\n1 : D \n2 : E\n3 : C\n4 : Desktop\n5 : Documents\n6 : Downloads ")  #speak  #C:\\Users\\princ FOR C DRIVE RUN
    gui.App.entry_2.insert("1.0","\n1 : D \n2 : E\n3 : C\n4 : Desktop\n5 : Documents\n6 : Downloads "+"\n")
    #drive_initialization = input()  #takeCommand().lower() TO PREVENT LOOPING
    drive =  drive_name()    
    print(drive)
    gui.App.entry_2.insert("1.0",drive+"\n")
    print("Does File name contains any special Symbols or Numeric Value ?")
    gui.App.entry_2.insert("1.0","Does File name contains any special Symbols or Numeric Value ?"+"\n")
    speak("Does File name contains any special Symbols or Numeric Value ?") #speak
    filenamespecifier = takecommand_yes()
    if ("yes" in filenamespecifier or "YES" in filenamespecifier or "Yes" in filenamespecifier):
        filename = returnfilename()        
    else:
        filename = returnfilename_withtext()   #takeCommand().lower()

    print(filename)
    gui.App.entry_2.insert("1.0",filename+"\n")
    #my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #to join single alphabetical word in list
    #Filename = ''.join(map(str, filename))
    #print(my_lst_str)
    if (pathc in drive):
        j = returnfile_c(drive,filename) #Pending Function for C://DRIVE
    else:
        j = returnfile(drive,filename) #print(j)

    Index_no = 1

    for i in j:
        print(str(Index_no) + " : " + i)
        gui.App.entry_2.insert("1.0",str(Index_no) + " : " + i+"\n")
        Index_no = Index_no + 1

    #print(len(j))
    if len(j) == 0:
        print("No such file present")
        gui.App.entry_2.insert("1.0","No such file present"+"\n")
        speak("No Such File Present")

    elif len(j) == 1:
        #print(j)
        sf_operations(j[0])

    else:
        print("Do you Want To Perform Operations On Single File or All Files or Multiple Files")
        gui.App.entry_2.insert("1.0","Do you Want To Perform Operations On Single File or All Files or Multiple Files"+"\n")
        speak("Do you Want To Perform Operations On Single File or All Files or Multiple Files")
        skt = selection_operation()  
        if "single file" in skt:
            #speak("Give Index No: ")
            print("Note -> If Files Repeated Choose any one of its Index no. ")
            gui.App.entry_2.insert("1.0","Note -> If Files Repeated Choose any one of its Index no. "+"\n")
            inddex = index_input()   #FROM WORD TO NUMBER REMAINING
            print(j[int(inddex) - 1])
            gui.App.entry_2.insert("1.0",j[int(inddex) - 1]+"\n")
            sf_operations(j[int(inddex) - 1])

        elif ("all" in skt or "all files" in skt or "ALL" in skt or "ALL files" in skt):
            mf_operations(j)

        else:
            print("How Many Files")
            gui.App.entry_2.insert("1.0","How Many Files"+"\n")
            #numberoffiles = input() #constraints regarding numbers and words (strings if input)
            numberoffiles=None
            def get_numberoffiles():
                global numberoffiles
                numberoffiles = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_numberoffiles)
            while numberoffiles is None:
                pass
            b = []
            countup = 0
            print("Enter File Indexes: ")
            gui.App.entry_2.insert("1.0","Enter File Indexes: "+"\n")
            speak("Enter File Indexes: ")
            print("Note -> If Files Repeated Choose any one of its Index no. ")
            gui.App.entry_2.insert("1.0","Note -> If Files Repeated Choose any one of its Index no. "+"\n")
            while(countup < int(numberoffiles)):
             
                def get_data():
                    global data
                    data = gui.App.entry_1_str.get()
                    gui.App.entry_1.delete(0,END)
                gui.App.button_2.config(command=get_data)
                while r is None:
                    pass
                b.append(data)

                countup = countup + 1
            final_files = []
            for i in b:
                final_files.append(j[int(i)-1])
            print(final_files)
            gui.App.entry_2.insert("1.0","Note -> If Files Repeated Choose any one of its Index no. "+"\n")
            mf_operations(final_files)

def openbrowser_website():                                #website-opener
    print("tell me the name of the website with domain name")
    gui.App.entry_2.insert("1.0","tell me the name of the website with domain name"+"\n")
    speak("tell me the name of the website with domain name")
    name = takeCommand().lower()
    web = 'https://www.' + name
    webbrowser.open(web)
    speak("Done Sir!")         
        
def screenshot_ss():                                          #modified version to remove error
    try:
        try:
            os.mkdir(pathc_ss)
        except Exception as e:
            pass
        path1name = ss_name()
        ss = pyautogui.screenshot()
        ss.save(path1name)
        os.startfile(path1name)
        speak("Here Is Your ScreenShot")
        
    except Exception as e:
        print("Sorry no such Path exist")
        gui.App.entry_2.insert("1.0","Sorry no such Path exist"+"\n")
        speak("Sorry no such Path exist")

def ss_name():
    print("Please tell me , What Should I Name That File ?")
    gui.App.entry_2.insert("1.0","Please tell me , What Should I Name That File ?"+"\n")
    speak("Please tell me , What Should I Name That File ?")
    path0 = takecommand()
    path2name = path0 + ".png"
    path3name = pathc_ss + "\\" + path2name
    try:
        if path.exists(path3name):
            print("Filename Already exists Please Rename the file: ")
            gui.App.entry_2.insert("1.0","Filename Already exists Please Rename the file: "+"\n")

            speak("Filename Already exists Please Rename the file: ")
            return ss_name()
        else:
            return path3name
        
    except Exception as e:
        print("Invalid Path cannot take a screenshot")
        gui.App.entry_2.insert("1.0","Invalid Path cannot take a screenshot"+"\n")
        speak("Invalid Path cannot take a screenshot")    #-->It will return None so to be saved as none.png
            
    
def open_file_in_notepad():
    print("Please name the file")
    gui.App.entry_2.insert("1.0","Please name the file"+"\n")
    speak("Please name the file")
    file_name = takecommand()
    print("Is the file name correct")
    gui.App.entry_2.insert("1.0","Is the file name correct"+"\n")
    speak("Is the file name correct")
    cd = takecommand_yes()
    try:
        if "yes" in cd:
            f_name = file_name + ".txt"
            os.startfile(f_name)
        elif "exit" in cd:
            while True:
                break
        else:
            return open_file_in_notepad()
    except Exception as e:
        print("specified file is not present on desktop")
        gui.App.entry_2.insert("1.0","specified file is not present on desktop"+"\n")
        speak("specified file is not present on desktop")
        
def YouTubeAuto():
    speak("youtube auto Initialized")
    while True:
        query = takecommand()
        if "pause" in query:
            press('space bar')

        elif "resume" in query:
            press('space bar')

        elif "full screen" in query or "no full screen" in query:
            press('f')

        elif "film screen" in query or "no film screen" in query:
            press('t')
            
        #elif "skip" in query:           #issues
            #press('l')
            
        elif "backward" in query:
            press('j')

        elif "forward" in query:
            press('l')

        elif "increase speed" in query:
            press_and_release('SHIFT + .')

        elif "decrease speed" in query:
            pyautogui.hotkey('shift', ',')    

        #elif "previous video" in query:
            #press_and_release('SHIFT + p')

        elif "go back" in query:
            press_and_release('Alt +Left arrow')

        elif "next video" in query:
            press_and_release('SHIFT +n')

        elif "mute" in query or "unmute" in query:
            press('m')

        elif "on caption" in query or "on subtitles" in query or "off caption" in query or "off subtitles" in query:
            press('c')
            
        #elif "increase subtitles text" in query or "increase caption text" in query:
            #press('+')

        #elif "decrease subtitles text" in query or "decrease caption text" in query:
            #press('-') 
            
        elif "exit" in query or "quit" in query:
            speak("Youtube Auto Deactivated")
            break
    
def ChromeAuto(query):
    query = query.replace("chrome","")
    query = query.replace("chrome auto", "")
    query = str(query)

    if "new tab" in query:
        press_and_release('ctrl + t')

    elif "close tab" in query:
        press_and_release('ctrl + w')

    elif "new window" in query:
        press_and_release('ctrl + n')

    elif "history" in query:
        press_and_release('ctrl + h')
        
    elif "open downloads" in query or "open download" in query:    
        press_and_release('ctrl + j')

    elif "bookmark this tab" in query or "bookmark tab" in query:
        press_and_release('ctrl + d')
        time.sleep(2)
        press('enter')
        speak("Done")
        
    elif "bookmark all tab" in query:
        press_and_release('ctrl + shift + d')
        time.sleep(2)
        press('enter')
        speak("Done")
     
    elif "open bookmark" in query or "bookmark manager" in query:
        press_and_release('ctrl + shift + O')

    elif "incognito" in query:
        press_and_release('Ctrl + Shift + n')

    elif "switch tab" in query or "go to tab" in query:
        tab = query.replace("switch tab ", "")           
        tab1 = tab.replace("go to tab", "")
        Tab = tab1.replace("to","")
        #print(Tab)
        num = Tab.replace(" ","")   #---> removes space between the _1 to 1
        #print(num)
        try:
            bb = f'ctrl+{num}'
            press_and_release(bb)  #was giving error for hacing spaces i.e. ctrl  +   4 so instead do this ctrl+4 --> take out the spaces in between
        except Exception as e:
            speak("We dont accept None as input")
            
    elif "close all" in query or "close all tabs" in query:
        #speak("closing chrome!!")
        os.system("taskkill /f /im chrome.exe")        #will give invalid request due to itself running in browser so not to worry about it
            
    else:
        speak("Sorry Invalid Request")
        
def WindowsAuto(query):
    query = query.replace("windows","")
    query = query.replace("window","")
    query = str(query)

    if 'home screen' in query or 'minimize' in query:
        press_and_release('windows + m')

    elif 'show start' in query:
        press('windows')

    elif 'open setting' in query or 'open settings' in query:
        press_and_release('windows + i')

    elif 'open search' in query:
        press_and_release('windows + s')

    elif 'restore windows' in query:
        press_and_release('Windows + Shift + M')

    elif "switch" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")
    
    else:
        speak("Sorry Invalid Request")
        
def SearchStackoverflow(query):
    query = query.replace("search on stackoverflow", "")
    query = query.replace("search stackoverflow", "")
    query = query.replace("stackoverflow search", "")
    query = query.replace(" ","")
    url = "https://stackoverflow.com/search?q=" + str(query)
    webbrowser.open_new_tab(url)
    
def news_world():
    try:
        query_params = {"source": "bbc-news","sortBy": "top","apiKey": "dc4398991e3247f1812d5155f05f52a8"}
        main_url = " https://newsapi.org/v1/articles"
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
        article = open_bbc_page["articles"]
        results = []
        speak("Todays News Displayed")
        for ar in article:
            results.append(ar["title"])
        for i in range(len(results)):
            print(i + 1, results[i])
            gui.App.entry_2.insert("1.0",i + 1, results[i]+"\n")
        speak("Do You want me to read for you")
        cd = takecommand_yes()
        if "yes" in cd:
            speak(results)
        else:
            while True:
                break
            
    except Exception as e:
        print("Check your Connection or request limits")
        gui.App.entry_2.insert("1.0","Check your Connection or request limits"+"\n")
        speak("Server Down")
        
        
def internet_speed_test():
    try:
        speak("I Am Checking Speed Sir , Wait For A While .")
        speed = speedtest.Speedtest()
        upload = speed.upload()
        correct_Up = int(int(upload)/800000)
        download = speed.download()
        correct_down = int(int(download)/800000)
        print(f"Downloading Speed Is {correct_down} M B Per Second .")
        gui.App.entry_2.insert("1.0",f"Downloading Speed Is {correct_down} M B Per Second ."+"\n")
        speak(f"Downloading Speed Is {correct_down} M B Per Second .")
        print(f"Uploading Speed Is {correct_Up} M B Per Second .")
        gui.App.entry_2.insert("1.0",f"Uploading Speed Is {correct_Up} M B Per Second ."+"\n")
        speak(f"Uploading Speed Is {correct_Up} M B Per Second .")

    except Exception as e:
        speak("Error Check Internet Connectivity")
        
def where_is(incomingText):
    incomingText = incomingText.replace("find place","")
    incomingText = incomingText.replace("find the place","")
    incomingText = incomingText.replace("find a place","")
    Place = incomingText.replace("where is","")
    try:
        Url_Place = "https://www.google.com/maps/place/" + str(Place)
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(Place , addressdetails= True)
        target_latlon = location.latitude , location.longitude
        webbrowser.open(url=Url_Place)
        location = location.raw['address']
        target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

        current_loca = geocoder.ip('me')
        current_latlon = current_loca.latlng
        distance = str(great_circle(current_latlon,target_latlon))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)
        print(target)
        gui.App.entry_2.insert("1.0",target+"\n")
        speak(target)
        speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")
    
    except Exception as e:
        speak("Invalid Input.")
        
def my_location_key():
    try:
        op = "https://www.google.com/maps/place/"
        print("Checking....")
        gui.App.entry_2.insert("1.0","Checking...."+"\n")
        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        opp = op+state
        webbrowser.open(opp)
        speak(f"Sir , You Are Now In {state , country} .")
        
    except Exception as e:
        speak("Error.Check Internet Connection")
        
def talktome():
    url = "https://chatbot19.p.rapidapi.com/chatbot"
    try:
        while True:
            str1 = takeCommand().lower()                          
            if "bye" in str1 or "good bye" in str1: 
                print("Bye have a good day")
                gui.App.entry_2.insert("1.0","Bye have a good day"+"\n")
                speak("Bye have a good day")
                break        
                
            else:
                payload = "{\r\"message\": \""+ str1 +"\",\r\"language\": \"en\",\r\"context\": [\r\" array of previous message\"\r]\r}"
                headers = {'content-type': "application/json",'x-rapidapi-host': "chatbot19.p.rapidapi.com",'x-rapidapi-key': "1cc0c16a1cmsh6fe2f3944fb171ep1fbdb4jsndb27d8f3d47f"}
                response = requests.request("POST", url, data=payload, headers=headers)
                values = response.text
                dict0 = values.split(":")
                dict1 = dict0[2].split("}")
                dict2= dict1[0]
                if "Internal server error" in dict2:
                    print("sorry out of context")
                    gui.App.entry_2.insert("1.0","sorry out of context"+"\n")
                    speak("sorry out of context")
                else:
                    print(dict2)
                    gui.App.entry_2.insert("1.0",dict2+"\n")
                    speak(dict2)
                
    except Exception as e:
        speak('Sorry Have to go now Bye')   
        
def check_db(filename):
    return os.path.exists(filename)

def hasitin(query):
    c.execute('SELECT CALL from FAVOURITE')
    items = c.fetchall()
    j = []
    for item in items:
        ck = ''.join(map(str, item))
        j.append(ck)
    #print(j)
    if query in j:
        return True
    else:
        return False
    
def show_record(): 
    c.execute('SELECT * from FAVOURITE')
    items = c.fetchall() 
    count = 0
    for item in items:
        count = count + 1
        print(str(count)+" Call: " + item[0] + "\t Path: " + item[1])
        gui.App.entry_2.insert("1.0",str(count)+" Call: " + item[0] + "\t Path: " + item[1]+"\n")
        
def insert_record():
    #n = int(input("Total No."))
    n=None
    gui.App.entry_2.insert("1.0","Total No."+"\n")
    def get_f():
            global f
            f = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
    gui.App.button_2.config(command=get_f)
    while f is None:
        pass
    for i in range(n):
        specify_pathc=None
        #specify_pathc = input("Enter Full Path:")
        gui.App.entry_2.insert("1.0","Enter Full Path:"+"\n")
        def get_specify_pathc():
            global specify_pathc
            specify_pathc = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_f)
        while specify_pathc is None:
            pass
        if os.path.exists(specify_pathc):
            #specify_calling = input("Specify your call:")
            specify_calling=None
            gui.App.entry_2.insert("1.0","Specify your call:"+"\n")
            def get_specify_calling():
                global specify_calling
                specify_calling = gui.App.entry_1_str.get()
                gui.App.entry_1.delete(0,END)
            gui.App.button_2.config(command=get_specify_calling)
            while specify_calling is None:
                pass
            many_pathc = [   
                        (specify_calling,specify_pathc),
                        ]
            try:
                c.executemany("INSERT INTO FAVOURITE (CALL,PATH) VALUES (?,?);",many_pathc)
                print ("Records Manual created successfully")
                gui.App.entry_2.insert("1.0","Records Manual created successfully"+"\n")
            
            except Exception as e:
                print("Call Name already Exists")
                gui.App.entry_2.insert("1.0","Call Name already Exists"+"\n")
                
        else:
            print("No such path exists")
            gui.App.entry_2.insert("1.0","No such path exists"+"\n")
        
    conn.commit()
    
    
def delete_record():
    show_record() 
    print("Specify Call:")
    gui.App.entry_2.insert("1.0","Specify Call:"+"\n")

    cd = input()
    cd=None
    def get_cd():
        global specify_calling
        cd = gui.App.entry_1_str.get()
        gui.App.entry_1.delete(0,END)
    gui.App.button_2.config(command=get_cd)
    while specify_calling is None:
        pass
    try:
        if hasitin(cd):
            many_call = [
                (cd)
            ]
            c.execute("DELETE from FAVOURITE WHERE CALL = (?);",many_call)
            print("Deleted record")  
            gui.App.entry_2.insert("1.0","Deleted record"+"\n")       
        else:
            print("No such Call exists")
            gui.App.entry_2.insert("1.0","No such Call exists"+"\n")
        
    except Exception as e:
        print("Invalid Input Sir")
        gui.App.entry_2.insert("1.0","Invalid Input Sir"+"\n")
        
    conn.commit()
        
def choice_selection():
    while True:
        print("\nOperations To Perform : \n1:Show\n2:Insert Record\n3:Delete Record\n4:Quit\nEnter your choice:\n")
        gui.App.entry_2.insert("1.0","\nOperations To Perform : \n1:Show\n2:Insert Record\n3:Delete Record\n4:Quit\nEnter your choice:\n"+"\n")
        #int_choice = input()
        int_choice=None
        def get_int_choice():
            global int_choice
            int_choice = gui.App.entry_1_str.get()
            gui.App.entry_1.delete(0,END)
        gui.App.button_2.config(command=get_int_choice)
        while specify_calling is None:
            pass
        if "1" in int_choice:
            show_record()
        elif "2" in int_choice:
            insert_record()
        elif "3" in int_choice:
            delete_record()
        elif "4" in int_choice:
            break
        else:
            print("Invalid Input")
            gui.App.entry_2.insert("1.0","Invalid Input"+"\n")

def open_my_favourite():
    print("Welcome to Easy Access. Here you can add CALL and PATH for files that you want instant access to.\n")
    gui.App.entry_2.insert("1.0","Welcome to Easy Access. Here you can add CALL and PATH for files that you want instant access to.\n"+"\n")
    speak("Welcome to Easy Access Here you can add CALL and PATH for files that you want instant access to")
    
    if check_db(database1):
        pass
    else:
        print ("Opened database successfully")
        gui.App.entry_2.insert("1.0","Opened database successfully"+"\n")

    try:
        c.execute('''CREATE TABLE FAVOURITE
                 (CALL TEXT PRIMARY KEY NOT NULL,
                 PATH TEXT NOT NULL);''')
        print ("Table created successfully")
        gui.App.entry_2.insert("1.0","Table created successfully"+"\n")
        conn.commit()

    except Exception as e:
        pass
    
    choice_selection()         
            
        
def solutionFinder(incomingText):
    """
    answer = ''
    if 'music' in incomingText:
        if 'play music' in incomingText:
            print("2")
            s.playSong()

        if 'next music' in incomingText:
            s.nextSong()

        if 'previous music' in incomingText:
            s.previousSong()

        if 'stop music' in incomingText:
            print("3")
            s.stopSong()

    else:
    """
    if 'implement file search' in incomingText:
        ImplementFileSearch()

    elif 'open website' in incomingText:
        openbrowser_website()

    elif 'screenshot' in incomingText:
        screenshot_ss()
      
    elif ('open desktop file in notepad' in incomingText or 'open desktop file notepad' in incomingText or 'desktop file in notepad' in incomingText or 'open desktop file' in incomingText):
        open_file_in_notepad()
        
    elif 'play on youtube' in incomingText  or 'youtube play' in incomingText or 'play youtube' in incomingText:
        incomingText = incomingText.replace("play on youtube", "")
        incomingText = incomingText.replace("youtube play", "")
        incomingText = incomingText.replace("play youtube","")
        pywhatkit.playonyt(incomingText)
        
    elif 'search on youtube' in incomingText  or 'youtube search' in incomingText or 'search youtube' in incomingText:
        yt1 = incomingText.replace("search on youtube", "")
        yt2 = yt1.replace("youtube search", "")
        yt = yt2.replace("search youtube ", "")
        webbrowser.open("https://www.youtube.com/results?search_query=" + str(yt)) 
        speak("here you go!!! ") 
        
    elif 'implement youtube auto' in incomingText:
        YouTubeAuto()
        
    elif 'search on google' in incomingText or 'google search' in incomingText or 'search google' in incomingText:
        incomingText = incomingText.replace("google", "")
        incomingText = incomingText.replace("search", "")
        incomingText = incomingText.replace("on","")
        pywhatkit.search(incomingText)
        
    elif 'chrome' in incomingText:
        ChromeAuto(incomingText)   
    
    elif "window" in incomingText or "windows" in incomingText:
        WindowsAuto(incomingText)

    elif "open command prompt" in incomingText or "open cmd" in incomingText:                 #Try to close the app too -- solved
        os.system("start cmd")
        
    elif "open google" in incomingText:                               
        webbrowser.open("https://www.google.co.in/")

    elif "open wikipedia" in incomingText:                           
        webbrowser.open("https://en.wikipedia.org/")

    elif "open telegram" in incomingText:                              
        webbrowser.open("https://web.telegram.org/")
        
    elif "open facebook" in incomingText:                               
         webbrowser.open("https://fb.com/")

    elif "open whatsapp" in incomingText:                               
        webbrowser.open("https://web.whatsapp.com/")

    elif "open gmail" in incomingText:                               
        webbrowser.open("https://mail.google.com/")

    elif "open stackoverflow" in incomingText:                            
        webbrowser.open("https://stackoverflow.com/")
    
    elif "close notepad" in incomingText:
        speak("closing notepad!! ")
        os.system("taskkill /f /im notepad.exe")
        speak("done")

    elif "close cmd" in incomingText or "close command prompt" in incomingText:
        speak("closing cmd!!")
        os.system("taskkill /f /im cmd.exe")
        speak("done")
        
    elif "search on stackoverflow" in incomingText or "stackoverflow search" in incomingText or "search stackoverflow" in incomingText:   #searches for query 
        SearchStackoverflow(incomingText)
        
    elif "ip address" in incomingText:
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)   
        speak("Your Computer Name is:" + hostname)  
        print("Your Computer Name is:" + hostname)
        gui.App.entry_2.insert("1.0","Your Computer Name is:" + hostname+"\n")
        speak("Your Computer IP Address is:" + IPAddr)
        print("Your Computer IP Address is:" + IPAddr)
        gui.App.entry_2.insert("1.0","Your Computer IP Address is:" + IPAddr+"\n")

        
    elif "tell me a joke" in incomingText or "make me laugh" in incomingText:             #
        joke = pyjokes.get_joke()
        print(joke)
        gui.App.entry_2.insert("1.0",joke+"\n")
        speak(joke)
        
    elif "shutdown system" in incomingText:                                               #
        os.system("shutdown /s /t 5")
        
    elif "restart system" in incomingText:                                                #
        os.system("shutdown /r /t 5")
        
    elif "news" in incomingText or "important headlines" in incomingText:                                                          #
        news_world()
    
    elif "speed test" in incomingText or "test speed" in incomingText:
        internet_speed_test()
        
    elif "find place" in incomingText or "find the place" in incomingText or "find a place" in incomingText or "where is" in incomingText:
        where_is(incomingText)
        
    elif "my location" in incomingText:
        my_location_key()
        
    elif "talk to me" in incomingText or "lets talk" in incomingText or "can we chat" in incomingText:     #-->change api-id please
        speak("Yeah Go ahead")
        talktome()
    
    elif "open my favourite" in incomingText:
        open_my_favourite()
        
    elif hasitin(incomingText):
        many_call = [
            (incomingText)
        ]
        c.execute("SELECT PATH from FAVOURITE WHERE CALL = (?);",many_call)
        item = c.fetchall()
        item_path = item[0]
        item_path = ''.join(map(str, item_path))
        print(item_path)
        gui.App.entry_2.insert("1.0",item_path+"\n")
        os.startfile(item_path)
        print("Executing properly")
        gui.App.entry_2.insert("1.0","Executing properly"+"\n")
        
        
if __name__ == "__main__":
    #gui.window.mainloop()
    #threading.Thread(target= main).start()
    #gui.window(0,main)
    #gui.window.mainloop()
    threading.Thread(target= main).start()
    #threading.Thread(target=gui.mainloop).start()
    gui.window.mainloop()
    
    #main()
    #gui.window.update()
    #t.start()
    #gui.window.after(0,main)
    
    

"""
Possible reasons error comes during file search is not providing right path or administrator name;
it will give none or not such file present as output/speak
other possible errors may occur due to absence of particular library
also change api id to new account
PROGRESSBAR --> SPEEDTEST FUNCTION
"""
