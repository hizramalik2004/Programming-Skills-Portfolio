# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:31:25 2024

@author: DELL
"""

# Step 1: Define the correct password
correct_password = "123456789"

# Step 2: Initialize the attempt counter
attempts = 5

# Step 3: Use a while loop to repeatedly ask the user for the password until the correct one is entered or attempts run out
while attempts > 0:
    entered_password = input(f"Enter the password (You have {attempts} attempts left): ")
    if entered_password == correct_password:
        print("Password is correct. Access granted!")
        break
    else:
        attempts -= 5
        print("Incorrect password.")
        
    # Step 4: Check if attempts run out
    if attempts == 0:
        print("Maximum attempts reached. Authorities have been alerted!")