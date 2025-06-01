#!/usr/bin/env python3
"""
Pattern Drawing
This script draws a square pattern of asterisks using nested loops.
"""

# Get user input for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Print asterisks for each row
    for col in range(size):
        print("*", end="")
    # Move to next line after each row
    print()
    row += 1 