# practice/exercise_01.py
"""
Vizione Labs — Python: Build Real Projects
Lesson 02: Primitive Data Types, Type Casting, Math Operations & String Interpolation

This fundamental script demonstrates:
1. Primitive Data Types (str, int, float, bool)
2. Explicit Type Casting (str(), int(), float(), bool())
3. Basic & Advanced Mathematical Operations
4. Operator Precedence (PEMDAS / BODMAS)
5. Historical String Formatting Methods vs. Modern f-Strings
"""

# ==============================================================================
# 1. PRIMITIVE DATA TYPES
# ==============================================================================
# Primitive types hold single, fundamental data values in Python.

service_name = "Cloud Database Optimization"  # String (str): Text enclosed in quotes
service_hours = 12                            # Integer (int): Whole number
hourly_rate = 85.50                           # Floating-Point (float): Decimal number
is_active_client = True                        # Boolean (bool): Binary True or False

print("--- 1. PRIMITIVE DATA TYPES ---")
print("Service Name:", service_name, "| Type:", type(service_name))
print("Service Hours:", service_hours, "| Type:", type(service_hours))
print("Hourly Rate:", hourly_rate, "| Type:", type(hourly_rate))
print("Active Status:", is_active_client, "| Type:", type(is_active_client))
print()

# ==============================================================================
# 2. EXPLICIT TYPE CASTING
# ==============================================================================
# Type casting is the explicit conversion of a variable from one data type to another.

raw_discount_input = "15"      # User input usually comes in as a string
raw_tax_rate_input = "0.08"    # String representing decimal tax

# Converting strings to numerical types
discount_percentage = int(raw_discount_input)       # Converts "15" -> 15 (int)
tax_rate = float(raw_tax_rate_input)               # Converts "0.08" -> 0.08 (float)

# Converting numerical types to strings
subtotal_amount = 1026.0
formatted_amount_str = str(subtotal_amount)         # Converts 1026.0 -> "1026.0" (str)

print("--- 2. EXPLICIT TYPE CASTING ---")
print("Converted Discount (int):", discount_percentage, "| Type:", type(discount_percentage))
print("Converted Tax Rate (float):", tax_rate, "| Type:", type(tax_rate))
print("Converted String Amount (str):", formatted_amount_str, "| Type:", type(formatted_amount_str))
print()

# ==============================================================================
# 3. MATHEMATICAL OPERATIONS & OPERATOR PRECEDENCE
# ==============================================================================
# Python provides built-in operators for performing calculations.

base_cost = service_hours * hourly_rate            # Multiplication (*) -> 12 * 85.50 = 1026.0
discount_value = base_cost * (discount_percentage / 100) # Division (/) produces float
taxed_cost = (base_cost - discount_value) * (1 + tax_rate) # Addition (+) and Subtraction (-)

# Advanced Math Operators
server_capacity = 2 ** 3                          # Exponentiation (**): 2^3 = 8
split_installments = 1026 // 4                     # Floor Division (//): Truncates decimal (1026 // 4 = 256)
remaining_cents = 1026 % 4                         # Modulus (%): Returns remainder of division

print("--- 3. MATHEMATICAL OPERATIONS ---")
print("Base Cost:", base_cost)
print("Discount Value:", discount_value)
print("Taxed Cost:", taxed_cost)
print("2 ^ 3 Capacity:", server_capacity)
print("Floor Division (1026 // 4):", split_installments)
print("Modulus Remainder (1026 % 4):", remaining_cents)
print()

# ==============================================================================
# 4. STRING INTERPOLATION: HISTORICAL METHODS VS. MODERN F-STRINGS
# ==============================================================================
# Before f-strings (introduced in Python 3.6), Python developers used three older methods
# to combine text and variables. Here is how formatting evolved:

client_name = "Vizione Tech Corp"
total_estimate = taxed_cost  # 1001.376

print("--- 4. STRING FORMATTING EVOLUTION ---")

# --- OLD METHOD 1: Plus (+) Concatenation ---
# Requires manual string conversion for every non-string variable using str().
# If you forget str(), Python raises a TypeError.
old_way_concat = "Client: " + client_name + " | Hours: " + str(service_hours) + " | Total: $" + str(total_estimate)
print("Old Method 1 (Plus Concatenation):")
print(old_way_concat)
print()

# --- OLD METHOD 2: C-Style Percent (%) Formatting ---
# Uses %s for strings, %d for integers, and %f for floats.
# Requires matching variable order at the end inside a tuple.
old_way_percent = "Client: %s | Hours: %d | Total: $%.2f" % (client_name, service_hours, total_estimate)
print("Old Method 2 (Percent % Operator):")
print(old_way_percent)
print()

# --- OLD METHOD 3: .format() Method ---
# Introduced in Python 2.7 / 3.0. Uses curly braces {} as placeholders.
# Better than older methods, but still verbose for long strings.
old_way_dot_format = "Client: {} | Hours: {} | Total: ${:.2f}".format(client_name, service_hours, total_estimate)
print("Old Method 3 (.format() Method):")
print(old_way_dot_format)
print()

# --- MODERN METHOD: f-Strings (Python 3.6+) ---
# Modern Python standard. Prefixed with 'f', variables and math expressions
# are placed directly inside braces {} without needing str() or external tuple mappings.
modern_fstring = f"Client: {client_name} | Hours: {service_hours} | Total: ${total_estimate:.2f}"
print("Modern Method (f-String Interpolation):")
print(modern_fstring)