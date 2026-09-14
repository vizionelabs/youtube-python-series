# ==============================================================================
# VIZIONE LABS - PYTHON FUNDAMENTALS PRACTICE
# Lesson 05: Loops (for loop), Range Function, and Execution Flow
# File: practice/exercise_01.py
# ==============================================================================

# --- PART 1: Basic Iteration Over a Sequence (List) ---
# A 'for' loop requests an iterator object from a sequence.
# In each iteration, the variable 'client_tier' receives the next item.
client_tiers = ["Starter", "Professional", "Enterprise", "Custom"]

print("--- Iterating Over List Items ---")
for client_tier in client_tiers:
    # Execution block indented inside the loop body
    print(f"Processing Vizione Labs Tier: {client_tier}")


# --- PART 2: Generating Sequences with range() ---
# The range() function creates an immutable sequence of numbers.
# Syntax: range(start, stop, step)
# Note: 'stop' is exclusive (up to, but not including).

print("\n--- Generating Index Ranges with range(stop) ---")
# Generates numbers: 0, 1, 2, 3, 4
for index in range(5):
    print(f"Audit Counter Index: {index}")


print("\n--- Ranged Iteration with range(start, stop, step) ---")
# Generates numbers starting at 10, up to 50, incrementing by 10
for account_id in range(100, 500, 100):
    print(f"Auditing Vizione Labs Account ID: VIZ-{account_id}")


# --- PART 3: Accumulator Pattern & Range Aggregation ---
# Combining 'for' loops with an accumulator variable to compute totals.
monthly_api_calls = [1200, 4500, 8900, 3100, 15000]
total_system_usage = 0

print("\n--- Accumulating Values Across Iteration ---")
for call_count in monthly_api_calls:
    total_system_usage += call_count
    print(f"Added {call_count} calls | Running Total: {total_system_usage}")

print(f"\nFinal Aggregate Platform Usage: {total_system_usage} total API requests.")