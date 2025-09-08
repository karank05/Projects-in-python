pwd = input("What is the master password? ")

import os

def view():
    if not os.path.exists('passwords.txt'):
        print("No passwords saved yet.")
        return
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data:
                user, passw = data.split("|")
                print("User:", user, "Password:", passw)
            else:
                print("Invalid entry in passwords file.")

def add():
    name = input('Account Name: ')
    password = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + " | " + password + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
