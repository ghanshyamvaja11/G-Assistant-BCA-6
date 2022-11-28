import os
import sys
import mysql.connector
import socket
import speech_recognition as sr
import pyttsx3
import pyaudio
import tkinter
from tkinter import *
import subprocess
import ctypes
import math
import re
import random
import datetime
import time
import wikipedia
import webbrowser
import winshell
import pyjokes
import ecapture
import win32com.client as wincl
import pywhatkit as pwk
from PIL import Image, ImageTk
from pytube import YouTube

##############################################DATABASE CONNECTION###################################################
myconn = ''
mycursor = ''
result = ''
email = ''
Email = ''
User = '' 
TName = ''
checkRecord = ''
emailValidate = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PasswordValidate = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,42}$"

#########################################################Database Connection#########################################################################
def dbConnection():
    # myconn = mysql.connector.connect(
    # host="db4free.net",
    # user="g402349",
    # password="G@402349",
    # database="g402349"
    # )
    try: 
        myconn = mysql.connector.connect(
        host="sql5.freesqldatabase.com",
        user="sql5531033",
        password="3RFNy7cent",
        database="sql5531033"
        )
        mycursor = myconn.cursor()
    except:
        print("\nInternal Server Error, Please try to open G Assistent After some time")
        speak("Internal Server Error, Please try to open G Assistent After some time")
        return False

#####Login Method
def Login():
    connStatus = dbConnection()
    if(connStatus == False):
        sys.exit()

    speak("Enter your Registered email in command prompt")
    email = input("Enter your registered email : ")
    while re.match(emailValidate, email):
        break
    else: 
        speak("enter valid email in command prompt")
        email = input("Enter valid Email : ")
        while re.search(emailValidate, email) == None:
            speak("enter valid email in command prompt")
            email = input("Enter valid Email : ")
    speak("Enter your Password in command prompt")
    password = input("Enter your Password : ")
    email = email.lower()
    sql = f"SELECT *FROM Users WHERE Email = '{email}' and Password = '{password}' "
    mycursor.execute(sql)
    checkRecord = mycursor.fetchone()
    while checkRecord is None:
            speak("your entered details is not matched in our database")
            speak("enter your registered email in command prompt")
            email = input("Enter your registered Email : ")
            speak("Enter your Password in command prompt")
            password = input("Enter your Password : ")
            email = email.lower()
            sql = f"SELECT *FROM Users WHERE Email = '{email}' and Password = '{password}' "
            mycursor.execute(sql)
            checkRecord = mycursor.fetchone()
    if checkRecord is not None:
        global User
        global Email
        Email = checkRecord[0]
        Email = Email.replace(',', '')
        User = checkRecord[1]
        User = User.replace(',','')
        speak(f"Hi, {User} Your Authentication is Done now you can use G Assistent....")

