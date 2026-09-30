"""
Vizione Labs - Track A: Python: Build Real Projects
Lesson 11: Local vs. Global Scope, Constants, Namespace Management, Global Mutations
File: main.py

Enterprise Application:
Vizione Labs Cloud Infrastructure & Session Billing Engine

Purpose:
Demonstrates production-grade scope segregation, constant definitions, namespace isolation,
and safe state management patterns for enterprise user session tracking and cloud billing.
"""

# ==============================================================================
# GLOBAL CONSTANTS & CONFIGURATION (SCREAMING_SNAKE_CASE)
# ==============================================================================
# Module-level constants defined globally for cross-system availability.
DEFAULT_HOURLY_RATE = 45.00
PLATFORM_TAX_RATE = 0.12
MAX_CONCURRENT_SESSIONS = 5
SYSTEM_ENVIRONMENT = "PRODUCTION"

# ==============================================================================
# GLOBAL APPLICATION STATE (MODULE COURTYARD)
# ==============================================================================
# Global state variables tracking runtime platform statistics.
total_active_sessions = 0
total_platform_revenue = 0.0


# ==============================================================================
# CORE SYSTEM FUNCTIONS
# ==============================================================================
def initialize_user_session(client_id, hours_allocated, active_sessions, platform_revenue):
    """
    Initializes a new cloud computing session for a client.

    Demonstrates the Pure Return Pattern for State Management:
    Instead of mutating global variables directly inside this function, it receives
    current system state as parameters, computes local math, and returns updated metrics.

    Returns:
        tuple: (session_data_dict, updated_active_sessions, updated_platform_revenue)
    """
    # Safety Guard: Check platform capacity limits using the passed state parameter
    if active_sessions >= MAX_CONCURRENT_SESSIONS:
        print(f"[WARN] Session initialization rejected for '{client_id}': Capacity Limit Reached.")
        return None, active_sessions, platform_revenue

    # Local scope variable calculations
    subtotal = hours_allocated * DEFAULT_HOURLY_RATE
    tax_amount = subtotal * PLATFORM_TAX_RATE
    total_cost = subtotal + tax_amount

    # Pure State Calculation (Local Scope)
    updated_sessions = active_sessions + 1
    updated_revenue = platform_revenue + total_cost

    session_data = {
        "client_id": client_id,
        "hours": hours_allocated,
        "subtotal": subtotal,
        "tax": tax_amount,
        "total_cost": total_cost,
        "status": "ACTIVE"
    }

    print(f"[SUCCESS] Session initialized for client '{client_id}'. Cost: ${total_cost:.2f}")
    return session_data, updated_sessions, updated_revenue


def terminate_user_session(session_data, active_sessions):
    """
    Terminates an active session and decrements the session count safely.
    Uses input arguments and explicit returns instead of hidden global mutations.

    Returns:
        tuple: (updated_session_data_dict, updated_active_sessions)
    """
    if session_data and session_data.get("status") == "ACTIVE":
        session_data["status"] = "TERMINATED"
        updated_sessions = active_sessions - 1
        client_id = session_data["client_id"]
        print(f"[TERMINATED] Session closed for client '{client_id}'. Active sessions remaining: {updated_sessions}")
        return session_data, updated_sessions
    else:
        print("[ERROR] Invalid or already terminated session provided.")
        return session_data, active_sessions


def generate_system_audit_report():
    """
    Generates a system status audit report by reading global variables
    without modifying them. Demonstrates read-only access to global scope.
    """
    print("\n" + "=" * 60)
    print("VIZIONE LABS CLOUD INFRASTRUCTURE AUDIT REPORT")
    print("=" * 60)
    print(f" Environment              : {SYSTEM_ENVIRONMENT}")
    print(f" Default Hourly Compute   : ${DEFAULT_HOURLY_RATE:.2f}/hr")
    print(f" Platform Tax Rate        : {PLATFORM_TAX_RATE * 100:.1f}%")
    print(f" Active Sessions          : {total_active_sessions}/{MAX_CONCURRENT_SESSIONS}")
    print(f" Total Platform Revenue   : ${total_platform_revenue:.2f}")
    print("=" * 60 + "\n")


# ==============================================================================
# MAIN PRODUCTION EXECUTION FLOW
# ==============================================================================
if __name__ == "__main__":
    print("=== STARTING VIZIONE LABS INFRASTRUCTURE ENGINE ===\n")

    # Display initial state
    generate_system_audit_report()

    # Simulating client session registrations using explicit state re-assignment
    s1, total_active_sessions, total_platform_revenue = initialize_user_session(
        client_id="Client_Alpha",
        hours_allocated=10,
        active_sessions=total_active_sessions,
        platform_revenue=total_platform_revenue
    )

    s2, total_active_sessions, total_platform_revenue = initialize_user_session(
        client_id="Client_Beta",
        hours_allocated=25,
        active_sessions=total_active_sessions,
        platform_revenue=total_platform_revenue
    )

    s3, total_active_sessions, total_platform_revenue = initialize_user_session(
        client_id="Client_Gamma",
        hours_allocated=5,
        active_sessions=total_active_sessions,
        platform_revenue=total_platform_revenue
    )

    # Display state post-initialization
    generate_system_audit_report()

    # Terminating a session with explicit state re-assignment
    if s1:
        s1, total_active_sessions = terminate_user_session(s1, total_active_sessions)

    # Display final state
    generate_system_audit_report()

    print("=== ENGINE EXECUTION COMPLETED SUCCESSFULLY ===")