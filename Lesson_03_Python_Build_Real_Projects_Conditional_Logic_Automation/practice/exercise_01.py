# ==============================================================================
# VZIONE LABS - PYTHON FUNDAMENTALS PRACTICE
# Lesson 03: Conditional Logic, Control Flow & Boolean Operators
# File Path: practice/exercise_01.py
# ==============================================================================

# --- 1. Basic Comparison Operators ---
# We define primitive variables to evaluate standard relational conditions.
client_lead_score = 85
minimum_threshold = 70

# Comparison operators evaluate to raw Boolean values (True or False)
is_qualified = client_lead_score >= minimum_threshold
print("Is the lead score qualified?:", is_qualified)


# --- 2. Standard Branching Control Flow (if / elif / else) ---
# Evaluating exclusive conditional branches based on numerical ranges.
if client_lead_score >= 90:
    # Executes only if client_lead_score is 90 or above
    lead_category = "Enterprise Tier 1"
elif client_lead_score >= 70:
    # Executes if first condition failed, but score is 70 or above
    lead_category = "Mid-Market Tier 2"
else:
    # Fallback branch if all preceding expressions evaluate to False
    lead_category = "Unqualified Lead"

print("Assigned Lead Category:", lead_category)


# --- 3. Boolean Logical Operators (and, or, not) ---
# Combining multiple conditions into a single logical evaluation.
has_budget_approval = True
has_signed_nda = False

# 'and' requires both operands to evaluate to True
can_schedule_demo = (client_lead_score >= 70) and has_budget_approval
print("Can schedule enterprise demo?:", can_schedule_demo)

# 'or' requires at least one operand to evaluate to True
is_vip_or_signed = (lead_category == "Enterprise Tier 1") or has_signed_nda
print("Has VIP Status or Signed NDA?:", is_vip_or_signed)

# 'not' reverses the Boolean evaluation of an expression
is_nda_pending = not has_signed_nda
print("Is NDA still pending signature?:", is_nda_pending)