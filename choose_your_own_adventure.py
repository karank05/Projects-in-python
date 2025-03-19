name = input("type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk around and swim to swim across: ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. ")

    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game. ")

    else:
        print('Not a valid option, you lose')


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(cross/back)? ").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose. ")

        else:
            print('Not a valid option, you lose')

    elif answer == "back":
        print("You go back and lose.")

    else:
        print('Not a valid option, you lose')


else:
    print('Not a valid option, you lose')


print("Thank you for trying", name)