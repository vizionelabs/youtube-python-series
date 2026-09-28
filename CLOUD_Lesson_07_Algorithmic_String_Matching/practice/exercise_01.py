# ==============================================================================
# Vizione Labs — Track A: Python: Build Real Projects
# Lesson 07: Algorithmic Problem Solving, String Matching, State Tracking
# Script: practice/exercise_01.py
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: STRING NORMALIZATION & EXACT MATCHING
# ------------------------------------------------------------------------------
# Define raw user query input and standardized system target string
user_input_query = "   VIZIONE-LABS-CORE-SERVICE   "
system_target_pattern = "vizione-labs-core-service"

# Clean leading/trailing whitespaces and normalize casing to lowercase
normalized_query = user_input_query.strip().lower()

# Exact full-string matching evaluation
is_exact_match = normalized_query == system_target_pattern

print("--- Section 1: String Normalization & Exact Matching ---")
print(f"Raw Input         : '{user_input_query}'")
print(f"Normalized Input  : '{normalized_query}'")
print(f"Target Pattern    : '{system_target_pattern}'")
print(f"Is Exact Match    : {is_exact_match}\n")

# ------------------------------------------------------------------------------
# SECTION 2: SUBSTRING MATCHING & CHARACTER COUNTS
# ------------------------------------------------------------------------------
# Dynamic search pattern inspection inside a system error log message
system_log_message = "ERR_404: API endpoint /api/v1/auth not found. Retry status: ERR_404."
target_sub_string = "ERR_404"

# Check substring occurrence using conditional 'in' operator
contains_error = target_sub_string in system_log_message

# Count total occurrences of the sub-string within the text block
error_count = system_log_message.count(target_sub_string)

print("--- Section 2: Substring Matching & Counting ---")
print(f"Log Message       : {system_log_message}")
print(f"Target Substring  : '{target_sub_string}'")
print(f"Contains Substring: {contains_error}")
print(f"Occurrence Count  : {error_count}\n")

# ------------------------------------------------------------------------------
# SECTION 3: STATE TRACKING & ITERATIVE PATTERN MATCHING
# ------------------------------------------------------------------------------
# Simulated list of incoming security request payloads
payload_stream = [
    "SEC_VAL_AUTH_PASS",
    "SEC_ERR_TOKEN_EXPIRED",
    "SEC_VAL_DATA_FETCH",
    "SEC_ERR_INVALID_HEADER",
    "SEC_VAL_LOGOUT"
]

# State tracking variables
successful_matches = 0
failed_matches = 0
total_inspected = 0

# Prefix target pattern for error detection
error_prefix = "SEC_ERR"

print("--- Section 3: State Tracking & Iterative Pattern Matching ---")
# Iterate over payload stream to track matching state
for payload in payload_stream:
    total_inspected += 1

    # Prefix string matching check using startswith()
    if payload.startswith(error_prefix):
        failed_matches += 1
        print(f"[{total_inspected}] ERROR DETECTED -> {payload}")
    else:
        successful_matches += 1
        print(f"[{total_inspected}] VALID PAYLOAD  -> {payload}")

# Final State Summary Report
print("\n--- Execution State Summary ---")
print(f"Total Payloads Processed : {total_inspected}")
print(f"Total Successful Matches : {successful_matches}")
print(f"Total Pattern Failures   : {failed_matches}")