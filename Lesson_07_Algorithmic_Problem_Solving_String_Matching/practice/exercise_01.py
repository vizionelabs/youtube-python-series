# ==============================================================================
# LESSON 07: ALGORITHMIC PROBLEM SOLVING, STRING MATCHING, STATE TRACKING
# FILE: practice/exercise_01.py
# DESCRIPTION: Core language fundamentals covering string parsing, sequence
#              matching algorithms, and explicit state tracking flags.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. STRING MATCHING FUNDAMENTALS
# ------------------------------------------------------------------------------
# In Python, string matching involves identifying specific sub-sequences or
# characters within larger string datasets.

log_entry = "2026-09-10 10:15:22 [AUDIT_WARN] Transaction TXN_9081 flags pending review."

# Simple Membership Testing (The 'in' operator performs pattern matching under the hood)
has_warning = "[AUDIT_WARN]" in log_entry
print(f"Contains warning flag: {has_warning}")

# Prefix and Suffix Validation
is_formatted_log = log_entry.startswith("2026")
is_flagged = log_entry.endswith("review.")
print(f"Valid log timestamp prefix: {is_formatted_log}")
print(f"Valid end sentinel: {is_flagged}")

# Position Extraction via Indexing and Finding
warning_index = log_entry.find("[AUDIT_WARN]")
print(f"Warning tag found at string character index: {warning_index}")


# ------------------------------------------------------------------------------
# 2. STATE TRACKING MACHINES (FLAG-BASED STATE CONTROL)
# ------------------------------------------------------------------------------
# Algorithmic problem solving often requires tracking changing states as we
# iterate through sequential data structures.

raw_stream = [
    "LOG_START",
    "TXN_001: 150.00: APPROVED",
    "TXN_002: -50.00: REJECTED",
    "TXN_003: 1200.00: SUSPICIOUS",
    "LOG_END",
    "TXN_004: 80.00: APPROVED" # Should be ignored because state is inactive
]

# State Variables
is_processing_active = False  # Boolean flag tracking state transition
total_flagged_amount = 0.0
flagged_count = 0

# Iteration with Conditional State Mutation
for line in raw_stream:
    # State Transition 1: Activate Processing
    if line == "LOG_START":
        is_processing_active = True
        print(">>> Audit Stream Ingestion Activated <<<")
        continue  # Skip to next item in loop

    # State Transition 2: Deactivate Processing
    if line == "LOG_END":
        is_processing_active = False
        print(">>> Audit Stream Ingestion Deactivated <<<")
        break  # Terminate processing stream

    # Algorithmic Logic Guarded by State Flag
    if is_processing_active:
        # String Decomposition (Splitting by delimiter)
        parts = line.split(": ")
        txn_id = parts[0]
        amount = float(parts[1])
        status = parts[2]

        # String Matching Logic for Flagged States
        if status == "SUSPICIOUS" or amount > 1000.0:
            print(f"ALERT: State Engine Flagged Record -> {txn_id} (${amount:.2f})")
            total_flagged_amount += amount
            flagged_count += 1

print("\n--- STATE SUMMARY ---")
print(f"Total Suspicious Amount Flagged: ${total_flagged_amount:.2f}")
print(f"Total Suspicious Items Tracked: {flagged_count}")


# ------------------------------------------------------------------------------
# 3. ALGORITHMIC PATTERN MATCHING (SUBSTRING SCANNING)
# ------------------------------------------------------------------------------
# Scans a text list for specific target tokens using manual iteration logic.

records = ["REF_901_PAID", "REF_902_PENDING", "REF_903_REFUNDED", "REF_904_PAID"]
search_pattern = "PAID"
matched_records = []

for record in records:
    # Substring search algorithm
    if search_pattern in record:
        matched_records.append(record)

print(f"\nPattern '{search_pattern}' matched records: {matched_records}")