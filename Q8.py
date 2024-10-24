# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:36:37 2024

@author: DELL
"""

# Define the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Get the search term from the user
search_name = input("Enter the name you are looking for: ")

# Check if the name is in the list and print appropriate message
if search_name in names:
    print(f"{search_name} found in the list!")
else:
    print(f"{search_name} not found in the list.")