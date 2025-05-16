"""
Title:       Critical Thinking Assignment #1
Author:      Minh Nguyen
Created:     2025-05-16
Last Edited: 2025-05-16
Description: This program collects a student's name, three assignment names, and corresponding scores.
                It calculates the total and average score and displays a formatted grade report.
User Input:
        - Student's name (string)
        - Three assignment names (string)
        - Three assignment scores (float)
Program Output:
        - Student's name
        - Each assignment name with corresponding score (rounded to two decimal places)
        - Total score (rounded to two decimal places)
        - Average score (rounded to two decimal places)
"""

# Program Introduction
# -----------------------------
# Print a welcome message for the user.
print("Welcome to the Grade Report Generator!\n")

# Data Input: Student Information
# -----------------------------
# Prompt the user to input the name of the student.
student_name = input("Enter the student's name: ")

# Data Input: Assignment Names
# -----------------------------
# Ask the user to enter the names of three assignments.
print("\nPlease enter the names of three assignments.")
assignment_1 = input("Enter the name of Assignment 1: ")
assignment_2 = input("Enter the name of Assignment 2: ")
assignment_3 = input("Enter the name of Assignment 3: ")

# Data Input: Assignment Scores
# -----------------------------
# Ask the user to enter the score for each of the three assignments.
# Convert the input to float to allow for decimal values.
print("\nPlease enter the scores for each assignment.")
assignment_score_1 = float(input(f"Enter the score for {assignment_1}: "))
assignment_score_2 = float(input(f"Enter the score for {assignment_2}: "))
assignment_score_3 = float(input(f"Enter the score for {assignment_3}: "))

# Calculate the total score by summing the three assignment scores.
total_score = assignment_score_1 + assignment_score_2 + assignment_score_3

# Calculate the average score by dividing the total score by 3.
average_score = total_score / 3

# Display of Results: Grade Report
# -----------------------------
# Print a well-formatted grade report showing:
# - Student's name
# - Each assignment with its score (formatted to two decimal places)
# - Total and average score
print("\n--- Grade Report ---")
print(f"Student Name: {student_name}")
print(f"{assignment_1}: {assignment_score_1:.2f}")
print(f"{assignment_2}: {assignment_score_2:.2f}")
print(f"{assignment_3}: {assignment_score_3:.2f}")
print(f"Total Score: {total_score:.2f}")
print(f"Average Score: {average_score:.2f}")
print("---------------------")
