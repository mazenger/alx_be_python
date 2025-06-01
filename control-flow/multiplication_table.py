#!/usr/bin/env python3
"""
Multiplication Table Generator
This script generates a multiplication table for a given number using a for loop.
"""

# Get user input for the number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}") 