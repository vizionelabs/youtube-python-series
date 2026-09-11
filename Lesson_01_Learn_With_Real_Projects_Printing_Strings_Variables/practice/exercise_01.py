# ==============================================================================
# LESSON 01: PYTHON FUNDAMENTALS (PRACTICE)
# Core Concepts: print(), input(), and Variable Assignment
# ==============================================================================

# 1. Outputting text to the terminal
# The print() function displays whatever text (string) is placed inside quotes.
print("=== VIZIONE LABS: PYTHON BASICS ===")
print("Initializing core system check...")

# 2. Capturing user input
# The input() function displays a prompt and waits for the user to type a response.
# Whatever the user types is captured as text (string data).
user_name = input("Enter your operator name: ")

# 3. Using variables in output
# A variable holds data in memory so we can reuse it later in our script.
print("Welcome to the system, " + user_name + "!")

# 4. Combining input and variable storage directly
company_name = input("Enter your business name: ")

# 5. Displaying stored data
print("System configured for: " + company_name)
print("Initialization complete.")