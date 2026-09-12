# ==============================================================================
# LESSON 04: PYTHON LISTS & RANDOMIZATION FUNDAMENTALS
# Brand: Vizione Labs | Track A: Core Fundamentals & Scripting
# File: practice/exercise_01.py
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: Importing Built-in Modules
# ------------------------------------------------------------------------------
# Python includes a built-in module named 'random' for generating pseudorandom numbers.
import random

# ------------------------------------------------------------------------------
# SECTION 2: Working with Python Lists (Data Structures)
# ------------------------------------------------------------------------------
# A list is an ordered collection of items stored inside square brackets [].
# Lists can hold strings, numbers, booleans, or mixed data types.
team_members = ["Lucas", "Sarah", "Alex", "David", "Elena"]

# Printing the full list to the terminal
print("Initial Vizione Labs Team List:")
print(team_members)

# Accessing individual items using zero-based indexing:
# Index 0 is the first item ("Lucas")
# Index 1 is the second item ("Sarah")
first_member = team_members[0]
print(f"First member (Index 0): {first_member}")

# ------------------------------------------------------------------------------
# SECTION 3: List Mutability & Modifications
# ------------------------------------------------------------------------------
# Lists are mutable, meaning we can add, update, or remove elements after creation.

# Adding a new member to the end of the list using .append()
team_members.append("Marcus")
print("Updated list after adding Marcus:")
print(team_members)

# Removing an item from the list using .remove()
team_members.remove("Sarah")
print("Updated list after removing Sarah:")
print(team_members)

# ------------------------------------------------------------------------------
# SECTION 4: Random Selection Mechanics
# ------------------------------------------------------------------------------
# Generating a random integer between 0 and the total length of the list minus 1
# len() gives the total count of items in the list.
total_members = len(team_members)
print(f"Total active team members: {total_members}")

# Using random.randint(a, b) to get a random index
random_index = random.randint(0, total_members - 1)
assigned_lead = team_members[random_index]
print(f"Randomly selected team member via randint(): {assigned_lead}")

# Convenient alternative: random.choice() picks a random element directly from a list
direct_choice = random.choice(team_members)
print(f"Randomly selected team member via random.choice(): {direct_choice}")

# ------------------------------------------------------------------------------
# SECTION 5: Understanding Index Errors (IndexError)
# ------------------------------------------------------------------------------
# An IndexError occurs when trying to access an index that does not exist in the list.
# For example, if a list has 5 items, the valid indices are 0, 1, 2, 3, 4.
# Accessing index 5 will raise: IndexError: list index out of range.
# Un-comment the line below to observe the error in PyCharm:
# invalid_member = team_members[100]