# ==============================================================================
# VIZIONE LABS — PYTHON BUILD REAL PROJECTS
# Lesson 01: Core Syntax Primitives (Printing, Strings, Inputs, Variables)
# File: practice/exercise_01.py
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. CONSOLE PRINTING & STRING LITERALS
# ------------------------------------------------------------------------------
# The print() function outputs data to the standard output stream (console).
# Strings are sequences of characters wrapped in single ('') or double ("") quotes.
print("==================================================")
print("   VIZIONE LABS — CLIENT ONBOARDING SYSTEM        ")
print("==================================================")

# ------------------------------------------------------------------------------
# 2. STRING ESCAPING & MULTI-LINE FORMATTING
# ------------------------------------------------------------------------------
# Use the escape character '\n' to insert a newline directly within a string.
# Double quotes can contain single quotes without requiring escape sequences.
print("System Status: Online\nEnvironment: Development")
print("Notice: 'Standard Terminal Ingestion' is active.")

# ------------------------------------------------------------------------------
# 3. USER INPUT INGESTION
# ------------------------------------------------------------------------------
# The input() function pauses execution, prints a prompt to the console,
# and reads a line of text entered by the user. It ALWAYS returns a string.
print("\n--- STAGE 1: ENTER CLIENT DETAILS ---")
client_name_input = input("Enter client company name: ")
contact_person_input = input("Enter primary contact person: ")

# ------------------------------------------------------------------------------
# 4. VARIABLE ASSIGNMENT & REFERENCE BINDING
# ------------------------------------------------------------------------------
# Variables in Python act as named references pointing to objects in memory.
# Here we assign user inputs and define system static variables.
client_company = client_name_input
primary_contact = contact_person_input
system_agent = "Vizione Automation Bot"

# ------------------------------------------------------------------------------
# 5. STRING CONCATENATION & OUTPUT
# ------------------------------------------------------------------------------
# Strings can be joined using the '+' operator (concatenation).
# We build a final confirmation payload message to display in the terminal.
greeting_header = "Client Record Created for: " + client_company
account_details = "Primary Point of Contact: " + primary_contact + " (Managed by " + system_agent + ")"

print("\n--- STAGE 2: INGESTION CONFIRMATION ---")
print(greeting_header)
print(account_details)
print("Status: Pending database verification...")