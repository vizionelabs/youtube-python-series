# ==============================================================================
# Vizione Labs — Track A: Python Automation & Scripting
# Lesson 12: Scope Mechanics, Block Scope & Variable Debugging
# File: practice/scope_exercise_01.py
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Global vs. Local Scope Basics
# ------------------------------------------------------------------------------
system_mode = "PRODUCTION"  # Global scope variable


def display_system_status():
    session_id = "SESS-89421"  # Local scope variable
    print(f"[LOCAL SCOPE] Active Session ID: {session_id}")
    print(f"[GLOBAL SCOPE READ] Current System Mode: {system_mode}")


display_system_status()

# Attempting to access local variable in global scope will raise NameError:
# print(session_id)  # NameError: name 'session_id' is not defined


# ------------------------------------------------------------------------------
# 2. Block Scope Myth in Python
# ------------------------------------------------------------------------------
# Python does NOT create new scope inside if/elif/else, for, or while blocks!

active_flag = True

if active_flag:
    block_scoped_variable = "Defined inside IF block"

# block_scoped_variable remains accessible in the enclosing scope
print(f"[BLOCK SCOPE DEMO] Variable created in IF block: {block_scoped_variable}")

for item_index in range(1, 4):
    last_processed_index = item_index

# last_processed_index leaks into the surrounding scope
print(f"[LOOP SCOPE DEMO] Last Processed Index: {last_processed_index}")


# ------------------------------------------------------------------------------
# 3. Modifying Global Variables safely vs. UnboundLocalError
# ------------------------------------------------------------------------------
global_counter = 100


def increment_counter_incorrect():
    # Attempting to modify global_counter without 'global' keyword causes UnboundLocalError
    # global_counter += 1  # UnboundLocalError: local variable 'global_counter' referenced before assignment
    pass

def increment_counter_explicit():
    global global_counter
    global_counter += 1
    print(f"[EXPLICIT GLOBAL MUTATION] Updated Counter: {global_counter}")


increment_counter_explicit()


def increment_counter_pure(current_value):
    """
    Best Practice: Avoid modifying global state directly.
    Pass variables as parameters and return updated values.
    """
    return current_value + 1


global_counter = increment_counter_pure(global_counter)
print(f"[RECOMMENDED FUNCTIONAL PATTERN] Updated Counter: {global_counter}")