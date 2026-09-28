# ==============================================================================
# Vizione Labs — Track A: Python: Build Real Projects
# Lesson 07: Algorithmic Problem Solving, String Matching, State Tracking
# Script: main.py
# ==============================================================================

# Enterprise System Log Payload Stream
system_log_stream = [
    "  [2026-09-28 10:00:15] [INFO] Auth service started successfully. ",
    "  [2026-09-28 10:00:18] [WARNING] Rate limit threshold reached for IP: 192.168.1.45. ",
    "  [2026-09-28 10:01:02] [ERROR] SEC_ERR_401: Unauthorized access attempt detected on /api/v1/vault. ",
    "  [2026-09-28 10:02:11] [INFO] Database connection re-established. ",
    "  [2026-09-28 10:03:45] [ERROR] SEC_ERR_500: Internal server timeout during data serialization. ",
    "  [2026-09-28 10:04:12] [CRITICAL] SEC_ERR_401: Repeated invalid token submitted by client. "
]

# State Tracking Indicators & Metrics
total_logs_processed = 0
info_count = 0
warning_count = 0
error_count = 0
critical_security_flags = 0

# Target Patterns for Algorithmic Detection
error_indicator = "[ERROR]"
security_threat_code = "SEC_ERR_401"

print("==================================================================")
print("       VIZIONE LABS — ENTERPRISE LOG AUDIT & SECURITY ENGINE      ")
print("==================================================================\n")

# Process Log Stream Iteratively
for raw_log_entry in system_log_stream:
    # 1. Normalization & Cleaning
    cleaned_log = raw_log_entry.strip()
    total_logs_processed += 1

    # 2. String Pattern Detection & State Metrics Increment
    if "[INFO]" in cleaned_log:
        info_count += 1
        status_tag = "INFO"
    elif "[WARNING]" in cleaned_log:
        warning_count += 1
        status_tag = "WARN"
    elif error_indicator in cleaned_log:
        error_count += 1
        status_tag = "FAIL"
    else:
        status_tag = "UNKN"

    # 3. Specific Security Threat Pattern Matching (Substring Check)
    has_security_breach = security_threat_code in cleaned_log
    if has_security_breach:
        critical_security_flags += 1
        flag_status = " [ALERT: UNAUTHORIZED ACCESS DETECTED]"
    else:
        flag_status = ""

    # Output Processed Record Summary
    print(f"[{status_tag}] Log #{total_logs_processed:02d}: {cleaned_log}{flag_status}")

# Final State Summary Report
print("\n==================================================================")
print("                     AUDIT & METRICS SUMMARY                      ")
print("==================================================================")
print(f" Total Log Entries Processed    : {total_logs_processed}")
print(f" Total Info Logs                : {info_count}")
print(f" Total Warning Logs             : {warning_count}")
print(f" Total Error Logs               : {error_count}")
print(f" Critical Security Alerts (401) : {critical_security_flags}")
print("==================================================================")