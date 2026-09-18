# ==============================================================================
# LESSON 01: CORE PYTHON FUNDAMENTALS
# File: practice/exercise_01.py
# Topics: Printing, String Manipulation, Input Function, Variable Assignment
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: THE PRINT FUNCTION & BASIC OUTPUT
# ------------------------------------------------------------------------------
# The print() function displays text or output on the terminal console screen.
# Text wrapped inside quotation marks (single or double) is called a String.

print("Welcome to Vizione Labs Developer Onboarding!")
print('Initializing local Python execution context...')


# ------------------------------------------------------------------------------
# SECTION 2: STRING MANIPULATION & CONCATENATION
# ------------------------------------------------------------------------------
# You can combine strings together using the plus (+) operator.
# Backslash-n (\n) creates a new line break inside a string.

print("Vizione Labs" + " " + "Automation Engine")
print("Line 1: System Check\nLine 2: Network Active\nLine 3: Ready")


# ------------------------------------------------------------------------------
# SECTION 3: THE INPUT FUNCTION
# ------------------------------------------------------------------------------
# The input() function pauses execution and waits for the user to type text.
# The user's input is returned directly into the program as a String.

input("Press Enter to continue client ingestion process...")


# ------------------------------------------------------------------------------
# SECTION 4: VARIABLE ASSIGNMENT & DYNAMIC DATA
# ------------------------------------------------------------------------------
# Variables are named containers that store data in memory for later use.
# Use the equals sign (=) to assign a value to a variable name.

developer_name = input("Enter your full developer name: ")
target_role = "Software Engineer"

print("Developer Registered:")
print(developer_name)
print("Assigned Role:")
print(target_role)

# You can reuse variables inside string concatenation:
print("Welcome aboard, " + developer_name + "! Your role is set to: " + target_role)