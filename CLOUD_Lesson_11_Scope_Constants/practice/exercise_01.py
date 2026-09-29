"""
Vizione Labs - Track A: Python: Build Real Projects
Lesson 11: Local vs. Global Scope, Constants, Namespace Management, Global Mutations
File: practice/exercise_01.py

Purpose:
Demonstrate the fundamental mechanics of local and global namespaces, block-scope
rules in Python, constant naming conventions, and explicit global mutation patterns.
"""

# ==============================================================================
# 1. MODULE-LEVEL CONSTANTS & GLOBAL SCOPE
# ==============================================================================
# PEP 8 standard SCREAMING_SNAKE_CASE indicates module-level constants.
# In Python, constants are enforced by convention, residing in the global namespace.
SYSTEM_TAX_RATE = 0.15
APP_ENVIRONMENT = "DEVELOPMENT"

# Global variable declared at the module level
current_active_users = 100


# ==============================================================================
# 2. LOCAL SCOPE & ISOLATED NAMESPACES
# ==============================================================================
def calculate_invoice(subtotal):
    """
    Demonstrates local scope isolation.
    Variable 'tax_amount' and parameter 'subtotal' exist ONLY inside this function's local scope.
    """
    # Reading global constant (SYSTEM_TAX_RATE) inside local scope
    tax_amount = subtotal * SYSTEM_TAX_RATE
    total = subtotal + tax_amount
    print(f"[LOCAL SCOPE] Inside calculate_invoice() -> Total: ${total:.2f}")
    return total


# ==============================================================================
# 3. GLOBAL MUTATIONS & THE 'global' KEYWORD
# ==============================================================================
def register_new_user():
    """
    Demonstrates explicit modification of a global variable inside a local scope.
    Uses the 'global' keyword to bind 'current_active_users' to the module-level namespace.
    """
    global current_active_users
    current_active_users += 1
    print(f"[GLOBAL MUTATION] Inside register_new_user() -> Active Users updated to: {current_active_users}")


# ==============================================================================
# 4. PYTHON BLOCK SCOPE RULES
# ==============================================================================
def demonstrate_block_scope():
    """
    Demonstrates that block structures (if/else, for, while) do NOT create new local namespaces.
    Variables defined inside 'if' blocks remain accessible outside the block in function scope.
    """
    user_status = "PREMIUM"

    if user_status == "PREMIUM":
        # 'discount_tier' is defined inside the 'if' block
        discount_tier = "Tier 1 - 20% Off"

    # In languages like C++ or Java, 'discount_tier' would raise an out-of-scope error.
    # In Python, 'discount_tier' is accessible throughout the enclosing function scope.
    print(f"[BLOCK SCOPE DEMO] Discount Tier evaluated outside IF block: {discount_tier}")


# ==============================================================================
# MAIN PRACTICE EXECUTION FLOW
# ==============================================================================
if __name__ == "__main__":
    print("=== LESSON 11: SCOPE, CONSTANTS & NAMESPACES PRACTICE ===\n")

    # 1. Inspecting Initial Global Variables
    print(f"[GLOBAL NAMESPACE] Environment: {APP_ENVIRONMENT}")
    print(f"[GLOBAL NAMESPACE] Initial Active Users: {current_active_users}")
    print(f"[GLOBAL NAMESPACE] Standard System Tax Rate: {SYSTEM_TAX_RATE}\n")

    # 2. Function Call & Local Scope Verification
    order_total = calculate_invoice(200.0)

    # Verification: Attempting to access local variable 'tax_amount' globally would raise a NameError.
    # Uncommenting the line below will trigger: NameError: name 'tax_amount' is not defined
    # print(tax_amount)

    # 3. Global Variable Mutation Execution
    print("\n--- Executing Global State Modification ---")
    register_new_user()
    print(f"[GLOBAL NAMESPACE] Post-mutation Active Users count: {current_active_users}\n")

    # 4. Block Scope Mechanics
    print("--- Executing Block Scope Test ---")
    demonstrate_block_scope()
    print("\n=== PRACTICE EXECUTION COMPLETE ===")