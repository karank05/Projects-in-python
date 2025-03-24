import time
import random
from colorama import Fore, Style

# User database
users = {}

def register():
    print(Fore.CYAN + "\n📝 Welcome to User Registration\n" + Style.RESET_ALL)
    name = input("Enter your name: ").strip().upper()
    
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print(Fore.RED + "\n❌ Invalid input! Please enter a valid age." + Style.RESET_ALL)
    
    if age < 18:
        print(Fore.RED + "\n🚫 YOU CAN'T ENTER MY WORLD. TRY AFTER 18 🚫" + Style.RESET_ALL)
        return None
    else:
        print(Fore.GREEN + f"\n✅ WELCOME TO MY WORLD, {name}! ✅" + Style.RESET_ALL)
        users[name] = {"age": age, "score": 0}
    return name

def games(name):
    print(Fore.YELLOW + "\n🎮 Welcome to the Game Hub!" + Style.RESET_ALL)
    while True:
        print("\nChoose a game:")
        print("1️⃣  GateKeeper")
        print("2️⃣  The Entry Test")
        print("3️⃣  World Access")
        print("4️⃣  Age of Entry")
        print("5️⃣  Restricted Zone")
        print("🔴  Type 'EXIT' to quit.")
        
        choice = input("\nEnter your choice (1-5 or EXIT): ").strip().upper()
        
        if choice == 'EXIT':
            print(Fore.MAGENTA + "\n👋 Exiting the game. See you next time!" + Style.RESET_ALL)
            break
        elif choice == '1':
            gatekeeper(name)
        elif choice == '2':
            entry_test(name)
        elif choice == '3':
            world_access(name)
        elif choice == '4':
            age_of_entry(name)
        elif choice == '5':
            restricted_zone(name)
        else:
            print(Fore.RED + "\n❌ Invalid choice. Please choose a valid game number." + Style.RESET_ALL)

def gatekeeper(name):
    print(Fore.BLUE + "\n🛡️ Welcome to Gatekeeper: The Entry Test 🛡️\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.YELLOW + "\n🔍 Processing your entry request..." + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.GREEN + f"\n✅ ACCESS GRANTED ✅\nWelcome to my world, {name}! Enjoy your journey." + Style.RESET_ALL)

def entry_test(name):
    print(Fore.BLUE + "\n📜 Welcome to The Entry Test 📜" + Style.RESET_ALL)
    questions = {
        "What is 5 + 3?": "8",
        "Which planet is known as the Red Planet?": "MARS",
        "What is the capital of France?": "PARIS",
        "What is 10 - 4?": "6"
    }
    score = 0
    
    for question, answer in questions.items():
        user_answer = input(f"\n{question} ").strip().upper()
        if user_answer == answer:
            print(Fore.GREEN + "✅ Correct!" + Style.RESET_ALL)
            score += 10
        else:
            print(Fore.RED + "\n🚫 WRONG ANSWER! ACCESS DENIED 🚫" + Style.RESET_ALL)
            return
    
    users[name]["score"] += score
    print(Fore.GREEN + "\n✅ ALL ANSWERS CORRECT! YOU MAY ENTER ✅" + Style.RESET_ALL)

def world_access(name):
    print(Fore.BLUE + "\n🔐 Welcome to World Access 🔐" + Style.RESET_ALL)
    secret_number = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        try:
            guess = int(input(f"\nGuess the secret number (1-10). You have {attempts} attempts: "))
        except ValueError:
            print(Fore.RED + "❌ Invalid input! Enter a number." + Style.RESET_ALL)
            continue

        if guess == secret_number:
            print(Fore.GREEN + "\n✅ ACCESS GRANTED! YOU GUESSED IT RIGHT ✅" + Style.RESET_ALL)
            users[name]["score"] += 20
            return
        else:
            print(Fore.RED + "\n❌ WRONG GUESS. TRY AGAIN ❌" + Style.RESET_ALL)
            attempts -= 1
    
    print(Fore.RED + "\n🚫 ACCESS DENIED! OUT OF ATTEMPTS 🚫" + Style.RESET_ALL)

def age_of_entry(name):
    print(Fore.BLUE + "\n🧮 Welcome to Age of Entry 🧮" + Style.RESET_ALL)
    number = random.randint(1, 20)
    
    print(f"\nWhat is {number} multiplied by 2?")
    try:
        user_answer = int(input("\nYour answer: "))
    except ValueError:
        print(Fore.RED + "\n❌ Invalid input! Please enter a number." + Style.RESET_ALL)
        return
    
    if user_answer == number * 2:
        print(Fore.GREEN + "\n✅ CORRECT! ACCESS GRANTED ✅" + Style.RESET_ALL)
        users[name]["score"] += 15
    else:
        print(Fore.RED + "\n🚫 WRONG ANSWER! ACCESS DENIED 🚫" + Style.RESET_ALL)

def restricted_zone(name):
    print(Fore.RED + "\n🚨 Welcome to the Restricted Zone 🚨" + Style.RESET_ALL)
    choice1 = input("\nYou see two doors: One is 🔴 Red and one is 🔵 Blue. Which do you enter? (RED/BLUE): ").strip().upper()
    
    if choice1 == "RED":
        print(Fore.RED + "\n🔥 You entered a fire room! GAME OVER. 🔥" + Style.RESET_ALL)
        return
    elif choice1 == "BLUE":
        print(Fore.BLUE + "\n🌊 You find a secret passage. You move forward. 🌊" + Style.RESET_ALL)
    
    choice2 = input("\nYou find a chest. Do you OPEN it or LEAVE it? (OPEN/LEAVE): ").strip().upper()
    if choice2 == "OPEN":
        print(Fore.GREEN + "\n💎 You found the key to escape! YOU WIN! 💎" + Style.RESET_ALL)
        users[name]["score"] += 30
    else:
        print(Fore.RED + "\n🚪 You missed the key and got trapped! GAME OVER. 🚪" + Style.RESET_ALL)

player_name = register()
if player_name:
    games(player_name)
