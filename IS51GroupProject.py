"""
Stuctured English

We wish to make a small python script to simulate the access panal for information.
To begin the user will be displayed a login screen. 
If the user fails to login a security notificaiton appears.
If the user logins in successfully then the information is then displayed.
The information is about US naval battleships.
Only three ships will be displayed from a list of ten.
The list will be from a seprate txt document that is used as a dictionary.
The dictionary will allow us to display the information to the user.
"""

"""
Pseudocode

import random, os, time, json (each in their own line)

main()
    time.sleep (delay time - act like a loading computer)
    print(insert welcom text)
    while 
        enter user name
        time sleep 
        enter password

        if 
            time sleep
            print (login good)
            log in 
            dictionary created 
            break loop
        else
            print (security notified)
            exit()

login()
    time sleep
    print welcome statement for login 

create dictionary()
    open file
    ships as list name
    close file
    display 3 random ships
    print the 3 ships in each their own line
"""

import random
import os
import time 
import json

def main():
    time.sleep(2)
    print("\n", "Welcome to the National Naval Archives. Please enter credentials below: ")
    while True:
        UserName = input ("Enter User Name: ")
        time.sleep(1)
        PassWord = input ("Enter Password: ")
        if UserName == "spectre" and PassWord == "iridium":
            time.sleep(2)
            print ("Login Successful!")
            logged()
            dictionary = create_dictionary("classified.txt")
            break
        else: 
            print ("Credentials not found. Access terminated....security notified")
            exit()
    
def logged():
    time.sleep(3)
    print ("\n", "Welcome to the National Naval Archives", "\n", "Recent reports are displayed below: ", "\n")

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    ships = [ship.rstrip() for ship in infile]
    infile.close()
    display = random.sample(ships, 3)
    print(json.dumps(display, indent=5))

main()