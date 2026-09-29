# main.py

# ==============================================================================
# VIZIONE LABS — SAAS CLIENT DIRECTORY & SUBSCRIPTION SERVICE ENGINE
# Lesson 09: Dictionaries, Nested Data Structures, Key-Value Manipulation
# Track A: Python: Build Real Projects
# ==============================================================================

from typing import Dict, Any, List, Optional
import datetime

# ------------------------------------------------------------------------------
# GLOBAL ENTERPRISE STATE: CLIENT DATABASE & SERVICE REGISTRY
# ------------------------------------------------------------------------------
# Core nested data structure mapping unique enterprise Client IDs to client profiles.
CLIENT_DIRECTORY: Dict[str, Dict[str, Any]] = {
    "CLI-1001": {
        "company_name": "Apex Cybernetics",
        "primary_contact": {
            "name": "Sarah Connor",
            "email": "s.connor@apexcyber.io"
        },
        "subscription_tier": "ENTERPRISE",
        "active_status": True,
        "resource_limits": {
            "api_calls_monthly": 1000000,
            "allocated_storage_gb": 500
        },
        "usage_metrics": {
            "api_calls_used": 745000,
            "storage_used_gb": 320.5
        },
        "billing_history": [
            {"invoice_id": "INV-2026-001", "amount": 1250.00, "paid": True},
            {"invoice_id": "INV-2026-042", "amount": 1250.00, "paid": True}
        ]
    },
    "CLI-1002": {
        "company_name": "Starlight Analytics",
        "primary_contact": {
            "name": "Marcus Vance",
            "email": "m.vance@starlight.tech"
        },
        "subscription_tier": "PRO",
        "active_status": True,
        "resource_limits": {
            "api_calls_monthly": 250000,
            "allocated_storage_gb": 100
        },
        "usage_metrics": {
            "api_calls_used": 248900,
            "storage_used_gb": 98.2
        },
        "billing_history": [
            {"invoice_id": "INV-2026-015", "amount": 450.00, "paid": True}
        ]
    }
}


# ------------------------------------------------------------------------------
# CORE ENGINE FUNCTIONS: DICTIONARY MUTATIONS & LOOKUPS
# ------------------------------------------------------------------------------

def register_new_client(
        client_id: str,
        company_name: str,
        contact_name: str,
        contact_email: str,
        subscription_tier: str = "STARTER"
) -> Dict[str, Any]:
    """
    Onboards a new client entry directly into the global client directory structure.
    Demonstrates key assignment and dictionary schema initialization.
    """
    tier_limits = {
        "STARTER": {"api_calls_monthly": 50000, "allocated_storage_gb": 20},
        "PRO": {"api_calls_monthly": 250000, "allocated_storage_gb": 100},
        "ENTERPRISE": {"api_calls_monthly": 1000000, "allocated_storage_gb": 500}
    }

    # Default to STARTER allocation if invalid tier provided using safe dict lookup
    limits = tier_limits.get(subscription_tier.upper(), tier_limits["STARTER"])

    new_profile: Dict[str, Any] = {
        "company_name": company_name,
        "primary_contact": {
            "name": contact_name,
            "email": contact_email
        },
        "subscription_tier": subscription_tier.upper(),
        "active_status": True,
        "resource_limits": limits,
        "usage_metrics": {
            "api_calls_used": 0,
            "storage_used_gb": 0.0
        },
        "billing_history": []
    }

    # Mutate top-level directory dictionary by adding the new key-value pair
    CLIENT_DIRECTORY[client_id] = new_profile
    return new_profile


def update_resource_usage(client_id: str, api_calls_delta: int, storage_delta_gb: float) -> bool:
    """
    Safely mutates nested usage metrics inside a target client record.
    Returns True if update was successful, False if client ID is non-existent.
    """
    client = CLIENT_DIRECTORY.get(client_id)
    if not client:
        print(f"[ERROR] Client ID '{client_id}' non-existent in directory.")
        return False

    # Access nested dictionary values and mutate directly
    client["usage_metrics"]["api_calls_used"] += api_calls_delta
    client["usage_metrics"]["storage_used_gb"] += storage_delta_gb
    return True


