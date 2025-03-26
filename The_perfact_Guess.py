'''
We are going to write a program that generates a random number and asks the user to guess it.
it the player's guess is higher then the actual number, the program prints "lower number please". 
Similary, it the uer's guess is too low , the program prints "higer number please" When the user guesses the correct number,
 the prgram displays the number guesses the player usef to arrive at the number.


'''

import random
n = random.randint(1,100)
a = -1
guesses = 0

while(a != n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1


print(f"You have guessed the number {n} correctly in {guesses} attempt")