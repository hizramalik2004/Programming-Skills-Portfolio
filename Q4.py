# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:12:59 2024

@author: DELL
"""

# Dictionary with 10 European countries and their capitals
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen"
}

# Initialize the score
score = 0

# Loop through each question
for country, capital in questions.items():
    # Asking the user
    answer = input(f"What is the capital of {country}? ").lower()
    
    # Checking the answer and giving feedback
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

# Display the final score
print(f"Your final score is {score}/{len(questions)}")
