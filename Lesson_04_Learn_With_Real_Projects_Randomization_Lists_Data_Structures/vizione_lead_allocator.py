# ==============================================================================
# LESSON 04: REAL-WORLD PRODUCTION SYSTEM
# Brand: Vizione Labs | Track A: Core Fundamentals & Scripting
# File: vizione_lead_allocator.py
# Description: Automated Client Lead Distribution Engine
# ==============================================================================

import random
from typing import List, Dict, Any


def get_active_account_executives() -> List[str]:
    """
    Simulates fetching current active sales and technical account managers.
    """
    return [
        "Lucas (Lead Architect)",
        "Sarah (Senior Full-Stack Engineer)",
        "Alex (Backend Specialist)",
        "Elena (Client Success Lead)",
        "David (DevOps Engineer)"
    ]


def process_incoming_leads() -> List[Dict[str, Any]]:
    """
    Simulates incoming project inquiries queued for allocation.
    """
    return [
        {
            "lead_id": "VIZ-2026-001",
            "client_name": "Apex Enterprise Solutions",
            "project_type": "Full-Stack SaaS Platform",
            "budget_usd": 15000
        },
        {
            "lead_id": "VIZ-2026-002",
            "client_name": "Nexus Financial Tech",
            "project_type": "PostgreSQL & API Migration",
            "budget_usd": 22000
        },
        {
            "lead_id": "VIZ-2026-003",
            "client_name": "Quantum AI Systems",
            "project_type": "Python Backend Automation Pipeline",
            "budget_usd": 18500
        }
    ]


def allocate_lead(lead: Dict[str, Any], reps: List[str]) -> Dict[str, Any]:
    """
    Assigns a random account executive to an incoming client lead.
    Prevents IndexErrors by validating list availability.
    """
    if not reps:
        raise ValueError("Error: Account executive queue is empty. Cannot allocate lead.")

    # Select a random representative from the available reps list
    assigned_rep = random.choice(reps)

    # Attach assignment details to the lead object
    lead_copy = lead.copy()
    lead_copy["assigned_representative"] = assigned_rep
    lead_copy["status"] = "ASSIGNED"

    return lead_copy


def run_allocation_engine() -> None:
    """
    Main execution pipeline for Vizione Labs lead distribution.
    """
    print("==================================================================")
    print("         VIZIONE LABS - AUTOMATED LEAD ALLOCATION SYSTEM          ")
    print("==================================================================\n")

    reps = get_active_account_executives()
    incoming_queue = process_incoming_leads()

    print(f"[SYSTEM LOG] Loaded {len(reps)} active representatives.")
    print(f"[SYSTEM LOG] {len(incoming_queue)} pending leads found in execution queue.\n")

    allocated_leads = []

    for lead in incoming_queue:
        assigned_lead = allocate_lead(lead, reps)
        allocated_leads.append(assigned_lead)

        print(f"-> Lead ID: {assigned_lead['lead_id']}")
        print(f"   Client: {assigned_lead['client_name']}")
        print(f"   Scope:  {assigned_lead['project_type']}")
        print(f"   Assigned To: {assigned_lead['assigned_representative']}")
        print("-" * 50)

    print("\n[SUCCESS] All incoming leads successfully distributed.")
    print(f"Total Allocated Pipeline Value: ${sum(item['budget_usd'] for item in allocated_leads):,}")
    print("==================================================================")


if __name__ == "__main__":
    run_allocation_engine()