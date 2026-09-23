# ==============================================================================
# Vizione Labs — Python: Build Real Projects
# Lesson 01: Printing, String Manipulation, Input Function, Variable Assignment
# File: practice/exercise_01.py
# ==============================================================================

# 1. Basic Output Printing
print("Welcome to Vizione Labs - Python Fundamentals!")

# 2. String Manipulation (Newline Escapes & Concatenation)
print("Module 1: Core Concepts\nStatus: Active\n" + "----------------------------------------")

# 3. Input Function & Variable Assignment
user_name = input("Enter your developer name: ")
target_role = input("Enter your target software role: ")

# 4. Input Sanitization & String Operations
clean_name = user_name.strip().title()
clean_role = target_role.strip().title()

# 5. Output Construction with Variable Concatenation
greeting_message = "Developer Profile Initialized: " + clean_name + " | Target Role: " + clean_role
print("\n" + greeting_message)

# 6. Variable Reassignment & Dynamic State Tracking
status_badge = "Status: Onboarding"
print("Initial Badge: " + status_badge)

status_badge = "Status: Active Developer"
print("Updated Badge: " + status_badge)