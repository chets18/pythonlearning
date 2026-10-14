#python slot machine
import random

def spin_row():
    symbols = ["🍒","🍇","🍊","🍉"]

    return[random.choice(symbols) for _ in range(3)]
    

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet / 0.2
        elif row[0] == "🍇":
            return bet * 10
        elif row[0] == "🍊":
            return bet * 4

    return 0


def main():
    balance = 100

    print("*************************")
    print("welcome to python slots")
    print("symbols: 🍒 🍇 🍊 🍉")
    print("*************************")

    while balance > 0:
        print(f"Your balance is: ${balance}")
        bet = input("Please enter your bet: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("You cannot bet more than your balance")
            continue
        if bet <= 0:
            print("Bet amount must be greater than 0")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning..\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("sorry you lost this round")
        balance += payout

        play_again = input("Do you want to spin again? (y/n): ")
        if play_again.upper() != 'Y':
            break

    
    print(f"Game over! Your final balance is ${balance}")

if __name__ == "__main__":
    main()