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