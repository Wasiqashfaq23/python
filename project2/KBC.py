# planned on making kon bane ga crore pati mini game
# ===================================================
# 🎮 Kon Banega Crorepati – Pakistan Edition (KBC PK)
# ===================================================
# This is a 10-question quiz game inspired by KBC.
# The goal is to answer all 10 questions correctly.
# Each correct answer increases your prize money.
# Final prize for Question 10 is ₨100,000 (1 Lakh).
# You can use 4 lifelines during the game (only once):
#   → 50:50: Removes 2 incorrect options.
#   → Audience Poll: Shows fake voting percentages.
#   → Phone a Friend: Gives a helpful hint.
#   → Ask the Expert: Suggests the best answer.
# Safe levels protect your earnings after:
#   → Question 3 (₨33,000)
#   → Question 6 (₨33,000)
# If you answer wrong before a safe level, you win nothing.
# If you quit, you take home the current prize.
# Answer options: A, B, C, or D (case-insensitive).
# You can type 'lifeline' to use a lifeline.
# You can type 'quit' anytime to leave the game.
# Questions become harder as the prize increases.
# Good luck! Try to become Pakistan's next Crorepati! 🇵🇰

import random

questions = [
    "What is the capital of Pakistan?",
    "Who was the founder of Pakistan?",
    "Which currency is used in Pakistan?",
    "What is the national language of Pakistan?",
    "Which city is known as the City of Lights?",
    "What does CPU stand for in computers?",
    "Which planet is known as the Red Planet?",
    "Which organ purifies blood in the human body?",
    "What gas do plants absorb from the air?",
    "Which ocean is the largest in the world?"
]

answers = [
    "Islamabad",
    "Muhammad Ali Jinnah",
    "Pakistani Rupee",
    "Urdu",
    "Karachi",
    "Central Processing Unit",
    "Mars",
    "Kidney",
    "Carbon Dioxide",
    "Pacific Ocean"
]

questions = [
    "What is the capital of Pakistan?",
    "Who was the founder of Pakistan?",
    "Which currency is used in Pakistan?",
    "What is the national language of Pakistan?",
    "Which city is known as the City of Lights?",
    "What does CPU stand for in computers?",
    "Which planet is known as the Red Planet?",
    "Which organ purifies blood in the human body?",
    "What gas do plants absorb from the air?",
    "Which ocean is the largest in the world?"
]

answers = [
    "Islamabad",
    "Muhammad Ali Jinnah",
    "Pakistani Rupee",
    "Urdu",
    "Karachi",
    "Central Processing Unit",
    "Mars",
    "Kidney",
    "Carbon Dioxide",
    "Pacific Ocean"
]

options = [
    ["A. Lahore", "B. Karachi", "C. Islamabad", "D. Peshawar"],
    ["A. Allama Iqbal", "B. Liaquat Ali Khan", "C. Zulfikar Ali Bhutto", "D. Muhammad Ali Jinnah"],
    ["A. Indian Rupee", "B. Pakistani Rupee", "C. Dollar", "D. Dinar"],
    ["A. Punjabi", "B. Sindhi", "C. Urdu", "D. English"],
    ["A. Islamabad", "B. Karachi", "C. Lahore", "D. Quetta"],
    ["A. Central Processing Unit", "B. Control Power Unit", "C. Computer Processing Utility", "D. Central Power Unit"],
    ["A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"],
    ["A. Heart", "B. Liver", "C. Kidney", "D. Lungs"],
    ["A. Oxygen", "B. Hydrogen", "C. Carbon Dioxide", "D. Nitrogen"],
    ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"]
]


prizes = [
    1000,
    2000,
    5000,
    10000,
    20000,
    33000,
    50000,
    66000,
    80000,
    100000
]


hints = [
    "It starts with the letter 'I' and is a planned city.",
    "He is known as the founder of Pakistan.",
    "It’s the official currency of Pakistan.",
    "It's the national language of Pakistan.",
    "It's the capital city of Pakistan.",
    "It's the brain of the computer.",
    "It's the largest planet in our solar system.",
    "It pumps blood throughout your body.",
    "We breathe it in.",
    "It’s the largest ocean on Earth."
]

prize_won=0
checkpoint=0
print("==========================================")
print("        🎙️  KON BANEGA CROREPATI 🇵🇰")
print("==========================================")
print("💡 Lifelines: Hint")
print("👉 Type A, B, C, or D to answer")
print("🔁 Or type 'Hint' to use a Hint")
print("🚪 Or type 'quit' to walk away")
print("==========================================")
i=1
hint=0
for iteration in range(len(questions)):
    print(f"\nQuestion {i} for Rs{prizes[iteration]}")        
    print(f"Question {i} on screen now\n\n{questions[iteration]}")
    print(options[iteration])
    response=(input("Enter your answer as per options: ")).strip().lower()
    if(response=="quit"):
        break
    if(response=="hint" and hint<2):
        print(f"Your hint is {hints[iteration]}")
        response=input("Enter your respose now: ").strip().lower()
    elif(response=="hint" and hint==2):
        print("Sorry u ran out of Hints")
        response=input("Enter your respose now: ").strip().lower()

    ans_lower=answers[iteration]
    if(response==ans_lower.lower()):
        print(f"Congratulations u won {prizes[iteration]}")
        prize_won=prizes[iteration]
        if(prize_won==prizes[5] or prize_won==prizes[7]):
            print("Checkpoint reached")
            checkpoint+=1
        elif(prize_won==prizes[9]):
            print("You won the Jackpot! Congratulations on winning a 100,00RS")
            quit()
    else:
        print("Sorry your answer is wrong!")
        print("Correct answer is",answers[iteration])
        if(checkpoint==0):
            print("Sorry u got no money")
        elif(checkpoint==1):
            print("You got 33,000")
        else:
            print("You got 66,000")
        quit()

    i+=1
    hint+=1

            