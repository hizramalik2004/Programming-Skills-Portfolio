# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:42:30 2024

@author: DELL
"""

# Function to determine if the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function to get user input and print the result
def main():
    # Ask the user for a number
    number = int(input("Enter a number: "))
    
    # Pass the number to the check_even_odd function
    result = check_even_odd(number)
    
    # Print the message returned by the function
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
