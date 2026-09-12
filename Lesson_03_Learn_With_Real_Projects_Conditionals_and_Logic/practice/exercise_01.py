# ==============================================================================
# LESSON 03: FUNDAMENTALS OF CONDITIONAL LOGIC AND COMPARISON OPERATORS
# File: practice/exercise_01.py
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: BASIC COMPARISON OPERATORS AND IF/ELSE
# ------------------------------------------------------------------------------
# Comparison operators check relationships between values and evaluate to True or False:
# > (greater than), < (less than), >= (greater or equal), <= (less or equal), == (equal to), != (not equal)

client_budget = 5000

# Basic conditional check
if client_budget >= 5000:
    print("Budget status: High-value lead detected.")
else:
    print("Budget status: Standard lead detected.")

# ------------------------------------------------------------------------------
# SECTION 2: MULTI-WAY BRANCHING WITH ELIF
# ------------------------------------------------------------------------------
# Use 'elif' (short for else-if) to test multiple mutually exclusive conditions sequentially.

lead_score = 75

if lead_score >= 90:
    print("Lead Tier: Tier 1 (Enterprise)")
elif lead_score >= 70:
    print("Lead Tier: Tier 2 (Mid-Market)")
elif lead_score >= 50:
    print("Lead Tier: Tier 3 (SMB)")
else:
    print("Lead Tier: Unqualified Lead")

# ------------------------------------------------------------------------------
# SECTION 3: LOGICAL OPERATORS (AND, OR, NOT)
# ------------------------------------------------------------------------------
# 'and' requires BOTH conditions to be True.
# 'or' requires AT LEAST ONE condition to be True.
# 'not' reverses the Boolean evaluation (True becomes False, False becomes True).

has_signed_contract = True
has_paid_deposit = False
is_blacklisted = False

# Using 'and'
if has_signed_contract and has_paid_deposit:
    print("Project Status: Ready to kickoff!")
else:
    print("Project Status: Waiting for contract or deposit completion.")

# Using 'or'
if has_signed_contract or has_paid_deposit:
    print("Account Action: Client has taken initial onboard steps.")

# Using 'not'
if not is_blacklisted:
    print("Security Check: Client is approved for routing.")

# ------------------------------------------------------------------------------
# SECTION 4: NESTED CONDITIONALS
# ------------------------------------------------------------------------------
# Conditionals can be nested inside one another to handle multi-stage checks.

is_vip = True
project_deadline_days = 5

if is_vip:
    if project_deadline_days <= 7:
        print("Routing: Priority Rush Escalation to Senior Lead Engineer.")
    else:
        print("Routing: Standard VIP Queue Assignment.")
else:
    print("Routing: General Service Desk Queue.")