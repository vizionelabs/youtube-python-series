"""
Vizione Labs — Python: Build Real Projects Series
Lesson 01: Variables, Data Types, and User Input
File: practice/exercise_01.py

Description: Teachable, standalone practice script demonstrating core language mechanics:
1. Variable instantiation and memory binding
2. Primitive data types (str, int, float, bool)
3. Dynamic user input capture via input()
4. Explicit type casting (str -> int, str -> float)
5. String formatting using f-strings
"""

# ==============================================================================
# SECTION 1: VARIABLE DECLARATION & PRIMITIVE TYPES
# ==============================================================================
# Variables are named references pointing to objects in memory.
developer_name = "Lucas"      # String (str)
assigned_tasks = 5            # Integer (int)
system_load = 0.85            # Floating-point (float)
is_active_member = True       # Boolean (bool)

print("--- Section 1: Memory & Primitive Types ---")
print("Developer Name:", developer_name, "| Type:", type(developer_name))
print("Assigned Tasks:", assigned_tasks, "| Type:", type(assigned_tasks))
print("System Load:", system_load, "| Type:", type(system_load))
print("Active Status:", is_active_member, "| Type:", type(is_active_member))
print()

# ==============================================================================
# SECTION 2: USER INPUT & TYPE CASTING
# ==============================================================================
# Note: input() ALWAYS returns data as a string (str). Explicit conversion is required.
print("--- Section 2: User Input & Explicit Type Casting ---")

raw_user_name = input("Enter member full name: ")
raw_experience_years = input("Enter years of development experience: ")
raw_hourly_rate = input("Enter expected hourly rate (USD): ")

# Explicit Type Conversion (Casting)
experience_years = int(raw_experience_years)
hourly_rate = float(raw_hourly_rate)

print("\nVerifying Converted Types:")
print("raw_experience_years type:", type(raw_experience_years), "-> experience_years type:", type(experience_years))
print("raw_hourly_rate type:", type(raw_hourly_rate), "-> hourly_rate type:", type(hourly_rate))
print()

# ==============================================================================
# SECTION 3: STRING INTERPOLATION & EXPRESSIONS
# ==============================================================================
# Formatted String Literals (f-strings) provide clean, performant string interpolation.
print("--- Section 3: Summary Output via F-Strings ---")

annual_capacity_hours = experience_years * 2000
projected_income = annual_capacity_hours * hourly_rate

summary_card = f"""
+-------------------------------------------------------+
| VIZIONE LABS — MEMBER ONBOARDING CARD                 |
+-------------------------------------------------------+
| Member Name      : {raw_user_name}
| Experience       : {experience_years} years
| Hourly Rate      : ${hourly_rate:.2f}/hr
| Est. Annual Cap. : {annual_capacity_hours} hours
| Projected Income : ${projected_income:,.2f}
+-------------------------------------------------------+
"""

print(summary_card)