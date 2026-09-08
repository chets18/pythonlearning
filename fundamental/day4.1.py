#python quiz game

questions = ("How many elements are in the periodic table?: ",
            "which animal lays the largest eggs?: ",
            "How many bones in human body ?: ",
            "which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 118", "C. 120", "D. 114"),
           ("A. Shark", "B. Ostrich", "C. Whale", "D. Elephant"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Venus", "B. Earth", "C. Mars", "D. Jupiter"))

answers=["B", "B", "A", "A"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("well, done!")

    else:
        print("you're cooked.")
        print(f"{answers[question_num]} is the correct answer")
        
    question_num +=1

print(f"You got {score} correct")
print(f"Your answers: {guesses}")
print(f"Correct answers: {answers}")
total = int(score / len(questions))
print(f"{total*100}%")