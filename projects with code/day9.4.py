#hangman in python it's a game

import __main__
import random

words = ("BMW", "Bugatti", "Farari", "TOYOTA", "BYD", "TATA")

#dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("\n___________________________")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("___________________________")

def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words).lower()
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint) 
        guess = input("\n Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter not alphabet either.")
            continue

        if guess in guessed_letters:
            print("f You already guessed {guess} .")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You WIN.")
            is_running = False
        
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Sorry! You LOSE.")
            is_running = False

if __name__ == "__main__":
    main()


#note: general practice, create a folder and add this code while create another file for words only and paste that set words in that file3
# then, write this code, from file_name import words
"""
givin' you a condition: if there's function or a program and you want it to execute first, but you don't want it 
on top of your codebase. in that case, you use __name__ == "__main__":
def y():
    print("Second")

def x():
    print("First")

if __name__ == "__main__":
    x()
    y()
"""