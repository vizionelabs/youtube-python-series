# main.py
# Vizione Labs — Python: Build Real Projects (Lesson 03)
# Topic: Enterprise Access Control & Automated System Audit Engine

import datetime


def evaluate_access_request(user_profile: dict, resource_request: dict) -> dict:
    """Evaluates an inbound system access request against security policies,

    user clearance, multi-factor authentication status, and risk metrics.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Extract user metadata
    user_id = user_profile.get("user_id", "UNKNOWN")
    role = user_profile.get("role", "guest")
    is_active = user_profile.get("is_active", False)
    mfa_enabled = user_profile.get("mfa_enabled", False)
    account_locked = user_profile.get("account_locked", True)
    failed_attempts = user_profile.get("failed_attempts", 0)

    # Extract resource metadata
    target_resource = resource_request.get("target_resource", "public_portal")
    required_clearance = resource_request.get("required_clearance", 1)
    is_production = resource_request.get("is_production", False)

    # Initial decision state tracking
    status = "DENIED"
    reason = "Undetermined evaluation error."
    risk_level = "LOW"

    # Rule 1: Account Health & Suspension Checks (Comparison & Logical Operators)
    if account_locked or not is_active:
        reason = "Account is either inactive or locked due to policy violation."
        risk_level = "HIGH"
    elif failed_attempts >= 5:
        reason = "Too many failed login attempts. Suspicious activity flagged."
        risk_level = "CRITICAL"
    else:
        # Rule 2: Production System Security Check (Nested Logic)
        if is_production:
            if not mfa_enabled:
                reason = "Multi-Factor Authentication (MFA) is strictly required for production environments."
                risk_level = "MEDIUM"
            elif role == "admin":
                status = "GRANTED"
                reason = "Full Administrative access to production authorized."
                risk_level = "LOW"
            elif role == "engineer" and required_clearance <= 2:
                status = "GRANTED"
                reason = "Engineering production deployment access authorized."
                risk_level = "LOW"
            else:
                reason = f"Insufficient role privileges for role '{role}' on production resource."
                risk_level = "MEDIUM"
        else:
            # Non-production resource access evaluation
            if role in ["admin", "engineer", "analyst"]:
                status = "GRANTED"
                reason = "Staging/Internal resource access authorized."
                risk_level = "LOW"
            else:
                reason = "Role lacks standard internal system access permissions."
                risk_level = "LOW"

    # Audit payload compilation
    audit_log = {
        "timestamp": timestamp,
        "user_id": user_id,
        "resource": target_resource,
        "decision": status,
        "reason": reason,
        "risk_level": risk_level,
    }

    return audit_log


def run_system_audit_demo():
    """Runs automated simulation scenarios through the evaluation engine."""
    print("==================================================================")
    print("      VIZIONE LABS: ENTERPRISE ACCESS CONTROL ENGINE (v3.0)       ")
    print("==================================================================")

    # Test Scenario 1: Active Engineer requesting Staging Database
    user_01 = {
        "user_id": "USR-8021",
        "role": "engineer",
        "is_active": True,
        "mfa_enabled": True,
        "account_locked": False,
        "failed_attempts": 0,
    }
    request_01 = {
        "target_resource": "staging_db",
        "required_clearance": 1,
        "is_production": False,
    }

    # Test Scenario 2: Active Engineer without MFA requesting Production Core
    user_02 = {
        "user_id": "USR-4092",
        "role": "engineer",
        "is_active": True,
        "mfa_enabled": False,
        "account_locked": False,
        "failed_attempts": 1,
    }
    request_02 = {
        "target_resource": "prod_payment_gateway",
        "required_clearance": 3,
        "is_production": True,
    }

    # Test Scenario 3: Suspicious User with high failed attempts
    user_03 = {
        "user_id": "USR-1002",
        "role": "admin",
        "is_active": True,
        "mfa_enabled": True,
        "account_locked": False,
        "failed_attempts": 6,
    }
    request_03 = {
        "target_resource": "prod_server_cluster",
        "required_clearance": 3,
        "is_production": True,
    }

    scenarios = [
        ("Scenario 1: Standard Staging Access", user_01, request_01),
        ("Scenario 2: Missing MFA on Production Request", user_02, request_02),
        ("Scenario 3: Excessive Failed Login Attempts", user_03, request_03),
    ]

    for title, user, request in scenarios:
        print(f"\n--- [EVALUATING] {title} ---")
        audit_result = evaluate_access_request(user, request)
        print(f" Timestamp  : {audit_result['timestamp']}")
        print(f" User ID    : {audit_result['user_id']}")
        print(f" Resource   : {audit_result['resource']}")
        print(f" Decision   : {audit_result['decision']}")
        print(f" Reason     : {audit_result['reason']}")
        print(f" Risk Level : {audit_result['risk_level']}")

    print("\n==================================================================")
    print("               AUDIT EVALUATION COMPLETE [OK]                     ")
    print("==================================================================")


if __name__ == "__main__":
    run_system_audit_demo()