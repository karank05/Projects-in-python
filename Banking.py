# Python Banking Program

def show_balance(balance):
    print(f"Your balance is rs {balance:.2f}")

def deposit():
    amount = float(input("Enter your deposit amount: "))

    if amount < 0:
        print("You cannot deposit negative amounts")
        return 0

    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter your withdraw amount: "))

    if amount > balance:
        print("You cannot withdraw more than your balance")

    elif amount < 0:
        print("You must be more then 0")
        return 0

    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("****************")
        print("Banking Program ")
        print("****************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("****************")
        
        
        choice = input("Enter your choice(1-4): ")
        print("****************")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance +=deposit()
        elif choice == "3":
           balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a Invalid choice")

    print("Thank You! Have a nice day!")

if __name__ == "__main__":
    main()