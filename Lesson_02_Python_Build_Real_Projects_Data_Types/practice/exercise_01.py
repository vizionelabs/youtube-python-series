# practice/exercise_01.py
# ==============================================================================
# VIZIONE LABS: PYTHON FUNDAMENTALS (LESSON 02)
# Primitive Data Types, Type Inspection, Type Casting & String Interpolation
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Primitive Data Types & Inspection
# ------------------------------------------------------------------------------
# String (str): Sequence of Unicode characters enclosed in quotes
company_name = "Vizione Labs"

# Integer (int): Whole numbers without decimal points
total_api_calls = 1500

# Floating-Point (float): Numbers containing a decimal point
tier_rate = 0.025

# Boolean (bool): Binary truth value (True or False)
is_active_account = True

# Inspecting data types at runtime using type()
print("company_name type:", type(company_name))
print("total_api_calls type:", type(total_api_calls))
print("tier_rate type:", type(tier_rate))
print("is_active_account type:", type(is_active_account))

# ------------------------------------------------------------------------------
# 2. Type Casting (Explicit Conversion)
# ------------------------------------------------------------------------------
# Simulated raw data payload received from an external API (always string format)
raw_input_calls = "2500"
raw_input_rate = "0.018"

# Converting strings to numeric types for mathematical operations
parsed_calls = int(raw_input_calls)
parsed_rate = float(raw_input_rate)

# Calculating raw usage cost
raw_usage_cost = parsed_calls * parsed_rate
print("Calculated Raw Usage Cost:", raw_usage_cost)

# Explicitly converting numeric values back to string for legacy concatenation
cost_summary_legacy = "Total Monthly Charge: $" + str(raw_usage_cost)
print("Legacy Concatenation Output:", cost_summary_legacy)

# ------------------------------------------------------------------------------
# 3. Mathematical Operations & Order of Operations (PEMDAS/BODMAS)
# ------------------------------------------------------------------------------
# Performing standard arithmetic operations
base_platform_fee = 100
discount_tier = 15
tax_multiplier = 1.10

# Formula: ((base_fee + usage_cost) - discount) * tax
final_invoice_amount = ((base_platform_fee + raw_usage_cost) - discount_tier) * tax_multiplier
print("Final Invoice Amount (Exact Float):", final_invoice_amount)

# Exponentiation (power) and Floor Division (integer division)
system_capacity_limit = 2 ** 10  # 1024 calls threshold
batch_processing_units = total_api_calls // 500  # Floor division yields int
print("System Capacity Limit:", system_capacity_limit)
print("Batch Units Allocated:", batch_processing_units)

# ------------------------------------------------------------------------------
# 4. Modern String Interpolation (f-strings)
# ------------------------------------------------------------------------------
# Inline formatting of expressions and rounding float precision to 2 decimal places
invoice_summary = (
    f"Client: {company_name} | "
    f"Calls: {parsed_calls} | "
    f"Base Rate: ${parsed_rate:.3f} | "
    f"Final Billed Total: ${final_invoice_amount:.2f} | "
    f"Active: {is_active_account}"
)

print("\n--- Final Invoice Summary ---")
print(invoice_summary)