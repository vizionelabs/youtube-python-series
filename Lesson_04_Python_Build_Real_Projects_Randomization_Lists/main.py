# ==============================================================================
# VIZIONE LABS - PRODUCTION LEAD ALLOCATION ENGINE
# Module: main.py
# Purpose: Enterprise CRM Lead Distribution & Queue Management System
# ==============================================================================

import random
from typing import List, Dict, Any, Optional


def allocate_lead(
        lead_name: str,
        lead_value: float,
        available_executives: List[str]
) -> Dict[str, Any]:
    """
    Randomly assigns an inbound lead to an available Account Executive.

    Args:
        lead_name: The company or contact name for the lead.
        lead_value: Estimated contract value in USD.
        available_executives: List of Account Executive names currently active.

    Returns:
        Dict containing routing status, assigned executive, and payload details.
    """
    if not available_executives:
        return {
            "status": "UNASSIGNED",
            "lead_name": lead_name,
            "lead_value": lead_value,
            "assigned_to": None,
            "reason": "Queue empty: No active Account Executives available."
        }

    # Safe random selection using random.choice
    assigned_exec: str = random.choice(available_executives)

    return {
        "status": "ASSIGNED",
        "lead_name": lead_name,
        "lead_value": lead_value,
        "assigned_to": assigned_exec,
        "reason": "Successfully routed via random round-robin allocation."
    }


def process_batch_queue(
        lead_queue: List[Dict[str, Any]],
        executives: List[str]
) -> List[Dict[str, Any]]:
    """
    Processes an incoming lead queue and safely mutates internal records.

    Args:
        lead_queue: List of lead dictionaries to be routed.
        executives: List of available Account Executives.

    Returns:
        List of processed allocation results.
    """
    processed_records: List[Dict[str, Any]] = []

    # Iterate through the list while managing boundaries safely
    for lead in lead_queue:
        result = allocate_lead(
            lead_name=lead.get("name", "Unknown Lead"),
            lead_value=lead.get("value", 0.0),
            available_executives=executives
        )
        processed_records.append(result)

    return processed_records


def main() -> None:
    print("==========================================================")
    print("VIZIONE LABS: ENTERPRISE CRM LEAD DISTRIBUTION ENGINE")
    print("==========================================================\n")

    # Active sales team roster
    account_executives: List[str] = [
        "Alexander Wright",
        "Elena Rostova",
        "Marcus Vance",
        "Sophia Chen"
    ]

    # Inbound dynamic lead queue
    incoming_leads: List[Dict[str, Any]] = [
        {"name": "Apex Cloud Systems", "value": 45000.00},
        {"name": "Nexus Financial Technologies", "value": 120000.00},
        {"name": "Quantum AI Infrastructure", "value": 85000.00},
        {"name": "Vortex Media Group", "value": 30000.00}
    ]

    print(f"Active Account Executives ({len(account_executives)}): {account_executives}")
    print(f"Incoming Leads to Process: {len(incoming_leads)}\n")

    # Execute dynamic allocation pipeline
    allocation_results = process_batch_queue(incoming_leads, account_executives)

    # Display processing ledger
    print("--- LEAD ROUTING EXECUTION LOG ---")
    for index, record in enumerate(allocation_results):
        # Safe array index display
        print(f"Record [{index + 1}/{len(allocation_results)}]")
        print(f"  Lead Name   : {record['lead_name']}")
        print(f"  Value       : ${record['lead_value']:,.2f}")
        print(f"  Assigned To : {record['assigned_to']}")
        print(f"  Status      : {record['status']}")
        print(f"  Log Reason  : {record['reason']}\n")

    # Edge Case Simulation: Attempting access on empty roster to test boundary safety
    print("--- SIMULATING EMPTY QUEUE EDGE CASE ---")
    empty_executives: List[str] = []
    fallback_result = allocate_lead("Unbound Systems Inc", 15000.00, empty_executives)
    print(f"Fallback Assignment Status: {fallback_result['status']}")
    print(f"Fallback Reason           : {fallback_result['reason']}")


if __name__ == "__main__":
    main()