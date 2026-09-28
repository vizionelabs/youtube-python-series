"""
Vizione Labs — Track A: Python: Build Real Projects
Lesson 04: Randomization Modules, Python Lists, Data Structures, Index Errors
File: practice/exercise_01.py

Objective:
Demonstrate standard library randomization (random.randint, random.choice),
list instantiation, zero-based positional indexing, mutability (.append, .extend),
and sequence boundary protection against IndexError exceptions.
"""

import random

def main():
    print("=== VIZIONE LABS: RANDOMIZATION & LIST DATA STRUCTURES ===")

    # -------------------------------------------------------------------------
    # 1. RANDOM NUMBER GENERATION
    # -------------------------------------------------------------------------
    # Generate a pseudo-random integer between inclusive boundaries [1, 100]
    random_score = random.randint(1, 100)
    print(f"[RANDOM INT] Generated Score (1-100): {random_score}")

    # Generate a random float in range [0.0, 1.0)
    random_float = random.random()
    print(f"[RANDOM FLOAT] Normalized Probability: {random_float:.4f}")

    # Simulate a coin flip using integer range boundaries [0, 1]
    coin_flip = random.randint(0, 1)
    outcome = "Heads" if coin_flip == 1 else "Tails"
    print(f"[COIN FLIP] Result: {outcome} (Value: {coin_flip})\n")

    # -------------------------------------------------------------------------
    # 2. LIST DATA STRUCTURE OPERATIONS
    # -------------------------------------------------------------------------
    # Initializing a sequence of engineering team roles
    engineering_roles = ["Frontend Engineer", "Backend Engineer", "DevOps Engineer"]
    print(f"[LIST INITIAL] Original Roles: {engineering_roles}")

    # Positional Zero-Indexed Access
    first_role = engineering_roles[0]
    last_role = engineering_roles[-1]
    print(f"[LIST INDEX] First Role [0]: {first_role}")
    print(f"[LIST INDEX] Last Role [-1]: {last_role}")

    # List Mutability: Appending a single element to the end of the sequence
    engineering_roles.append("Data Engineer")
    print(f"[LIST MUTATION] After .append(): {engineering_roles}")

    # List Mutability: Extending the sequence with another collection
    additional_roles = ["QA Automation Lead", "Cloud Architect"]
    engineering_roles.extend(additional_roles)
    print(f"[LIST MUTATION] After .extend(): {engineering_roles}\n")

    # -------------------------------------------------------------------------
    # 3. RANDOM CHOICE & BOUNDARY PROTECTION (INDEX ERROR PREVENTION)
    # -------------------------------------------------------------------------
    # Dynamic element selection using standard library choice
    assigned_role = random.choice(engineering_roles)
    print(f"[DYNAMIC CHOICE] Assigned Team Role: {assigned_role}")

    # Safe sequence length validation before positional indexing
    list_length = len(engineering_roles)
    print(f"[LIST LENGTH] Total Active Roles: {list_length}")

    # Demonstrating Boundary Safety
    # engineering_roles[list_length] -> Would raise IndexError: list index out of range
    # Valid maximum index is always (list_length - 1)
    safe_max_index = list_length - 1
    print(f"[SAFE ACCESS] Last element via index (len - 1 = {safe_max_index}): {engineering_roles[safe_max_index]}")

if __name__ == "__main__":
    main()