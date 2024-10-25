# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:48:45 2024

@author: Sofia Cinco
"""

"Exercise 4: Primitive Quiz"

# list of countries and their capitals
quiz_questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Austria": "Vienna"
}

# used function to ask a question and evaluate the answer
def ask_question(country, correct_answer):
    answer = input(f"What is the capital of {country}? ")
    if answer.strip().lower() == correct_answer.lower():  # to ignore the capitalization
        print("Good job!")
    else:
        print(f"Nope! The correct answer is {correct_answer}.")

# just to welcome the user or be interactive
print("Welcome to tonight's gameshow: The European Capital Quiz!")

# loop through each country and ask the question, I used for loop because there are no conditions
for country, capital in quiz_questions.items():
    ask_question(country, capital)

print("Thank you for participating! Until next time!")
