# ==============================================================================
# Vizione Labs — Enterprise Automation Engine
# Track A: Python Automation & Scripting (Lesson 12)
# File: main.py
# System: Role-Based Access Control (RBAC) & Audit Engine
# ==============================================================================

import time

# Global Application State & Configuration Flags
SYSTEM_NAME = "Vizione Enterprise Security Engine"
MAX_LOGIN_ATTEMPTS = 3
global_audit_log = []
active_user_sessions = 0


def log_audit_event(event_type, details):
    """
    Appends an audit entry to the global audit log safely.
    Uses pure return patterns where applicable or clear global mutation boundaries.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"[{timestamp}] [{event_type}] {details}"
    global_audit_log.append(formatted_entry)


def authenticate_user(username, secret_key):
    """
    Authenticates user and returns session state.
    Demonstrates local scope isolation: variables created here do NOT leak globally.
    """
    # Local scope isolation variables
    valid_credentials = {
        "admin_lucas": "SecuredPass2026!",
        "engineer_dev": "CloudTech99#"
    }

    is_authenticated = False
    access_level = "GUEST"

    if username in valid_credentials and valid_credentials[username] == secret_key:
        is_authenticated = True
        access_level = "ADMINISTRATOR" if "admin" in username else "OPERATOR"
        log_audit_event("AUTH_SUCCESS", f"User '{username}' authenticated as {access_level}.")
    else:
        log_audit_event("AUTH_FAILURE", f"Invalid login attempt for username '{username}'.")

    # Local scoped variables stay localized inside the function
    return {
        "user": username,
        "authenticated": is_authenticated,
        "access_level": access_level
    }


def process_user_session(session_data):
    """
    Simulates session processing and demonstrates block scope behavior in Python.
    """
    global active_user_sessions

    if session_data["authenticated"]:
        active_user_sessions += 1
        # Variable initialized inside an IF block (demonstrating block scope behavior in Python)
        session_token = f"TOKEN-{hash(session_data['user']) & 0xFFFFFF}"
        status_message = f"Session initialized successfully. Active Token: {session_token}"
    else:
        status_message = "Access Denied: Session initialization aborted."

    # In Python, status_message is accessible outside the IF block because IF blocks do not create scope
    print(f"[SESSION MANAGER] {status_message}")
    return session_data["authenticated"]


def terminate_session(user_name):
    """
    Decrements global active user count cleanly using explicit global declaration.
    """
    global active_user_sessions
    if active_user_sessions > 0:
        active_user_sessions -= 1
        log_audit_event("SESSION_TERMINATED", f"Session ended for user: {user_name}")


def main():
    """
    Application execution entry point.
    """
    print(f"=== {SYSTEM_NAME} ===")
    print(f"Initial Active Sessions: {active_user_sessions}\n")

    # Attempt 1: Failed Login
    print("--- Executing Test Case 1: Failed Authentication ---")
    user1_auth = authenticate_user("unknown_user", "wrong_pass")
    process_user_session(user1_auth)
    print(f"Active Sessions: {active_user_sessions}\n")

    # Attempt 2: Successful Admin Login
    print("--- Executing Test Case 2: Authorized Admin Authentication ---")
    user2_auth = authenticate_user("admin_lucas", "SecuredPass2026!")
    if process_user_session(user2_auth):
        print(f"Granted Access Level: {user2_auth['access_level']}")
    print(f"Active Sessions: {active_user_sessions}\n")

    # Terminating Active Session
    print("--- Executing Session Cleanup ---")
    terminate_session("admin_lucas")
    print(f"Final Active Sessions: {active_user_sessions}\n")

    # Printing System Audit Logs
    print("=== SYSTEM AUDIT LOG REPOSITORY ===")
    for entry in global_audit_log:
        print(entry)


if __name__ == "__main__":
    main()