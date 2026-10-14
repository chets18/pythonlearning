# python banking program

def show_balance():
    print(f"Your balance is ${balance}\n")

def deposit():
    amt = float(input("Enter deposit amount: "))
    if amt < 0:
        print("Invalid amount")
        return 0
    else:
        return amt


def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Banking program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
        
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
        print("Thank you for banking with us!")
    else:
        print("Invalid choice. Please try again.")
         