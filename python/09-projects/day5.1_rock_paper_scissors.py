import random

options = ("rock","paper","scissors")
running = True

playing = True
while playing: 
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        player = player.lower()
  

    print(f"PlAYER: {player}")
    print(f"COMPUTER: {computer}")

    if player == computer:
        print("TIE!")
    elif player == "rock" and computer == "scissors":
        print("WIN!")
    elif player == "paper" and computer == "rock":
        print("WIN!")
    elif player == "scissors" and computer == "paper":
        print("WIN!")
    else:
        print("BETTER LUCK NEXT TIME!")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("Thanks for playing!")
