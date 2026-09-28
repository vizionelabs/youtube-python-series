# practice/exercise_01.py
# Vizione Labs — Python: Build Real Projects (Lesson 03)
# Topic: Conditional Statements, Comparison Operators, Logical Operators, Nested Logic

print("=== VIZIONE LABS: ACCESS CONTROL & LOGIC SIMULATOR ===")

# 1. basic Comparison & Conditional Branching (if / else)
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("[GRANT] Standard system access authorized.")
else:
    print("[DENY] Access restricted: User must be at least 18 years old.")

print("\n--- Testing Multi-Tier Access (if / elif / else) ---")

# 2. Multi-tier Conditionals (if / elif / else)
clearance_level = int(input("Enter clearance tier level (1-3): "))

if clearance_level == 1:
    print("[TIER 1] Basic System Access granted.")
elif clearance_level == 2:
    print("[TIER 2] Advanced System Access granted.")
elif clearance_level == 3:
    print("[TIER 3] Full Administrative Access granted.")
else:
    print("[INVALID] Unknown clearance tier provided.")

print("\n--- Testing Compound Conditions (Logical Operators: and, or, not) ---")

# 3. Logical Operators (and, or, not)
is_active = input("Is user account active? (yes/no): ").strip().lower() == "yes"
has_mfa = input("Is Multi-Factor Authentication enabled? (yes/no): ").strip().lower() == "yes"
is_suspended = input("Is user account suspended? (yes/no): ").strip().lower() == "yes"

# compound evaluation using AND, OR, NOT
if is_active and has_mfa and not is_suspended:
    print("[SECURE] Access granted to production dashboard.")
elif is_active and not has_mfa and not is_suspended:
    print("[WARNING] Access pending: Multi-Factor Authentication is required.")
else:
    print("[BLOCK] Access denied: Account is either inactive or suspended.")

print("\n--- Testing Nested Logic ---")

# 4. Nested Conditional Statements
is_employee = input("Are you an employee of Vizione Labs? (yes/no): ").strip().lower() == "yes"

if is_employee:
    department = input("Enter your department (engineering/marketing/other): ").strip().lower()
    if department == "engineering":
        print("[DEPLOY] Access to code repositories authorized.")
    elif department == "marketing":
        print("[ANALYTICS] Access to marketing metrics authorized.")
    else:
        print("[GENERAL] Access to general corporate portal authorized.")
else:
    print("[EXTERNAL] Non-employee detected. Redirecting to partner portal.")