"""
Vizione Labs - Python Fundamentals
Lesson 04: Randomization Modules, Lists, Data Structures & Index Safety

This script introduces fundamental list operations, index access,
random sampling mechanics, and safe array mutations.
"""

import random

# ==============================================================================
# 1. RANDOM MODULE BASICS
# ==============================================================================

# Generating pseudo-random integers within an inclusive range [a, b]
random_priority = random.randint(1, 10)
print(f"Generated Random Priority Score: {random_priority}")

# Generating a floating-point number in the range [0.0, 1.0)
random_weight = random.random()
print(f"Generated Weight Factor: {random_weight:.4f}")

# ==============================================================================
# 2. PYTHON LISTS & INDEXING MECHANICS
# ==============================================================================

# Initializing an ordered sequence of Vizione Labs client status tags
client_stages = ["Lead", "Qualified", "Proposal Sent", "Contract Signed"]

# Accessing elements using zero-based indexing
first_stage = client_stages[0]
latest_stage = client_stages[-1]  # Negative indexing accesses from the tail

print(f"Pipeline Entry Point: {first_stage}")
print(f"Pipeline Terminal Stage: {latest_stage}")

# ==============================================================================
# 3. SAFE INDEXING & PREVENTING INDEXERROR
# ==============================================================================

# Dynamic length calculation using len()
total_stages = len(client_stages)
print(f"Total Configured Stages: {total_stages}")

# Index Safety Rule: Valid indices range from 0 to (len - 1)
# Accessing client_stages[total_stages] would throw an IndexError exception!
safe_last_index = total_stages - 1
print(f"Verified Safe Tail Element: {client_stages[safe_last_index]}")

# ==============================================================================
# 4. RANDOM SELECTION FROM LISTS
# ==============================================================================

# Randomly picking a single element directly from a sequence
random_stage = random.choice(client_stages)
print(f"Randomly Sampled Stage for Audit: {random_stage}")

# Random shuffling (mutates the list in-place)
random.shuffle(client_stages)
print(f"Shuffled Pipeline Order: {client_stages}")