#####Signup Method
def Signup():
    connStatus = dbConnection()
    if connStatus == False:
        sys.exit()

    speak("Enter your Name in command prompt")
    Name = input("Enter your Name : ")
    speak("Enter your email in command prompt")
    email = input("Enter your email : ")
    while re.match(emailValidate, email):
        break
        pass
    else:
        speak("enter valid email in command prompt")
        email = input("Enter valid Email : ")
        while re.match(emailValidate, email):
            break
            pass
        else:
            speak("enter valid email in command prompt")
            email = input("Enter valid Email : ")
    speak("Enter Password in command prompt")
    Password = input("Enter Password : ")
    res = re.search(PasswordValidate, Password)
    email = email.lower()
    sql = f"SELECT *FROM Users WHERE Email = '{email}'"
    mycursor.execute(sql)
    checkRecord = mycursor.fetchone()
    while checkRecord is None:
            break
    while re.search(emailValidate, email) == None:
            speak("enter valid email in command prompt")
            email = input("Enter valid Email : ")
    while res == None:
        print("\n Warning : \nMinimum password length is needs required more than 8 character")
        print("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
        speak("Warning")
        speak("Minimum password length is nneds too be required more than 8 character")
        speak("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
        speak("Enter password in valid  format ")
        Password = input("Enter password in valid format : ")
        res = re.search(PasswordValidate, Password)
    while checkRecord is not None:
        speak("This email is registered in our database try to enter different email")
        email = input("Enter different Email : ")
        while re.search(emailValidate, email) == None:
            speak("enter valid email in command prompt")
            email = input("Enter valid Email : ")
        speak("Enter Password")
        Password = input("Enter Password : ")
        res = re.search(PasswordValidate, Password)
        while res == None:
            print("\n Warning : \nMinimum password length is needs required more than 8 character")
            print("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
            speak("Warning")
            speak("Minimum password length is nneds too be required more than 8 character")
            speak("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
            speak("Enter password in valid  format ")
            Password = input("Enter password in valid format : ")
            res = re.search(PasswordValidate, Password)
        email = email.lower()
        sql = f"SELECT *FROM Users WHERE Email = '{email}'"
        mycursor.execute(sql)
        checkRecord = mycursor.fetchone()
    email = email.lower()
    sql = f"SELECT *FROM Users WHERE Email = '{email}'"
    mycursor.execute(sql)
    checkRecord = mycursor.fetchone()
    if mycursor.rowcount:
        #####Create User Table
        TName = email.lower()
        TName = TName.replace("@","_")
        TName = TName.replace(".","_")
        if checkRecord is None:
            email = email.lower()
            sql = "Insert into Users(Email, Name, Password, QueryTable)VALUES(%s, %s, %s, %s)"
            val = (email, Name, Password, TName)
            mycursor.execute(sql, val)
            myconn.commit()
        if res is not None:
        	mycursor.execute(f"CREATE TABLE {TName} (Query VARCHAR(150), Host VARCHAR(59), IPAddress VARCHAR(65), DateAndTime VARCHAR(59))")
        email.lower()
        sql = f"SELECT *FROM Users WHERE Email = '{email}' and Password = '{Password}' "
        mycursor.execute(sql)
        checkRecord = mycursor.fetchone()
        User = checkRecord[1]
        User = User.replace(',','')
        if True:
            speak(f"Hi, {User} Your registration is Successfully completed now you can use G Assistent After login....")
            Login()
        else:
            speak("Something went Wrong try again to Signup")
            Signup()

def DeleteAccount():
    connStatus = dbConnection()
    if connStatus == False:
        sys.exit()

    speak("Enter your Registered email in command prompt")
    email = input("Enter your registered email : ")
    while re.match(emailValidate, email):
        break
    else: 
        speak("enter valid email in command prompt")
        email = input("Enter valid Email : ")
    speak("Enter your Password in command prompt")
    password = input("Enter your Password : ")
    email = email.lower()
    sql = f"SELECT *FROM Users WHERE Email = '{email}' and Password = '{password}' "
    mycursor.execute(sql)
    checkRecord = mycursor.fetchone()
    User = checkRecord[1]
    User = User.replace(',','')
    while checkRecord is None:
            speak("your entered details is not matched in our database")
            speak("enter your registered email in command prompt")
            email = input("Enter your registered Email : ")
            speak("Enter your Password in command prompt")
            password = input("Enter your Password : ")
            email = email.lower()
            sql = f"SELECT *FROM Users WHERE Email = '{email}' and Password = '{password}' "
            mycursor.execute(sql)
            checkRecord = mycursor.fetchone()
            Name = checkRecord[0]
            Name = Name.replace(',', '')
    TName = email.replace("@","_")
    TName = TName.replace(".","_")
    email = email.lower()
    sql2 = f"DELETE FROM Users WHERE Email = '{email}'"
    sql3 = f"DROP TABLE {TName}"
    mycursor.execute(sql2)
    if mycursor.rowcount:
        speak(f"Hi, {User} your account is deleted successfully.....")
    myconn.commit()
    mycursor.execute(sql3)
        
# def CT():   
#     	res = mycursor.execute(f"CREATE TABLE Users (Email VARCHAR(59) primary key, Name VARCHAR(59), Password VARCHAR(59), QueryTable VARCHAR(59))")
#     	if res:
#     		print("Table is Created Successfully.....")
####################################################################################################################

##############################Guess The Number Console Game#########################################################
def GuessNumber() :
        print("Welcome in Number Guessing Game \n")
        speak("Welcome in Number Guessing Game")
        print("Application Type : Console Game")
        speak("Application Type : Console Game")
        print("Version : 2.0.1 LTS")
        speak("Version : 2.0.1 LTS")
        print("Developer : GHANSHYAM VAJA","\n")
        speak("Developer : GHANSHYAM vaja")
        rand = 0
        randomNumber = 0
        userNumber = 0
        chooseLevel = 0
        easyCount = 5
        mediumCount = 7
        hardCount = 10
        ultrahardCount = 15
        leftCount = 0

        print("    Level         Range       Turns")
        print("1 - Easy       (1 to 100)       5\n2 - Medium     (1 to 1000)      7\n3 - Hard       (1 to 10000)     10\n4 - Ultra Hard (1 to 100000)    15")
        speak("1 for Easy       Range = 1 to 100       turns = 5\n")
        speak("2 for Medium     Range = 1 to 1000      turns=7\n")
        speak("3 for Hard       Range=1 to 10000     turns=10\n")
        speak("4 for Ultra Hard Range=1 to 100000    turns=15")
        print(" \nChoose Level(1 | 2 | 3 | 4 ) : ", end ="")
        speak("Choose Level between 1 to 4")
        chooseLevel = int(input())
        while (chooseLevel <= 0 or chooseLevel > 4) :
            print("Choose Level(1 | 2 | 3 | 4) : ", end ="")
            speak("Choose Level")
            chooseLevel = int(input())
        if (chooseLevel == 1) :
            randomNumber = random.randint(0, 101)
        elif(chooseLevel == 2) :
            randomNumber = random.randint(0, 1001)
        elif(chooseLevel == 3) :
            randomNumber = random.randint(0, 10001)
        else :
            randomNumber = random.randint(0,100001)
        while True :
            if (easyCount == 0 or mediumCount == 0 or hardCount == 0 or ultrahardCount == 0) :
                print("\n---------------------------------------------")
                print("GAME OVER", end ="")
                speak("GAME OVER")
                break
            print(" \nGuess A Number Between 1 To ", end ="")
            speak(" \nGuess A Number Between 1 To")
            if (chooseLevel == 1) :
                easyCount -= 1
                leftCount = easyCount
                print("100", end ="")
                speak("100")
            elif(chooseLevel == 2) :
                mediumCount -= 1
                leftCount = mediumCount
                print("1000", end ="")
                speak("1000")
            elif(chooseLevel == 3) :
                hardCount -= 1
                leftCount = hardCount
                print("10000", end ="")
                speak("10000")
            else :
                ultrahardCount -= 1
                leftCount = ultrahardCount
                print("100000", end ="")
                speak("100000")
            print(" : ", end ="")
            userNumber = int(input())
            if (userNumber == randomNumber) :
                print("\n---------------------------------------------")
                print(" \nCongratulations, Your Guess Is Correct, YOU WON.....")
                speak("Congratulations, Your Guess Is Correct, YOU WON.....")
            elif(userNumber > randomNumber) :
                print("Your Guess Is Large     Available Turn : " + str(leftCount))
                speak("Your Guess Is Large")
                speak("Available Turn : " + str(leftCount))
            elif(userNumber > 0) :
                print("Your Guess Is Small     Available Turn : " + str(leftCount))
                speak("Your Guess Is Small")
                speak("Available Turn : " + str(leftCount))
            if((userNumber > 0) == False) :
                    break
        print(" \n---------------------------------------------")
        print("Your Answer Is : ")
        print(randomNumber)
        speak("Your Answer Is ")
        speak(randomNumber)
        print("---------------------------------------------")
###################################################################################################################

####################################Snake and Ladder Console Game##################################################
class Play_With_Computer :
    WONPOINT = 100
    rand =  random.randint(1, 7)
    rollDice = ' '
    playerPosition = 0
    computerPosition = 0
    playerDice = 0
    computerDice = 0
    Name = None
    Snake_Mouth_Position = [0] * (8)
    Snake_Tail_Position = [0] * (8)
    Ladder_Up_Position = [0] * (8)
    Ladder_Down_Position = [0] * (8)
    flag = 0
    Level = ' '
    ctr = 0
    def PlayerAndComputerPosition(self) :
                if (Play_With_Computer.playerPosition > Play_With_Computer.WONPOINT) :
                    Play_With_Computer.playerPosition -= Play_With_Computer.playerDice
                if (Play_With_Computer.computerPosition > Play_With_Computer.WONPOINT) :
                    Play_With_Computer.computerPosition -= Play_With_Computer.computerDice
                # playerPosition With Snake_Tail_Position
                i = 0
                while (i < 8) :
                    if (self.Level == '1' and i < 3) :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Snake_Tail_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Snake_Tail_Position[i]
                    elif(self.Level == '2' and i < 5) :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Snake_Tail_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Snake_Tail_Position[i]
                    else :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Snake_Tail_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Snake_Tail_Position[i]
                    i += 1
                # playerPosition With Ladder
                i = 0
                while (i < 8) :
                    if (self.Level == '1' and i < 3) :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Ladder_Up_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Ladder_Up_Position[i]
                    elif(self.Level == '2' and i < 5) :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Ladder_Up_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Ladder_Up_Position[i]
                    else :
                        if (Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.playerPosition = Play_With_Computer.Ladder_Up_Position[i]
                        elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[i]) :
                            Play_With_Computer.computerPosition = Play_With_Computer.Ladder_Up_Position[i]
                    i += 1
                # player position display
                print("\n--------------------->Player\'s Position<---------------------------")
                speak("Player\'s Position")
                i = 0
                while (i < 2) :
                    if (i == 0) :
                        print(f" \n                         YOU -> {Play_With_Computer.Name}  = {Play_With_Computer.playerPosition}")
                        speak(f" \n                         YOU -> {Play_With_Computer.Name}  = {Play_With_Computer.playerPosition}")
                    else :
                        print(f"                         COMPUTER = {Play_With_Computer.computerPosition}")
                        speak(f"                         COMPUTER = {Play_With_Computer.computerPosition}")
                    i += 1
    def IsWon(self) :
        if (Play_With_Computer.playerPosition == Play_With_Computer.WONPOINT) :
            print("\n---------------------WINNER------------------------------- \n")
            print(f"                          CONGRATS {Play_With_Computer.Name}")
            print("\n---------------------WINNER------------------------------- \n")
            speak("\n---------------------WINNER------------------------------- \n")
            speak(f"                          CONGRATS {Play_With_Computer.Name}")
            speak("\n---------------------WINNER------------------------------- \n")
            self.flag = 1
        if (Play_With_Computer.computerPosition == Play_With_Computer.WONPOINT) :
            print("\n--------------------------------WINNER---------------------------- \n")
            print("                              COMPUTER \n")
            print("                            YOU LOSE !!!!!")
            print("\n------------------------------------------------------------------ \n")
            speak("WINNER")
            speak("COMPUTER")
            speak("YOU LOSE")
            self.flag = 1
    # setGame()
    def setGame(self) :
        print("-------------------------->SET GAME<------------------------------- \n", end ="")
        speak("SET GAME")
        print("         Levels :   1 - EASY     2 - MEDIUM     3 - HARD \n \n", end ="")
        speak("Levels")
        speak("1 - EASY")
        speak("2 - MEDIUM")
        speak("3 - HARD")
        print("Choose a Level (1 | 2 | 3 ) : ", end ="")
        speak("Choose a Level")
        speak("1 or 2 or 3 ")
        self.Level = input()[0]
        while (self.Level != '1' and self.Level != '2' and self.Level != '3') :
            print("Choose a valid Level (1 | 2 | 3 ) : ", end ="")
            speak("Choose a valid Level")
            self.Level = input()[0]
        print(" \nEnter Your Name : ", end ="")
        speak("Enter Your Name")
        Play_With_Computer.Name = input()
    def SnakesAndLaddersPosition(self) :
        if (self.Level == '1') :
            # Snake Mouth Position Setting
            Play_With_Computer.Snake_Mouth_Position[0] = random.randint(95, (99 - 95) + 95)
            Play_With_Computer.Snake_Mouth_Position[1] = random.randint(60, (65 - 60) + 60)
            Play_With_Computer.Snake_Mouth_Position[2] = random.randint(30, (35 - 30) + 30)
            # Snake Tail Position Setting
            Play_With_Computer.Snake_Tail_Position[0] = random.randint(24, (26 - 24) + 24)
            Play_With_Computer.Snake_Tail_Position[1] = random.randint(51, (56 - 51) + 51)
            Play_With_Computer.Snake_Tail_Position[2] = random.randint(15, (19 - 15) + 15)
        elif(self.Level == '2') :
            # Snake Mouth Position Setting
            Play_With_Computer.Snake_Mouth_Position[0] = random.randint(98, (99 - 98) + 98)
            Play_With_Computer.Snake_Mouth_Position[1] = random.randint(87, (87 - 81) + 81)
            Play_With_Computer.Snake_Mouth_Position[2] = random.randint(55, (59 - 55) + 55)
            Play_With_Computer.Snake_Mouth_Position[3] = random.randint(32, (38 - 32) + 32)
            Play_With_Computer.Snake_Mouth_Position[4] = random.randint(15, (19 - 15) + 15)
            # Snake Tail Position Setting
            Play_With_Computer.Snake_Tail_Position[0] = random.randint(51, (56 - 51) + 51)
            Play_With_Computer.Snake_Tail_Position[1] = random.randint(72, (78 - 72) + 72)
            Play_With_Computer.Snake_Tail_Position[2] = random.randint(41, (42 - 41) + 41)
            Play_With_Computer.Snake_Tail_Position[3] = random.randint(26, (29 - 26) + 26)
            Play_With_Computer.Snake_Tail_Position[4] = random.randint(6,  (9 - 6) + 6)
        else :
            # Snake Mouth Position Setting
            Play_With_Computer.Snake_Mouth_Position[0] = random.randint(98, (99 - 98) + 98)
            Play_With_Computer.Snake_Mouth_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_Computer.Snake_Mouth_Position[2] = random.randint(71, (74 - 71) + 71)
            Play_With_Computer.Snake_Mouth_Position[3] = random.randint(62, (65 - 62) + 62)
            Play_With_Computer.Snake_Mouth_Position[4] = random.randint(41, (42 - 41) + 41)
            Play_With_Computer.Snake_Mouth_Position[5] = random.randint(65, (69 - 65) + 65)
            Play_With_Computer.Snake_Mouth_Position[6] = random.randint(24, (26 - 24) + 24)
            Play_With_Computer.Snake_Mouth_Position[7] = random.randint(15, (19 - 15) + 15)
            # Snake Tail Position Setting
            Play_With_Computer.Snake_Tail_Position[0] = random.randint(51, (56 - 51) + 51)
            Play_With_Computer.Snake_Tail_Position[1] = random.randint(41, (45 - 41) + 41)
            Play_With_Computer.Snake_Tail_Position[2] = random.randint(32, (36 - 32) + 32)
            Play_With_Computer.Snake_Tail_Position[3] = random.randint(22, (26 - 22) + 22)
            Play_With_Computer.Snake_Tail_Position[4] = random.randint(26, (29 - 26) + 26)
            Play_With_Computer.Snake_Tail_Position[5] = random.randint(15, (19 - 15) + 15)
            Play_With_Computer.Snake_Tail_Position[6] = random.randint(15, (19 - 15) + 15)
            Play_With_Computer.Snake_Tail_Position[7] = random.randint(6, (9 - 6) + 6)
        if (self.Level == '1') :
            # Ladder Down Position Setting
            Play_With_Computer.Ladder_Down_Position[0] = random.randint(6, (9 - 6) + 6)
            Play_With_Computer.Ladder_Down_Position[1] = random.randint(65, (69 - 65) + 65)
            Play_With_Computer.Ladder_Down_Position[2] = random.randint(87, (87 - 81) + 81)
            # Laddet Up Position Setting
            Play_With_Computer.Ladder_Up_Position[0] = random.randint(81, (87 - 81) + 81)
            Play_With_Computer.Ladder_Up_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_Computer.Ladder_Up_Position[2] = random.randint(96, (99 - 96) + 96)
        elif(self.Level == '2') :
            # Ladder Down Position Setting
            Play_With_Computer.Ladder_Down_Position[0] = random.randint(15, (19 - 15) + 15)
            Play_With_Computer.Ladder_Down_Position[1] = random.randint(37, (38 - 37) + 37)
            Play_With_Computer.Ladder_Down_Position[2] = random.randint(51, (59 - 51) + 51)
            Play_With_Computer.Ladder_Down_Position[3] = random.randint(65, (69 - 65) + 65)
            Play_With_Computer.Ladder_Down_Position[4] = random.randint(81, (86 - 81) + 81)
            # Ladder Up Position Setting
            Play_With_Computer.Ladder_Up_Position[0] = random.randint(81, (86 - 81) + 81)
            Play_With_Computer.Ladder_Up_Position[1] = random.randint(41, (42 - 41) + 41)
            Play_With_Computer.Ladder_Up_Position[2] = random.randint(81, (86 - 81) + 81)
            Play_With_Computer.Ladder_Up_Position[3] = random.randint(92, (96 - 92) + 92)
            Play_With_Computer.Ladder_Up_Position[4] = random.randint(96, (99 - 96) + 96)
        else :
            # Ladder Down Position Setting
            Play_With_Computer.Ladder_Down_Position[0] = random.randint(6, (9 - 6) + 6)
            Play_With_Computer.Ladder_Down_Position[1] = random.randint(24, (26 - 24) + 24)
            Play_With_Computer.Ladder_Down_Position[2] = random.randint(36, (38 - 36) + 36)
            Play_With_Computer.Ladder_Down_Position[3] = random.randint(41, (45 - 41) + 41)
            Play_With_Computer.Ladder_Down_Position[4] = random.randint(54, (59 - 54) + 54)
            Play_With_Computer.Ladder_Down_Position[5] = random.randint(68, (69 - 68) + 68)
            Play_With_Computer.Ladder_Down_Position[6] = random.randint(72, (78 - 72) + 72)
            Play_With_Computer.Ladder_Down_Position[7] = random.randint(81, (86 - 81) + 81)
            # Ladder Up Position Setting
            Play_With_Computer.Ladder_Up_Position[0] = random.randint(81, (87 - 81) + 81)
            Play_With_Computer.Ladder_Up_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_Computer.Ladder_Up_Position[2] = random.randint(74, (78 - 74) + 74)
            Play_With_Computer.Ladder_Up_Position[3] = random.randint(65, (69 - 65) + 65)
            Play_With_Computer.Ladder_Up_Position[4] = random.randint(81, (87 - 81) + 81)
            Play_With_Computer.Ladder_Up_Position[5] = random.randint(74, (78 - 74) + 74)
            Play_With_Computer.Ladder_Up_Position[6] = random.randint(95, (96 - 95) + 95)
            Play_With_Computer.Ladder_Up_Position[7] = random.randint(92, (99 - 92) + 92)
    def SnakesAndLaddersPositionPrint(self) :
        print(" \n-------->SNAKES POSITION           |      LADDERS POSITION <--------- \n", end ="")
        speak("SNAKES POSITION and LADDERS POSITION")
        if (self.Level == '1') :
            i = 0
            while (i < 3) :
                if (i == 0) :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    0{Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                i += 1
        elif(self.Level == '2') :
            i = 0
            while (i < 5) :
                if (i == 0) :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                elif(i == 4) :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   0{Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                i += 1
        else :
            i = 0
            while (i < 8) :
                if (i == 0) :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    0{Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                elif(i == 7) :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   0{Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_Computer.Snake_Mouth_Position[i]}     to   {Play_With_Computer.Snake_Tail_Position[i]}      |    {Play_With_Computer.Ladder_Down_Position[i]}     to    {Play_With_Computer.Ladder_Up_Position[i]}")
                i += 1
        print("------------------------------------------------------------------- \n", end ="")
    def RollDice(self) :
        print(" \n----------------------->Roll The Dice<-----------------------------\n", end ="")
        speak("Roll The Dice")
        print(f" \n            {Play_With_Computer.Name}\'s Turn (Enter character \"R\" or \"r\" ) : ", end ="")
        speak("Enter character Capital or Small R")
        Play_With_Computer.rollDice = input()
        while (Play_With_Computer.rollDice != 'R' and Play_With_Computer.rollDice != 'r') :
            print("               Enter Valid Character R or r : ", end ="")
            speak("Enter Valid Character Capital or Small R")
            Play_With_Computer.rollDice = input()
        Play_With_Computer.playerDice = random.randint(1, (6 - 1) + 1)
        Play_With_Computer.playerPosition += Play_With_Computer.playerDice
        print(f"                     Your Dice Score : {Play_With_Computer.playerDice}")
        I = 0
        while (I < 8) :
            if (self.Level == '1' and I < 3) :
                if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(f" \n        --------->Oops, {Play_With_Computer.Name} Swallowed By Snake<---------")
                    speak(f"Oops, {Play_With_Computer.Name} Swallowed By Snake")
                elif(Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(f" \n            ----->Hurry, {Play_With_Computer.Name} Climb Up The Ladder<-----")
                    speak(f">Hurry, {Play_With_Computer.Name} Climb Up The Ladder")
            elif(self.Level == '2' and I < 5) :
                if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(f" \n        --------->Oops, {Play_With_Computer.Name} Swallowed By Snake<---------")
                    speak(f"nOops, {Play_With_Computer.Name} Swallowed By Snake")
                elif(Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(f" \n            ----->Hurry, {Play_With_Computer.Name} Climb Up The Ladder<-----")
                    speak(f"Hurry, {Play_With_Computer.Name} Climb Up The Ladder")
            else :
                if (Play_With_Computer.playerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(f" \n        --------->Oops, {Play_With_Computer.Name} Swallowed By Snake<---------")
                    speak(f"Oops, {Play_With_Computer.Name} Swallowed By Snake")
                elif(Play_With_Computer.playerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(f" \n            ----->Hurry, {Play_With_Computer.Name} Climb Up The Ladder<-----")
                    speak(f"Hurry, {Play_With_Computer.Name} Climb Up The Ladder")
            I += 1
        print("\n                   Computer\'s Turn (Wait) : ", end ="")
        speak("Computer\'s Turn (Wait)")
        Play_With_Computer.computerDice = random.randint(1, (6 - 1) + 1)
        Play_With_Computer.computerPosition += Play_With_Computer.computerDice
        try :
            # Thread
            k = 0
            while (k < 5) :
                Thread.sleep(501)
                k += 1
        except Exception as expn :
            if (random.randint(6, (9 - 6) + 6)% 2 == 0) :
                print(f"R \n                   Computer\'s Dice Score : {Play_With_Computer.computerDice}")
            else :
                print(f"r \n                   Computer\'s Dice Score : {Play_With_Computer.computerDice}")
            I = 0
        while (I < 8) :
            if (self.Level == '1' and I < 3) :
                if (Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(" \n       -------->Computer Swallowed By Snake<---------")
                    speak("Computer Swallowed By Snake")
                elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(" \n       -------->Computer Climb Up The Ladder<-------")
                    speak("Computer Climb Up The Ladder")
            elif(self.Level == '2' and I < 5) :
                if (Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(" \n       -------->Computer Swallowed By Snake<---------")
                    speak("Computer Swallowed By Snake")
                elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(" \n       -------->Computer Climb Up The Ladder<-------")
                    speak("Computer Climb Up The Ladder")
            else :
                if (Play_With_Computer.computerPosition == Play_With_Computer.Snake_Mouth_Position[I]) :
                    print(" \n       -------->Computer Swallowed By Snake<---------")
                    speak("Computer Swallowed By Snake")
                elif(Play_With_Computer.computerPosition == Play_With_Computer.Ladder_Down_Position[I]) :
                    print(" \n       -------->Computer Climb Up The Ladder<-------")
                    speak("Computer Climb Up The Ladder")
            I += 1
        if (self.flag != 1) :
            self.PlayerAndComputerPosition()
            self.IsWon()
#Play_with_friends class
class Play_With_friends :
    WONPOINT = 100
    rand =  random.randint(1, 7)
    n = 100
    rollDice = ' '
    playerPosition = [0] * (n)
    diceScore = [0] * (n)
    Names = [None] * (n)
    Snake_Mouth_Position = [0] * (8)
    Snake_Tail_Position = [0] * (8)
    Ladder_Up_Position = [0] * (8)
    Ladder_Down_Position = [0] * (8)
    flag = 0
    Level = ' '
    Count = 0
    Snake_flag = 0
    Ladder_flag = 0
    # setGame()
    def setGame(self) :
        print("-------------------------->SET GAME<------------------------------- \n", end ="")
        speak("SET GAME")
        print("         Levels :   1 - EASY     2 - MEDIUM     3 - HARD \n \n", end ="")
        speak("Levels")
        speak("1 - EASY")
        speak("2 - MEDIUM")
        speak("3 - HARD")
        print("Choose a Level (1 | 2 | 3 ) : ", end ="")
        speak("Choose a Level")
        speak("1 or 2 or 3 ")
        self.Level = input()
        while (self.Level != '1' and self.Level != '2' and self.Level != '3') :
            print("Choose a valid Level (1 | 2 | 3 ) : ", end ="")
            speak("Choose a valid Level")
            self.Level = input()
    # setPlayer()
    def SetPlayer(self) :
        print(" \nEnter no. of Players : ", end ="")
        speak("Enter number of Players")
        Play_With_friends.n = int(input())
        while (self.n < 0) :
            print("Enter Valid no. of Players : ")
            speak("Enter Valid no. of Players")
            Play_With_friends.n = input()
        print(" \nEnter players Names : ")
        speak("Enter players Names")
        i = 0
        while (i < Play_With_friends.n) :
            print(f"player {i + 1}  : ", end ="")
            speak(f"Enter player {i + 1}  Name")
            Play_With_friends.Names[i] = input()
            i += 1
    def SnakesAndLaddersPosition(self) :
        if (self.Level == '1') :
            # Snake Mouth Position Setting
            Play_With_friends.Snake_Mouth_Position[0] = random.randint(95, (99 - 95) + 95)
            Play_With_friends.Snake_Mouth_Position[1] = random.randint(60, (65 - 60) + 60)
            Play_With_friends.Snake_Mouth_Position[2] = random.randint(30, (35 - 30) + 30)
            # Snake Tail Position Setting
            Play_With_friends.Snake_Tail_Position[0] = random.randint(24, (26 - 24) + 24)
            Play_With_friends.Snake_Tail_Position[1] = random.randint(51, (56 - 51) + 51)
            Play_With_friends.Snake_Tail_Position[2] = random.randint(15, (19 - 15) + 15)
        elif(self.Level == '2') :
            # Snake Mouth Position Setting
            Play_With_friends.Snake_Mouth_Position[0] = random.randint(98, (99 - 98) + 98)
            Play_With_friends.Snake_Mouth_Position[1] = random.randint(87, (87 - 81) + 81)
            Play_With_friends.Snake_Mouth_Position[2] = random.randint(55, (59 - 55) + 55)
            Play_With_friends.Snake_Mouth_Position[3] = random.randint(32, (38 - 32) + 32)
            Play_With_friends.Snake_Mouth_Position[4] = random.randint(15, (19 - 15) + 15)
            # Snake Tail Position Setting
            Play_With_friends.Snake_Tail_Position[0] = random.randint(51, (56 - 51) + 51)
            Play_With_friends.Snake_Tail_Position[1] = random.randint(72, (78 - 72) + 72)
            Play_With_friends.Snake_Tail_Position[2] = random.randint(41, (42 - 41) + 41)
            Play_With_friends.Snake_Tail_Position[3] = random.randint(26, (29 - 26) + 26)
            Play_With_friends.Snake_Tail_Position[4] = random.randint(6,  (9 - 6) + 6)
        else :
            # Snake Mouth Position Setting
            Play_With_friends.Snake_Mouth_Position[0] = random.randint(98, (99 - 98) + 98)
            Play_With_friends.Snake_Mouth_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_friends.Snake_Mouth_Position[2] = random.randint(71, (74 - 71) + 71)
            Play_With_friends.Snake_Mouth_Position[3] = random.randint(62, (65 - 62) + 62)
            Play_With_friends.Snake_Mouth_Position[4] = random.randint(41, (42 - 41) + 41)
            Play_With_friends.Snake_Mouth_Position[5] = random.randint(65, (69 - 65) + 65)
            Play_With_friends.Snake_Mouth_Position[6] = random.randint(24, (26 - 24) + 24)
            Play_With_friends.Snake_Mouth_Position[7] = random.randint(15, (19 - 15) + 15)
            # Snake Tail Position Setting
            Play_With_friends.Snake_Tail_Position[0] = random.randint(51, (56 - 51) + 51)
            Play_With_friends.Snake_Tail_Position[1] = random.randint(41, (45 - 41) + 41)
            Play_With_friends.Snake_Tail_Position[2] = random.randint(32, (36 - 32) + 32)
            Play_With_friends.Snake_Tail_Position[3] = random.randint(22, (26 - 22) + 22)
            Play_With_friends.Snake_Tail_Position[4] = random.randint(26, (29 - 26) + 26)
            Play_With_friends.Snake_Tail_Position[5] = random.randint(15, (19 - 15) + 15)
            Play_With_friends.Snake_Tail_Position[6] = random.randint(15, (19 - 15) + 15)
            Play_With_friends.Snake_Tail_Position[7] = random.randint(6, (9 - 6) + 6)
        if (self.Level == '1') :
            # Ladder Down Position Setting
            Play_With_friends.Ladder_Down_Position[0] = random.randint(6, (9 - 6) + 6)
            Play_With_friends.Ladder_Down_Position[1] = random.randint(65, (69 - 65) + 65)
            Play_With_friends.Ladder_Down_Position[2] = random.randint(87, (87 - 81) + 81)
            # Laddet Up Position Setting
            Play_With_friends.Ladder_Up_Position[0] = random.randint(81, (87 - 81) + 81)
            Play_With_friends.Ladder_Up_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_friends.Ladder_Up_Position[2] = random.randint(96, (99 - 96) + 96)
        elif(self.Level == '2') :
            # Ladder Down Position Setting
            Play_With_friends.Ladder_Down_Position[0] = random.randint(15, (19 - 15) + 15)
            Play_With_friends.Ladder_Down_Position[1] = random.randint(37, (38 - 37) + 37)
            Play_With_friends.Ladder_Down_Position[2] = random.randint(51, (59 - 51) + 51)
            Play_With_friends.Ladder_Down_Position[3] = random.randint(65, (69 - 65) + 65)
            Play_With_friends.Ladder_Down_Position[4] = random.randint(81, (86 - 81) + 81)
            # Ladder Up Position Setting
            Play_With_friends.Ladder_Up_Position[0] = random.randint(81, (86 - 81) + 81)
            Play_With_friends.Ladder_Up_Position[1] = random.randint(41, (42 - 41) + 41)
            Play_With_friends.Ladder_Up_Position[2] = random.randint(81, (86 - 81) + 81)
            Play_With_friends.Ladder_Up_Position[3] = random.randint(92, (96 - 92) + 92)
            Play_With_friends.Ladder_Up_Position[4] = random.randint(96, (99 - 96) + 96)
        else :
            # Ladder Down Position Setting
            Play_With_friends.Ladder_Down_Position[0] = random.randint(6, (9 - 6) + 6)
            Play_With_friends.Ladder_Down_Position[1] = random.randint(24, (26 - 24) + 24)
            Play_With_friends.Ladder_Down_Position[2] = random.randint(36, (38 - 36) + 36)
            Play_With_friends.Ladder_Down_Position[3] = random.randint(41, (45 - 41) + 41)
            Play_With_friends.Ladder_Down_Position[4] = random.randint(54, (59 - 54) + 54)
            Play_With_friends.Ladder_Down_Position[5] = random.randint(68, (69 - 68) + 68)
            Play_With_friends.Ladder_Down_Position[6] = random.randint(72, (78 - 72) + 72)
            Play_With_friends.Ladder_Down_Position[7] = random.randint(81, (86 - 81) + 81)
            # Ladder Up Position Setting
            Play_With_friends.Ladder_Up_Position[0] = random.randint(81, (87 - 81) + 81)
            Play_With_friends.Ladder_Up_Position[1] = random.randint(92, (96 - 92) + 92)
            Play_With_friends.Ladder_Up_Position[2] = random.randint(74, (78 - 74) + 74)
            Play_With_friends.Ladder_Up_Position[3] = random.randint(65, (69 - 65) + 65)
            Play_With_friends.Ladder_Up_Position[4] = random.randint(81, (87 - 81) + 81)
            Play_With_friends.Ladder_Up_Position[5] = random.randint(74, (78 - 74) + 74)
            Play_With_friends.Ladder_Up_Position[6] = random.randint(95, (96 - 95) + 95)
            Play_With_friends.Ladder_Up_Position[7] = random.randint(92, (99 - 92) + 92)
    def SnakesAndLaddersPositionPrint(self) :
        print(" \n-------->SNAKES POSITION           |      LADDERS POSITION <--------- \n", end ="")
        speak("SNAKES POSITION and LADDERS POSITION")
        if (self.Level == '1') :
            i = 0
            while (i < 3) :
                if (i == 0) :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    0{Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                i += 1
        elif(self.Level == '2') :
            i = 0
            while (i < 5) :
                if (i == 0) :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                elif(i == 4) :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   0{Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                i += 1
        else :
            i = 0
            while (i < 8) :
                if (i == 0) :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    0{Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                elif(i == 7) :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   0{Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                else :
                    print(f"               {Play_With_friends.Snake_Mouth_Position[i]}     to   {Play_With_friends.Snake_Tail_Position[i]}      |    {Play_With_friends.Ladder_Down_Position[i]}     to    {Play_With_friends.Ladder_Up_Position[i]}")
                i += 1
        print("------------------------------------------------------------------- \n", end ="")
    def RollDice(self) :
        print("\n------------------------>Roll The Dice<--------------------------\n", end ="")
        speak("Roll The Dice")
        i = 0
        while (i < Play_With_friends.n) :
            print(f" \n           {Play_With_friends.Names[i]}\'s Turn (Enter character "R" or "r" ) : ", end ="")
            speak(f"{Play_With_friends.Names[i]}\'s Turn")
            speak("Enter Capital or Small R")
            Play_With_friends.rollDice = input()
            while (Play_With_friends.rollDice != 'R' and Play_With_friends.rollDice != 'r') :
                print("\n           Enter Valid Character R or r : ")
                speak("Enter Valid Capital or Small R")
                Play_With_friends.rollDice = input()
            Play_With_friends.diceScore[i] = random.randint(1, (6 - 1) + 1)
            Play_With_friends.playerPosition[i] += Play_With_friends.diceScore[i]
            print(f"                     dice Score = {Play_With_friends.diceScore[i]}")
            speak(f"dice Score = {Play_With_friends.diceScore[i]}")
            I = 0
            while (I < Play_With_friends.n) :
                k = 0
                while (k < 8) :
                    if (self.Level == '1' and I < 3) :
                        if (Play_With_friends.playerPosition[I] == Play_With_friends.Snake_Mouth_Position[k] and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Snake_Mouth_Position[k] != 0)) :
                            print(" \n        --------->Oops, Swallowed By Snake<---------")
                            speak("Oops, Swallowed By Snake")
                        elif(Play_With_friends.playerPosition[I] == Play_With_friends.Ladder_Down_Position[k] and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Ladder_Down_Position[k] != 0)) :
                            print(" \n            ----->Hurry, Climb Up The Ladder<-----")
                            speak("Hurry, Climb Up The Ladder")
                    elif(self.Level == '2' and I < 5) :
                        if (Play_With_friends.playerPosition[I] == Play_With_friends.Snake_Mouth_Position[k]  and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Snake_Mouth_Position[k] != 0)) :
                            print(" \n        --------->Oops, Swallowed By Snake<---------")
                            speak("Oops, Swallowed By Snake")
                        elif(Play_With_friends.playerPosition[I] == Play_With_friends.Ladder_Down_Position[k] and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Ladder_Down_Position[k] != 0)) :
                            print(" \n            ----->Hurry, Climb Up The Ladder<-----")
                            speak("Hurry, Climb Up The Ladder")
                    else :
                        if (Play_With_friends.playerPosition[I] == Play_With_friends.Snake_Mouth_Position[k] and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Snake_Mouth_Position[k] != 0)) :
                            print(" \n        --------->Oops, Swallowed By Snake<---------")
                            speak("Oops, Swallowed By Snake")
                        elif(Play_With_friends.playerPosition[I] == Play_With_friends.Ladder_Down_Position[k] and (Play_With_friends.playerPosition[I] != 0 and Play_With_friends.Ladder_Down_Position[k] != 0)) :
                            print(" \n            ----->Hurry, Climb Up The Ladder<-----")
                            speak("Hurry, Climb Up The Ladder")
                    k += 1
                I += 1
            if (self.flag != 1) :
                self.PlayerPosition()
                self.IsWon()
            i += 1
    def PlayerPosition(self) :
        i = 0
        while (i < Play_With_friends.n) :
            if (Play_With_friends.playerPosition[i] > Play_With_friends.WONPOINT) :
                Play_With_friends.playerPosition[i] -= Play_With_friends.diceScore[i]
            i += 1
        # playerPosition With Snake_Tail_Position
        i = 0
        while (i < Play_With_friends.n) :
            if (self.Level == '1') :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[2]
            elif(self.Level == '2') :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[2]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[3]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[3]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[4]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[4]
                else :
                    pass
            else :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[2]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[3]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[3]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[4]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[4]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[5]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[5]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[6]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[6]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Snake_Mouth_Position[7]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Snake_Tail_Position[7]
            i += 1
        # playerPosition With Ladder
        i = 0
        while (i < Play_With_friends.n) :
            if (self.Level == '1') :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[2]
            elif(self.Level == '2') :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[2]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[3]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[3]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[4]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[4]
            else :
                if (Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[0]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[0]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[1]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[1]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[2]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[2]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[3]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[3]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[4]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[4]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[5]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[5]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[6]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[6]
                elif(Play_With_friends.playerPosition[i] == Play_With_friends.Ladder_Down_Position[7]) :
                    Play_With_friends.playerPosition[i] = Play_With_friends.Ladder_Up_Position[7]
            i += 1
        # player position display
        print("\n------------------:::::Player\'s Position:::::------------------ \n")
        speak("Player\'s Position")
        i = 0
        while (i < Play_With_friends.n) :
            self.Count = 1
            if (Play_With_friends.diceScore[i] > 0) :
                print(f"CURRENT :                    {Play_With_friends.Names[i]}  = {Play_With_friends.playerPosition[i]}")
                speak(f"CURRENT :                    {Play_With_friends.Names[i]}  = {Play_With_friends.playerPosition[i]}")
            else :
                print(f"CURRENT :                    {Play_With_friends.Names[i]}  = {Play_With_friends.playerPosition[i]}")
                speak(f"CURRENT :                    {Play_With_friends.Names[i]}  = {Play_With_friends.playerPosition[i]}")
            if (i == Play_With_friends.n - 1) :
                print("------------------------------------------------------------------- ", end ="")
            self.Count += 1
            Play_With_friends.diceScore[i] = 0
            i += 1
    def IsWon(self) :
        i = 0
        while (i < Play_With_friends.n) :
            if (Play_With_friends.playerPosition[i] == Play_With_friends.WONPOINT) :
                print("\n-------------------------WINNER----------------------------------- \n")
                print(f"                          CONGRATS {Play_With_friends.Names[i]}")
                speak(f"CONGRATS {Play_With_friends.Names[i]} you won.")
                print("\n-------------------------WINNER----------------------------------- \n")
                self.flag = 1
                break
            if (self.flag == 1) :
                break
            i += 1
class SnakeNLadderGame :
    def main() :
        print("                 Welcome To SNACK AND LADDER GAME \n-------------------------------------------------------------------\n")
        speak("Welcome To SNACK AND LADDER GAME")
        print("Application Type : Console Game")
        speak("Application Type : Console Game")
        print("Version : 1.0.1 LTS")
        speak("Version : 1.0.1 LTS")
        print("Developer : GHANSHYAM VAJA")
        speak("Developer : GHANSHYAM vaja")
        print("-------------------------------------------------------------------")
        playWith = ' '
        print("\n       1 - play With Computer         2 - play With friends")
        print(" \nEnter Your choice (1 | 2) : ", end ="")
        speak("Enter Your choice")
        speak("1 for play With Computer")
        speak("2 for play With friends")
        playWith = input()
        while (playWith != '1' and playWith != '2') :
            print(" \nEnter valid choice (1 | 2) : ", end ="")
            speak("Enter valid choice")
            speak("1 or 2")
            playWith = input()
        print(" \n::::::::::::::::::::---->WINPOINT : 100<----:::::::::::::::::::: \n")
        speak("WINPOINT 100")
        if (playWith == '1') :
            obj = Play_With_Computer()
            i = 1
            while (obj.flag != 1) :
                if (i == 1) :
                    obj.setGame()
                    obj.SnakesAndLaddersPosition()
                obj.SnakesAndLaddersPositionPrint()
                if (i == 1) :
                    print("\n-------------------::Lets Start The Game::------------------------- ", end ="")
                    speak("Lets Start The Game")
                obj.RollDice()
                # obj.PlayerPosition();
                # obj.IsWon();
                i = 2
        else :
            obj2 = Play_With_friends()
            k = 1
            while (obj2.flag != 1) :
                if (k == 1) :
                    obj2.setGame()
                    obj2.SetPlayer()
                    obj2.SnakesAndLaddersPosition()
                obj2.SnakesAndLaddersPositionPrint()
                if (k == 1) :
                    print("\n-------------------::Lets Start The Game::------------------------- ", end ="")
                    speak("Lets Start The Game")
                obj2.RollDice()
                k = 2
##################################################################################################################
root = Tk()
Status = tkinter.StringVar(value="Listening.....")

#set text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

####################################################Speak() Method#####################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

###############################################################Wish to User######################################################################
def WishMe(Name, version):
    hour = int(datetime.datetime.now().hour)
    speak("Welcome" + User)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<17:
        speak("Good Afternoon sir!")
    
    else:
        speak("Good Evening Sir!")
    
    Assistent = (f"G{version}")
    speak(f"I am Your Assistent {Assistent}")

    speak("How can i Help You,sir")

################################################################Return User Commands#############################################################
def takeCommand():
    global Status
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        Status = tkinter.StringVar(value="Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        Status = tkinter.StringVar(value="Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print((f"you said: {query} \n"))
    except Exception as e:
        print(e)
        print("Unable to Recognize your Voice.")
        return "none"
    
    return query

#####################################################################Commands####################################################################
def run_assistent():
    while True:
        os.system('cls')
        speak("Press 1 and Enter in command prompt to give command")
        Activate = input("Press 1 and Enter key : ")
        while Activate != '1':
            speak("Press 1 and Enter in command prompt to give command")
            Activate = input("Press 1 and Enter key : ")
        query = takeCommand().lower()
        host = socket.gethostname()
        IP = socket.gethostbyname(host)
        DateTime = datetime.datetime.now()
        TName = Email.replace('@', '_')
        TName = TName.replace('.', '_')
        sql = f"Insert into {TName}(Query, Host, IPAddress, DateAndTime)VALUES(%s, %s, %s, %s)"
        val = (query, host, IP, DateTime)
        mycursor.execute(sql, val)
        myconn.commit()

        if "none" in query:
            pass

        elif 'how are you' in query:
            speak("I am fine sir.. And you?")
            query = takeCommand().lower()
            if query == "i am fine" or query == "fine":
                speak("nice to hear this")
                speak("how can i help you sir?")
        
        elif 'what is your name' in query:
            speak("My name is G 1 point o")

        elif 'change my name' in query:
            global User
            speak("Enter your new name in command prompt")
            OldName = User
            speak("Enter your new name in command prompt")
            NewName = input("Enter your new Name : ")
            while NewName ==  '':
                NewName = input("Enter your new Name : ")
            mycursor.execute(f"UPDATE Users SET Name='{NewName}' WHERE Email='{Email}'")
            speak(f"Hi, {OldName} your name is changed Successfully.")
            speak(f"your new name is {NewName}")
            myconn.commit()
            User = NewName
            break

        elif 'change my password' in query or 'change account password' in query:
            speak("Enter your new password in command prompt")
            NewPassword = input("Enter New Password : ")
            res = re.search(PasswordValidate, NewPassword)
            while res == None:
                print("\n Warning : \nMinimum password length is needs required more than 8 character")
                print("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
                speak("Warning")
                speak("Minimum password length is nneds too be required more than 8 character")
                speak("password can be combination of uppercase latters, lowercase latters, numbers and special characters")
                speak("Enter password in valid  format ")
                NewPassword = input("Enter password in valid format : ")
                res = re.search(PasswordValidate, NewPassword)
            mycursor.execute(f"UPDATE Users SET Password='{NewPassword}' WHERE Email='{Email}'")
            speak(f"Hi, {User} your Password is changed Successfully.")
            myconn.commit()
            break

        elif 'delete my account' in query:
            speak("Enter your Password in command prompt")
            password = input("Enter your Password : ")
            sql = f"SELECT *FROM Users WHERE Email = '{Email}' and Password = '{password}' "
            mycursor.execute(sql)
            checkRecord = mycursor.fetchone()
            while checkRecord is None:
                speak("Enter your Password in command prompt")
                password = input("Enter your Password : ")
                sql = f"SELECT *FROM Users WHERE Email = '{Email}' and Password = '{password}' "
                mycursor.execute(sql)
                checkRecord = mycursor.fetchone()
            sql2 = f"DELETE FROM Users WHERE Email = '{Email}'"
            sql3 = f"DROP TABLE {TName}"
            mycursor.execute(sql2)
            if mycursor.rowcount:
                speak(f"Hi, {User} your account is deleted successfully.....")
            myconn.commit()
            mycursor.execute(sql3)
            os.system('cls')
            speak("Press 1 for Login")
            speak("Press 2 For Signup")
            speak("Press 3 For Delete Account")
            print("\nPress 1 for Login")
            print("Press 2 For Signup")
            print("Press 3 For Delete Account")
            speak("Enter your choice in command prompt")
            choice = input("Enter your Choice (1 or 2 or 3) : ")
            while choice != '1' and choice != '2' and choice != '3':
               speak("Enter valid choice")
               choice = input("Enter valid choice : ")
            if choice ==  '1':
               Login()
            elif choice == '2':
               Signup()
            else:
               DeleteAccount()
            break

        elif 'what is my name' in query or 'who i am' in query or 'who am i' in query or 'what\'s my name' in query or 'my name' in query:
            speak(f"Sir you name is {User}")
            break

        elif 'who made you' in query or 'who created you' in query:
            speak(f'I have been created by ghanshyam vaja')
            break

        elif 'who owns you' in query:
            speak(f'Ghanshyam vaja owns me')
            break

        elif 'ghanshyam bca sem5 project' in query or 'ghanshyam bca sem 5 project' in query or 'ghanshyam bca 5 project' in query or 'developer bca sem5 project' in query or 'developer bca sem 5 project' in query or 'developer bca 5 project' in query:
            speak("wait for new moments i am openinng Ghanshyam vaja\'s bca sem 5 project for you")
            webbrowser.open("savjani-college.000webhostapp.com")
            break

        elif 'change voice' in query or 'change your voice' in query:
            speak("ok sir, i am changing my voice")
            engine.setProperty('voice', voices[1].id)
            speak("hi sir, this is me your assistent How can i help you sir?")

        elif 'ip address' in query or 'ipaddress' in query or 'what\'s my ip' in query or 'what is my ip address' in query:
            host = socket.gethostname()
            speak(f"your computer name is {host}")
            print(f"your computer ip address is : {socket.gethostbyname(host)}")
            speak(f"and your computer ip address is {socket.gethostbyname(host)}")
            break

        elif "open cmd" in query or "command prompt" in query:
            os.system("start cmd")
            speak("I am starting Command Prompt in next few moments..")
            break

        elif 'number guessing game' in query or 'play number guessing game' in query:
            speak("Sir, now focus on command prompt to play game")
            GuessNumber()
            break

        elif 'snake and ladder game' in query or 'play snake and ladder game' in query:
            speak("Sir, now focus on command prompt to play game")
            SnakeNLadderGame.main()
            break

        elif 'factorial' in query or 'find factorial' in query:
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"factorial of {int(value[0])} is {math.factorial(int(value[0]))}")
            speak(f"factorial of {int(value[0])} is {math.factorial(int(value[0]))}")
            break

        elif 'find square root' in query or 'find squareroot' in query or 'squareroot' in query or 'square root' in query:
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"square root of {float(value[0])} is {math.sqrt(float(value[0]))}")
            speak(f"square root of {float(value[0])} is {math.sqrt(float(value[0]))}")
            break

        elif 'to the power of' in query or 'power of' in query:
            values = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"{float(values[0])} to the power of {float(values[1])} is {math.pow(float(values[0]), float(values[1]))}")
            speak(f"{float(values[0])} to the power of {float(values[1])} is {math.pow(float(values[0]), float(values[1]))}")
            break

        elif 'value of pi' in query:
            print(f"the value of pi is {math.pi}")
            speak(f"the value of pi is {math.pi}")
            break

        elif 'gcd of' in query or 'gcd' in query:
            values = [int(i) for i in query.split() if i.isdigit()]
            print(f"the gcd of {values[0]} and {values[1]} is {math.gcd(values[1], values[0])}")
            speak(f"the gcd of {values[0]} and {values[1]} is {math.gcd(values[1], values[0])}")
            break

        elif 'log of' in query  or 'find log' in query:
            values = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of log {float(values[0])} with base {float(values[1])} is {math.log(float(values[0]), float(values[1]))}")
            speak(f"the value of log {float(values[0])} with base {float(values[1])} is {math.log(float(values[0]), float(values[1]))}")
            break

        elif 'log2 of' in query or 'log 2 of' in query or 'find log2' in query or 'find log 2' in query:
            query = query.replace('log2', '')
            query = query.replace('log 2', '')
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of log2 of {float(value[0])} is {math.log2(float(value[0]))}")
            speak(f"the value of log2 of {float(value[0])} is {math.log2(float(value[0]))}")
            break

        elif 'log 10 of' in query or 'log10 of' in query or 'find log 10' in query or 'find log10' in query:
            query = query.replace('log 10', '')
            query = query.replace('log10', '')
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of log10 of {float(value[0])} is {math.log10(float(value[0]))}")
            speak(f"the value of log10 of {float(value[0])} is {math.log10(float(value[0]))}")
            break 

        elif 'sin' in query or 'sin of' in query or 'find sin' in query or 'find sin of' in query or 'sine' in query:
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of sine of {float(value[0])} is : {math.sin(float(value[0]))}")
            speak(f"the value of sine of {float(value[0])} is {math.sin(float(value[0]))}")
            break

        elif 'cos' in query or 'cos of' in query or 'find cos' in query or 'find cos of' in query or 'cosine' in query:
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of cosine of {float(value[0])} is : {math.cos(float(value[0]))}")
            speak(f"the value of cosine of {float(value[0])} is {math.cos(float(value[0]))}")
            break

        elif 'tan' in query or 'tan of' in query or 'find tan' in query or 'find tan of' in query or 'tangent' in query:
            value = re.findall(r"[-+]?\d*\.\d+|\d+", query)
            print(f"the value of tangent of {float(value[0])} is : {math.tan(float(value[0]))}")
            speak(f"the value of tangent of {float(value[0])} is {math.tan(float(value[0]))}")
            break

        elif 'who is' in query:
            pwk.search(query)
            speak(f'Wait for few moments...')
            break
        
        elif 'what is' in query:
            pwk.search(query)
            speak(f'Wait for few moments...')
            break

        elif 'where is' in query:
            try:
                query = query.replace('where is', '')
                speak(f'Wait i am finding right location for you...')
                webbrowser.open("https://google.com/maps/place/" + query + '')
            except:
                speak("Place not found")
            break

        elif 'which is' in query or 'which' in query:
            pwk.search(query)
            speak(f'Wait for few moments...')
            break

        elif 'what is' in query:
            pwk.search(query)
            speak(f'Wait for few moments...')
            break

        elif 'the date' in query or 'date' in query or 'what is the date' in query or 'what is the date today' in query:
           pwk.search(query)
           speak(f'Wait for few moments...')
           break

        elif 'the time' in query or 'time' in query or 'what is the time' in query or 'what is the time right now' in query or 'current time' in query:
           pwk.search(query)
           speak(f'Wait for few moments...')
           break

        elif 'download youtube video' in query or 'youtube video download' in query:
            speak("Paste video link in command prompt")
            url = input("Paste Link Here : ")
            yt = YouTube(url)

            print(f"title : {yt.title}")
            speak(f"title : {yt.title}")
            print(f"views : {yt.views}")
            speak(f"views : {yt.views}")

            ys = yt.streams.get_highest_resolution()

            print("Downloading Started.....")
            speak("Downloading Started")
            ys.download("")
            print("Download Completed.")
            speak("Download Commpleted sir")
            print("Path : C:/Users/Default/Downloads")
            break
        
        elif 'video' in query or 'play video' in query or 'play song on youtube' in query:
            speak("Wait for few moments i am finding video for you....")
            query = query.replace("video", '')
            pwk.playonyt(query)
            break

        elif 'open google' in query or 'google' in query:
            speak("Wait for few moments i am opening google for you... \n")
            webbrowser.open("google.com") 
            break

        elif 'open youtube' in query or 'youtube' in query:
            speak("Wait for few moments i am opening Youtube for you... \n")
            webbrowser.open("youtube.com")
            break

        elif 'open stack overflow' in query or 'stack overflow' in query:
            speak("Wait for few moments i am opening Stack Overflow for you... \n")
            webbrowser.open("stackoverflow.com") 
            break

        elif 'apple' in query or 'open apple.com' in query or 'open apple' in query:
            speak("Wait for few moments i am opening apple.com for you... \n")
            webbrowser.open("apple.com") 
            break

        elif 'open whatsapp' in query or 'whatsapp' in query:
            speak("Wait for few moments i am opening whatsapp for you...\n")
            webbrowser.open("web.whatsapp.com")
            break

        elif 'open instagram' in query or 'instagram' in query:
            speak("Wait for few moments i am opening instagram for you... \n")
            webbrowser.open("instagram.com")   
            break 

        elif 'open twitter' in query or 'twitter' in query:
            speak("Wait for few moments i am opening Twitter for you... \n")
            webbrowser.open("twitter.com")
            break

        elif 'open spotify' in query or 'spotify' in query or 'play music' in query or 'play song' in query or 'music' in query or 'song' in query:
            speak("Wait for few moments i am opening spotify for you... \n")
            webbrowser.open("spotify.com")
            break

        elif 'search' in query or 'find' in query:
            speak("wait for few moments i am finding best results for you...")
            query = query.replace('search', '')
            pwk.search(query)
            break

        elif 'wikipedia' in query or 'according to wikipedia' in query or 'search in wikipedia' in query or 'tell me about' in query:
            speak("Wait for few moments I am Searching Wikipedia... \n")
            query = query.replace(("wikipedia"), "")
            query = query.replace('according to wikipedia', '')
            try:
                result = wikipedia.summary(query, sentences = 29)
                speak("According to Wikipedia.... \n")
                print(result)
                speak(result)
            except:
                print(f"Information not found About {query}")
                speak(f"Information not found About {query}")
            break


        elif 'take photo' in query or 'take image' in query or 'camera' in query or 'take selfie' in query or 'open camera' in query:
            Name = f"IMG{random.randint(5, 9)} .jpg"
            ecapture.open(0, "G", Name)
            break

        elif 'play joke' in query or  'tell me a joke' in query or 'speak a joke' in query or 'make me happy' in query or 'joke' in query:
            speak(pyjokes.get_joke())
            speak("want to Listen one more??")
            speak("say yes or no")
            confirm = takeCommand().lower()
            if confirm == 'yes':
                speak(pyjokes.get_joke())
            break

        elif 'lock' in query or 'lock my computer' in query or 'lock my system' in query:
            speak("wait for few  moments, i am doing lock your computer")
            ctypes.windll.user32.LockWorkStation()
            break

        elif 'shutdown' in query or 'shutdown system' in query or 'shutdown my computer' in query:
           speak("wait for few moment, i am doing process to do your system shutting down")
           os.system("shutdown /s /t 1")

        elif 'restart' in query or 'restart system' in query or 'restart  my computer'  in query:
            speak("Wait for few moments, i am doing restart your computer")
            subprocess.call(["shutdown", "/r"])

        elif 'terminate yourself'  in query or 'deactivte yourself' in query or 'stop your self' in query or 'terminate your self'  in query or 'deactivte your self' in query or 'stop yourself' in query:
            speak("Ok sir, i am terninating myself in few moment")
            speak("3")
            speak("2")
            speak("1")
            myconn.close()
            sys.exit()
        
        else:
            speak(f'Wait for few moments...')
            pwk.search(query)
        time.sleep(2.9)

#Main Function
if __name__ == '__main__':

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$UI using tkinter & Driver Code$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    root.title("G Assistent")
    root.iconbitmap("C:/Project2/Logo_Icon.ico")
    def a():
        clear = lambda: os.system('cls')
        version = "1 point o"
        speak(f"Hi, I am G Assistent {version}")
        speak("Press 1 for Login")
        speak("Press 2 For Signup")
        speak("Press 3 For Delete Account")
        print("Press 1 for Login")
        print("Press 2 For Signup")
        print("Press 3 For Delete Account")
        speak("Enter your choice in command prompt")
        choice = input("Enter your Choice (1 or 2 or 3) : ")

        while choice != '1' and choice != '2' and choice != '3':
           speak("Enter valid choice")
           choice = input("Enter valid choice : ")

        if choice ==  '1':
           Login()
        elif choice == '2':
           Signup()
        else:
           DeleteAccount()
           speak(f"Hi, I am G Assistent {version}")
           speak("Press 1 for Login")
           speak("Press 2 For Signup")
           speak("Press 3 For Delete Account")
           print("\nPress 1 for Login")
           print("Press 2 For Signup")
           print("Press 3 For Delete Account")
           speak("Enter your choice in command prompt")
           choice = input("Enter your Choice (1 or 2 or 3) : ")
           while choice != '1' and choice != '2' and choice != '3':
              speak("Enter valid choice")
              choice = input("Enter valid choice : ")
           if choice ==  '1':
              Login()
           elif choice == '2':
              Signup()
           else:
              DeleteAccount()

        while True:
            run_assistent()

    image  = Image.open("C:/Project2/Logo.jpg")
    photo = ImageTk.PhotoImage(image)
    LogoLabel = Label(image = photo)
    LogoLabel.pack()
    Start = tkinter.Button(root, text="Activate", font="sanserif 19", command=a)
    #StatusInfo = Label(root, font="sen-serif 29", height="2", width="15", textvariable=Status)
    #StatusInfo.pack(pady=29)
    Start.pack()
    root.mainloop()