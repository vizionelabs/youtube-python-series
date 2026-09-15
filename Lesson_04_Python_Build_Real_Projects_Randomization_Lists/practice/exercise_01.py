# ==============================================================================
# VIZIONE LABS - PRACTICE EXERCISE 01
# Topic: Python Lists, Indexing, Mutability & Randomization
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# 1. LIST CREATION AND INDEXING
# ------------------------------------------------------------------------------
# Lists store ordered sequences of items enclosed in square brackets.
executives = ["Alice", "Bob", "Charlie", "Diana"]

# Accessing elements using zero-based indexing
first_executive = executives[0]
second_executive = executives[1]
last_executive = executives[-1]  # Negative indexing accesses from the end

print(f"First Executive: {first_executive}")
print(f"Second Executive: {second_executive}")
print(f"Last Executive: {last_executive}")

# ------------------------------------------------------------------------------
# 2. LIST MUTABILITY AND DYNAMIC MODIFICATION
# ------------------------------------------------------------------------------
# Lists are mutable; elements can be updated, appended, or removed.
executives[1] = "Robert"  # Replaces 'Bob' with 'Robert'
executives.append("Edward")  # Appends 'Edward' to the end of the list

print(f"Updated Executive List: {executives}")
print(f"Total Executives Count: {len(executives)}")

# ------------------------------------------------------------------------------
# 3. RANDOM SELECTION (random.choice & random.randint)
# ------------------------------------------------------------------------------
# Selecting a random element directly using random.choice
random_rep = random.choice(executives)
print(f"Randomly Selected Executive (choice): {random_rep}")

# Selecting a random element using random.randint and list index
# Note: list indices range from 0 to len(list) - 1
random_index = random.randint(0, len(executives) - 1)
indexed_rep = executives[random_index]
print(f"Randomly Selected Executive (randint index {random_index}): {indexed_rep}")

# ------------------------------------------------------------------------------
# 4. PREVENTING INDEXERRORS (INDEX OUT OF RANGE)
# ------------------------------------------------------------------------------
# Attempting to access an index equal to len(list) raises an IndexError.
# Safe boundary check before accessing arbitrary index positions:
target_index = 5

if target_index < len(executives):
    print(f"Target Executive: {executives[target_index]}")
else:
    print(f"Index {target_index} is out of bounds for list size {len(executives)}.")