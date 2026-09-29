"""
==============================================================================
Vizione Labs — Python: Build Real Projects Series
Lesson 10: Functions with Return Values, Docstrings, Multi-Return & Recursion
File: practice/exercise_01.py
==============================================================================
"""


# ------------------------------------------------------------------------------
# 1. Functions with Return Values & Docstrings
# ------------------------------------------------------------------------------
def calculate_formatted_name(first_name: str, last_name: str) -> str:
    """
    Takes a first and last name, strips extra whitespace, title-cases them,
    and returns a clean full name string.
    """
    clean_first = first_name.strip().title()
    clean_last = last_name.strip().title()
    return f"{clean_first} {clean_last}"


# Calling the function and capturing the returned string in a variable
developer_name = calculate_formatted_name("  lucas ", " QUAIA  ")
print(f"Formatted Developer Name: {developer_name}")


# ------------------------------------------------------------------------------
# 2. Multi-Return Logic & Early Exits
# ------------------------------------------------------------------------------
def validate_and_categorize_score(score: float):
    """
    Evaluates a numeric test or assessment score.
    Returns early with a status tuple: (is_valid: bool, category: str).
    """
    if score < 0 or score > 100:
        return False, "Invalid Score (Out of Range)"

    if score >= 90:
        return True, "Tier 1 — Mastery"
    elif score >= 75:
        return True, "Tier 2 — Proficient"
    elif score >= 60:
        return True, "Tier 3 — Competent"
    else:
        return True, "Tier 4 — Needs Review"


# Testing multiple return branches
is_valid_1, tier_1 = validate_and_categorize_score(94.5)
is_valid_2, tier_2 = validate_and_categorize_score(58.0)
is_valid_3, tier_3 = validate_and_categorize_score(-10.0)

print(f"Score 94.5 -> Valid: {is_valid_1}, Category: {tier_1}")
print(f"Score 58.0 -> Valid: {is_valid_2}, Category: {tier_2}")
print(f"Score -10  -> Valid: {is_valid_3}, Category: {tier_3}")


# ------------------------------------------------------------------------------
# 3. Multiple Value Return (Tuple Unpacking)
# ------------------------------------------------------------------------------
def compute_dataset_bounds(numbers: list):
    """
    Calculates the minimum, maximum, and average of a list of numbers.
    Returns three distinct values via tuple packing.
    """
    if not numbers:
        return None, None, 0.0

    minimum_val = min(numbers)
    maximum_val = max(numbers)
    average_val = sum(numbers) / len(numbers)

    return minimum_val, maximum_val, average_val


sample_data = [12, 45, 67, 23, 89, 34]
min_num, max_num, avg_num = compute_dataset_bounds(sample_data)

print(f"Dataset Metrics -> Min: {min_num}, Max: {max_num}, Avg: {avg_num:.2f}")


# ------------------------------------------------------------------------------
# 4. Recursion Basics (Base Case & Call Stack)
# ------------------------------------------------------------------------------
def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a positive integer n using recursion.
    n! = n * (n - 1) * ... * 1
    """
    # Base Case: Stops the recursion stack
    if n <= 1:
        return 1

    # Recursive Step: Function calls itself with a reduced parameter
    return n * calculate_factorial(n - 1)


factorial_5 = calculate_factorial(5)
print(f"Factorial of 5 (5!): {factorial_5}")