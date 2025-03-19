'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}

if youstr not in youDict:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you ==1):
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("you lose!")

    elif(computer ==1 and you == -1):
        print("you lose!")

    elif(computer ==1 and you == 0):
        print("you win!")

    elif(computer ==0 and you == -1):
        print("you win!")

    elif(computer ==0 and you == 1):
        print("you lose!")
