"""
Vizione Labs - Lesson 04: Randomization & Data Structures
System: Automated Field Service Lead Dispatcher
"""

import random
from typing import List, Dict, Union

# Define initial technician rosters and active incoming lead queue
field_technicians: List[str] = ["Marcus Vance", "Elena Rostova", "David Chen", "Sarah Miller"]
service_vehicles: List[str] = ["Van 01 (Ford Transit)", "Van 02 (Mercedes Sprinter)", "Van 03 (RAM ProMaster)"]

# Nested Data Structure: Incoming job leads with details
incoming_leads: List[Dict[str, Union[str, int]]] = [
    {"client": "Apex Commercial Group", "service": "Hardwood Sanding", "sqft": 2500},
    {"client": "Highland Residential", "service": "Parquet Calafetação", "sqft": 800},
    {"client": "Vanguard Logistics", "service": "Polyurethane Varnishing", "sqft": 4200},
]


def dispatch_single_lead(lead_index: int) -> None:
    """
    Dispatches a specific lead by index using random allocation and safe index boundaries.
    """
    total_leads = len(incoming_leads)

    # Prevent IndexError by validating the list boundaries
    if lead_index < 0 or lead_index >= total_leads:
        print(f"[ERROR] Index {lead_index} is out of bounds! Current lead queue length is {total_leads}.")
        return

    # Select lead safely
    selected_lead = incoming_leads[lead_index]

    # Randomly select technician and service vehicle using random module
    assigned_tech = random.choice(field_technicians)
    assigned_vehicle = random.choice(service_vehicles)

    # Dynamic payout calculation based on random index modifier
    base_rate_per_sqft = 3.50
    estimated_revenue = selected_lead["sqft"] * base_rate_per_sqft

    print("=" * 60)
    print(f"DISPATCHING LEAD #{lead_index + 1}: {selected_lead['client']}")
    print("-" * 60)
    print(f"Service Type     : {selected_lead['service']}")
    print(f"Area Size        : {selected_lead['sqft']} sq ft")
    print(f"Estimated Value  : ${estimated_revenue:,.2f}")
    print(f"Assigned Tech    : {assigned_tech}")
    print(f"Assigned Vehicle : {assigned_vehicle}")
    print("=" * 60 + "\n")


def run_automated_dispatch_pipeline() -> None:
    """
    Executes the automated dispatch loop and demonstrates safe list mutations.
    """
    print("Starting Vizione Lead Dispatcher System...\n")

    # Dispatch lead at index 0
    dispatch_single_lead(0)

    # Mutate technician roster: Add a new technician dynamically
    new_tech = "James"
    print(f"[SYSTEM UPDATE] Onboarding new field specialist: {new_tech}")
    field_technicians.append(new_tech)
    print(f"Active Technicians ({len(field_technicians)} total): {field_technicians}\n")

    # Dispatch lead at index 1
    dispatch_single_lead(1)

    # Demonstrating Safe Boundary Handling (Attempting out-of-range index)
    print("[TESTING BOUNDARY LOGIC] Attempting to query an invalid lead index...")
    invalid_index = 99
    dispatch_single_lead(invalid_index)


if __name__ == "__main__":
    run_automated_dispatch_pipeline()