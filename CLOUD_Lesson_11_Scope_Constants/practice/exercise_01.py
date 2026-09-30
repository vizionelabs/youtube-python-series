"""
Vizione Labs - Track A: Python: Build Real Projects
Lesson 11: Local vs. Global Scope, Constants, Namespace Management, Global Mutations
File: practice/exercise_01.py

Purpose:
Demonstrate the mechanics of local and global namespaces, block-scope rules,
constant naming conventions, explicit global declaration bindings, side-effect hazards,
and the safe production pure-return pattern for state management.
"""

# ==============================================================================
# 1. MODULE-LEVEL CONSTANTS & GLOBAL SCOPE (THE COURTYARD)
# ==============================================================================
# PEP 8 standard SCREAMING_SNAKE_CASE indicates module-level constants.
# In Python, constants reside in the global namespace (the "courtyard").
SYSTEM_TAX_RATE = 0.15
APP_ENVIRONMENT = "DEVELOPMENT"

# Global state variable declared at the module level (the courtyard)
current_active_users = 100


# ==============================================================================
# 2. LOCAL SCOPE & ISOLATED NAMESPACES
# ==============================================================================
def calculate_invoice(subtotal):
    """
    Demonstrates local scope isolation.
    Variable 'tax_amount' and parameter 'subtotal' exist ONLY inside this function's local scope.
    It can read global constants (SYSTEM_TAX_RATE) through the one-way window.
    """
    tax_amount = subtotal * SYSTEM_TAX_RATE
    total = subtotal + tax_amount
    print(f"[LOCAL SCOPE] Inside calculate_invoice() -> Total: ${total:.2f}")
    return total


# ==============================================================================
# 3. GLOBAL DECLARATION BINDING & MUTATION
# ==============================================================================
def register_new_user():
    """
    Demonstrates a Global Declaration using the 'global' keyword.

    This does NOT create a new variable!
    It binds local assignments to the existing top-level 'current_active_users'
    variable living in the global courtyard, allowing in-place mutation.
    """
    global current_active_users  # Explicit binding statement to global scope
    current_active_users += 1
    print(f"[GLOBAL MUTATION] Inside register_new_user() -> Active Users mutated to: {current_active_users}")


# ==============================================================================
# 4. UNPREDICTABILITY & SIDE EFFECTS OF GLOBAL MUTATION
# ==============================================================================
def unexpected_system_reset():
    """
    Demonstrates how global mutations make systems unpredictable in large applications.
    A function silently reaching out to change global state can wipe out critical
    application data without caller awareness (hidden side effect).
    """
    global current_active_users
    # Dangerous side effect: Silently resetting global state to zero
    current_active_users = 0
    print("[SIDE EFFECT ALERT] unexpected_system_reset() silently wiped global active users to 0!")


# ==============================================================================
# 5. SAFER PRODUCTION BEST PRACTICE: THE PURE RETURN PATTERN
# ==============================================================================
def register_user_safely(current_count):
    """
    Demonstrates the Industry Best Practice: Pure Function with Return Value.

    Instead of modifying global variables directly inside the function:
    1. Receive the current state as an argument (input parameter).
    2. Compute the calculation strictly within local scope.
    3. Return the newly calculated value.

    The caller explicitly re-assigns the global state in the main execution flow.
    """
    updated_count = current_count + 1
    print(f"[SAFE PATTERN] Calculated new user count inside local scope: {updated_count}")
    return updated_count


# ==============================================================================
# 6. PYTHON BLOCK SCOPE RULES
# ==============================================================================
def demonstrate_block_scope():
    """
    Demonstrates that block structures (if/else, for, while) do NOT create new local namespaces.
    Variables defined inside an 'if' block remain accessible throughout the function scope.
    """
    user_status = "PREMIUM"

    if user_status == "PREMIUM":
        discount_tier = "Tier 1 - 20% Off"

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

    # 2. Local Scope Isolation
    order_total = calculate_invoice(200.0)

    # 3. Global Declaration Binding Execution
    print("\n--- Executing Global Declaration Binding ---")
    register_new_user()
    print(f"[GLOBAL NAMESPACE] Post-mutation Active Users count: {current_active_users}\n")

    # 4. Unpredictability & Side Effects Hazard
    print("--- Demonstrating Global Side Effect Hazard ---")
    unexpected_system_reset()
    print(f"[GLOBAL NAMESPACE] Active Users post-reset (Corrupted State): {current_active_users}\n")

    # 5. Executing Industry Best Practice (Pure Function Return Pattern)
    print("--- Executing Industry Best Practice (Safe Pure Return Pattern) ---")
    # State update is explicit, controlled, and visible in the main execution flow
    current_active_users = register_user_safely(current_active_users)
    print(f"[GLOBAL NAMESPACE] Active Users post-safe update: {current_active_users}\n")

    # 6. Block Scope Mechanics
    print("--- Executing Block Scope Test ---")
    demonstrate_block_scope()
    print("\n=== PRACTICE EXECUTION COMPLETE ===")