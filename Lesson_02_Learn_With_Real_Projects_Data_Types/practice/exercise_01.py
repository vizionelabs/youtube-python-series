# ==============================================================================
# VIZIONE LABS | LEARN WITH REAL PROJECTS - LESSON 02
# File: practice/exercise_01.py
# Subject: Python Data Types, Type Casting, Math Operations & f-strings
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. PRIMITIVE DATA TYPES IN PYTHON
# ------------------------------------------------------------------------------
# Python automatically detects data types, but every piece of data belongs
# to a specific category.

# String (str): Text enclosed in quotes
agency_name = "Vizione Labs"

# Integer (int): Whole numbers without decimals
active_projects = 12

# Float (float): Numbers with decimal places
hourly_rate = 85.50

# Boolean (bool): True or False state evaluation
is_agency_active = True

# ------------------------------------------------------------------------------
# 2. CHECKING DATA TYPES WITH type()
# ------------------------------------------------------------------------------
# We can inspect the exact data type of any variable using type()
print("Checking variable data types:")
print(type(agency_name))       # Output: <class 'str'>
print(type(active_projects))   # Output: <class 'int'>
print(type(hourly_rate))       # Output: <class 'float'>
print(type(is_agency_active))  # Output: <class 'bool'>
print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. TYPE CASTING (CONVERTING DATA TYPES)
# ------------------------------------------------------------------------------
# Inputs from users or API forms always arrive as Strings.
# To perform calculations, we must convert Strings to Integers or Floats.

hours_worked_input = "40"  # This is a String because of quotes!

# Convert String -> Integer
hours_worked_int = int(hours_worked_input)

# Calculate total billable amount
total_earnings = hours_worked_int * hourly_rate
print("Calculated Total Earnings ($):")
print(total_earnings)
print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. BASIC MATHEMATICAL OPERATIONS
# ------------------------------------------------------------------------------
# Python supports standard math operations:
# Addition (+), Subtraction (-), Multiplication (*), Division (/)

subtotal = 1000.00
tax_rate = 0.10      # 10% tax rate
discount = 50.00     # Flat $50 discount

# Order of operations (PEMDAS) applies
tax_amount = subtotal * tax_rate
final_invoice_total = (subtotal + tax_amount) - discount

print("Invoice Calculation Breakdown:")
print("Tax Amount:", tax_amount)
print("Final Total:", final_invoice_total)
print("----------------------------------------")

# ------------------------------------------------------------------------------
# 5. STRING INTERPOLATION WITH F-STRINGS
# ------------------------------------------------------------------------------
# Instead of concatenating strings with '+', f-strings let us embed variables
# directly into text using curly braces `{}`.

client_name = "Acme Corp"
summary_message = f"Client {client_name} owes ${final_invoice_total} to {agency_name}."

print("Formatted Dynamic Summary:")
print(summary_message)