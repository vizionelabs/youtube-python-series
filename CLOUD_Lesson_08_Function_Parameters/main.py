# main.py
# ==============================================================================
# VIZIONE LABS — ENTERPRISE CLIENT DISPATCH SYSTEM
# Lesson 08: Function Parameters, Keyword Arguments & Positional Input Mapping
# File: main.py
# ==============================================================================

import datetime


def dispatch_client_notification(
        client_id,
        project_ref,
        message_body,
        channel="EMAIL",
        priority="NORMAL",
        require_ack=False
):
    """
    Constructs and dispatches a client notification payload with mandatory identification
    and configurable routing controls.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format high-priority or acknowledgment-required tags
    ack_tag = "[ACK_REQUIRED]" if require_ack else "[NO_ACK]"
    status_header = f"[{priority.upper()}][{channel.upper()}]{ack_tag}"

    payload = {
        "timestamp": timestamp,
        "client_id": client_id,
        "project_ref": project_ref,
        "routing": status_header,
        "content": message_body,
        "status": "DISPATCHED"
    }

    return payload


def format_audit_log(timestamp, event_type, details, severity="INFO"):
    """
    Formats a single line audit log entry using explicit parameter ordering.
    """
    return f"[{timestamp}] [{severity.upper()}] {event_type.upper()}: {details}"


def execute_notification_pipeline():
    """
    Main orchestration function running client notification scenarios.
    """
    print("==================================================================")
    print("       VIZIONE LABS — ENTERPRISE DISPATCH ENGINE (LESSON 08)       ")
    print("==================================================================\n")

    # Scenario 1: Standard Positional Parameters (Mandatory Inputs)
    # Ordering matters: client_id, project_ref, message_body
    print("--- SCENARIO 1: Standard Positional Dispatch ---")
    notice_01 = dispatch_client_notification(
        "CLI-9042",
        "PRJ-VIZ-2026-08",
        "Weekly automated project metrics report is ready for download."
    )
    print(f"Header: {notice_01['routing']}")
    print(f"Target: Client {notice_01['client_id']} | Project: {notice_01['project_ref']}")
    print(f"Body: {notice_01['content']}\n")

    # Scenario 2: Keyword Parameter Overrides for Specific Alerting
    print("--- SCENARIO 2: Urgent SMS Alerting via Keyword Overrides ---")
    notice_02 = dispatch_client_notification(
        client_id="CLI-1108",
        project_ref="PRJ-SAAS-PROD",
        message_body="CRITICAL: API key quota reached 95%. Immediate action required.",
        channel="SMS",
        priority="HIGH",
        require_ack=True
    )
    print(f"Header: {notice_02['routing']}")
    print(f"Target: Client {notice_02['client_id']} | Project: {notice_02['project_ref']}")
    print(f"Body: {notice_02['content']}\n")

    # Scenario 3: Mixed Invocation (Positional Base + Keyword Optional Controls)
    print("--- SCENARIO 3: Webhook Alert Dispatch (Mixed Arguments) ---")
    notice_03 = dispatch_client_notification(
        "CLI-3301",
        "PRJ-CLOUD-MIGRATE",
        "Database backup completed successfully.",
        require_ack=False,
        channel="WEBHOOK"
    )
    print(f"Header: {notice_03['routing']}")
    print(f"Target: Client {notice_03['client_id']} | Project: {notice_03['project_ref']}")
    print(f"Body: {notice_03['content']}\n")

    # Scenario 4: Dynamic Audit Log Formatting
    print("--- SCENARIO 4: Enterprise Audit Logging ---")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Passing arguments using keyword matching to enforce transparency
    log_entry = format_audit_log(
        timestamp=current_time,
        event_type="DISPATCH_BATCH",
        details="3 notifications successfully processed through Vizione Engine.",
        severity="SUCCESS"
    )
    print(log_entry)
    print("\n==================================================================")


if __name__ == "__main__":
    execute_notification_pipeline()