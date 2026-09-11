# ==============================================================================
# LESSON 01: LANGUAGE FUNDAMENTALS - STRINGS, PRINT, INPUT & VARIABLES
# ==============================================================================

# 1. THE PRINT FUNCTION AND STRINGS
# In Python, text is represented as a String (a sequence of characters wrapped in quotes).
# We use the built-in print() function to output text directly to the console terminal.
print("=== PYTHON FUNDAMENTALS PRACTICE ===")
print("Welcome to Vizione Labs Developer Environment.")

# 2. STRING CONCATENATION & ESCAPE CHARACTERS
# You can join (concatenate) multiple strings together using the + operator.
# The \n escape character creates a new line break inside a single string.
print("System Status: Online\n" + "Environment: Local PyCharm Terminal")

# 3. THE INPUT FUNCTION
# The input() function pauses code execution and waits for the user to type text in the terminal.
# Whatever the user types is captured as a string value.
# Note: Uncommenting the line below would trigger an interactive prompt in your terminal:
# input("Press Enter to continue setup...")

# 4. VARIABLE ASSIGNMENT
# Variables are containers in memory used to store data values for later use in your program.
# We assign a value to a variable name using the single equals sign (=).
developer_name = "Lucas"
active_role = "Automation Architect"

# 5. COMBINING VARIABLES WITH PRINT & INPUT
# We can dynamically pull data stored inside variables and print them out.
print("Lead Developer: " + developer_name)
print("Current Role: " + active_role)

# Here we prompt the user for input and immediately store their response inside a variable:
project_tag = input("Enter your current project tag name: ")

# Finally, we output a confirmation message using the variable we just captured:
print("Initializing environment workspace for project: " + project_tag)