def \
        evaluate_quota_overflow(client_id: str) -> Dict[str, Any]:
    """
    Evaluates client usage against resource limits. Demonstrates multi-level
    nested dictionary access and safe condition verification.
    """
    client = CLIENT_DIRECTORY.get(client_id)
    if not client:
        return {"error": "Client not found"}

    limits = client.get("resource_limits", {})
    usage = client.get("usage_metrics", {})

    api_limit = limits.get("api_calls_monthly", 0)
    api_used = usage.get("api_calls_used", 0)
    storage_limit = limits.get("allocated_storage_gb", 0)
    storage_used = usage.get("storage_used_gb", 0.0)

    api_pct = (api_used / api_limit * 100) if api_limit > 0 else 0.0
    storage_pct = (storage_used / storage_limit * 100) if storage_limit > 0 else 0.0

    return {
        "client_id": client_id,
        "company_name": client.get("company_name", "Unknown"),
        "api_usage_percent": round(api_pct, 2),
        "api_overflow_flag": api_used >= api_limit,
        "storage_usage_percent": round(storage_pct, 2),
        "storage_overflow_flag": storage_used >= storage_limit
    }


def generate_directory_audit_report() -> None:
    """
    Iterates through the entire nested client dictionary structure (.items())
    to produce a formatted management audit report.
    """
    print("\n" + "=" * 80)
    print(f"VIZIONE LABS SAAS CLIENT DIRECTORY AUDIT REPORT | {datetime.date.today()}")
    print("=" * 80)

    for client_id, profile in CLIENT_DIRECTORY.items():
        company = profile["company_name"]
        tier = profile["subscription_tier"]
        status = "ACTIVE" if profile["active_status"] else "SUSPENDED"
        contact_email = profile["primary_contact"]["email"]

        usage = profile["usage_metrics"]
        limits = profile["resource_limits"]

        print(f"\n[CLIENT RECORD]: {client_id} - {company.upper()}")
        print(f"  ├─ Status / Tier  : {status} | Tier: {tier}")
        print(f"  ├─ Contact Email  : {contact_email}")
        print(f"  ├─ API Calls      : {usage['api_calls_used']:,} / {limits['api_calls_monthly']:,}")
        print(f"  └─ Storage Load   : {usage['storage_used_gb']:.1f} GB / {limits['allocated_storage_gb']} GB")

    print("=" * 80 + "\n")


# ------------------------------------------------------------------------------
# SYSTEM EXECUTION & VERIFICATION PIPELINE
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Initializing Vizione Labs Client Directory Engine...")

    # 1. Onboard a new enterprise client profile into the directory
    register_new_client(
        client_id="CLI-1003",
        company_name="Aura Dynamics",
        contact_name="Elena Rostova",
        contact_email="e.rostova@auradynamics.com",
        subscription_tier="STARTER"
    )

    # 2. Simulate daily telemetry/usage updates across nested records
    update_resource_usage(client_id="CLI-1002", api_calls_delta=2000, storage_delta_gb=3.5)
    update_resource_usage(client_id="CLI-1003", api_calls_delta=48500, storage_delta_gb=18.2)

    # 3. Evaluate resource overflow warnings for high-usage clients
    starlight_eval = evaluate_quota_overflow("CLI-1002")
    print(
        f"\nQuota Evaluation [CLI-1002]: API Limit Reached = {starlight_eval['api_overflow_flag']} ({starlight_eval['api_usage_percent']}%)")

    aura_eval = evaluate_quota_overflow("CLI-1003")
    print(
        f"Quota Evaluation [CLI-1003]: API Limit Reached = {aura_eval['api_overflow_flag']} ({aura_eval['api_usage_percent']}%)")

    # 4. Perform an administrative status report across all nested client keys
    generate_directory_audit_report()