# ==============================================================================
# LESSON 01: PYTHON FUNDAMENTALS (PRACTICE EXERCISE)
# Topic: Printing, Strings, User Inputs, and Variables
# ==============================================================================

# 1. THE PRINT FUNCTION & STRINGS
# The print() function outputs text to the console screen.
# Anything enclosed inside single ('') or double ("") quotes is a String (text data).
print("=== WELCOME TO LESSON 01 PRACTICE ===")
print("Python executes code sequentially from top to bottom.")

# 2. STRING CONCATENATION
# You can join multiple strings together using the plus (+) operator.
print("Hello " + "Developer!")

# 3. THE INPUT FUNCTION
# The input() function pauses script execution and waits for user text entry in the terminal.
# Whatever the user types is returned as a string.
# NOTE: The input() function runs inside print() here to demonstrate nested execution.
print("User provided response: " + input("Type your name and press Enter: "))

# 4. VARIABLES & DATA STORAGE
# Variables act as named containers or labels in memory that store data values for later use.
# Here, we store the result of input() into a variable named 'client_name'.
client_name = input("Enter client name for storage: ")

# We can reuse the stored variable as many times as needed throughout our program.
print("Client successfully saved to memory!")
print("Stored Client Name: " + client_name)