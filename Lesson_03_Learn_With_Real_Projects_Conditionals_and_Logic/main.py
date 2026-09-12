# ==============================================================================
# VIZIONE LABS - AUTOMATED CRM LEAD QUALIFICATION & SLA ROUTING ENGINE
# File: main.py
# Description: Evaluates incoming project inquiries using conditional logic,
#              logical operators, and nested checks to assign SLA tiers,
#              routing queues, and automated pricing discounts.
# ==============================================================================

def evaluate_lead(
        client_name: str,
        estimated_budget: float,
        deadline_days: int,
        requires_custom_architecture: bool,
        is_existing_client: bool
) -> dict:
    """
    Processes client lead metrics and returns a routing decision package.
    """
    print(f"\n[VIZIONE LABS ENGINE] Processing inquiry for: {client_name}")

    # 1. Lead Tier & Base Priority Evaluation
    # Enterprise Tier: Budget >= $10,000 OR (Budget >= $7,500 AND Existing Client)
    if estimated_budget >= 10000.0 or (estimated_budget >= 7500.0 and is_existing_client):
        lead_tier = "Tier 1 - Enterprise"
        priority_score = 95
    elif estimated_budget >= 4000.0:
        lead_tier = "Tier 2 - Mid-Market"
        priority_score = 75
    elif estimated_budget >= 1500.0:
        lead_tier = "Tier 3 - SMB"
        priority_score = 55
    else:
        lead_tier = "Unqualified"
        priority_score = 10

    # Early Exit for Unqualified Leads
    if lead_tier == "Unqualified":
        return {
            "client_name": client_name,
            "lead_tier": lead_tier,
            "status": "REJECTED",
            "routing_queue": "Automated Self-Service Portal",
            "assigned_sla_hours": 72,
            "discount_eligible": False
        }

    # 2. SLA SLA Hours & Routing Queue Determination (Nested Logic)
    if lead_tier == "Tier 1 - Enterprise":
        if deadline_days <= 5:
            routing_queue = "CRITICAL_RUSH_ENGINEERING"
            assigned_sla_hours = 2
        else:
            routing_queue = "ENTERPRISE_SOLUTIONS_DESK"
            assigned_sla_hours = 12
    elif lead_tier == "Tier 2 - Mid-Market":
        if deadline_days <= 7 and requires_custom_architecture:
            routing_queue = "SENIOR_FULLSTACK_QUEUE"
            assigned_sla_hours = 12
        else:
            routing_queue = "STANDARD_DEV_QUEUE"
            assigned_sla_hours = 24
    else:  # Tier 3 - SMB
        routing_queue = "SMB_SUPPORT_DESK"
        assigned_sla_hours = 48

    # 3. Discount & Special Incentive Logic
    # Clients qualify for a 10% retainer discount if they are existing clients OR high budget without rush deadlines
    if is_existing_client or (estimated_budget >= 8000.0 and not deadline_days <= 3):
        discount_eligible = True
    else:
        discount_eligible = False

    return {
        "client_name": client_name,
        "lead_tier": lead_tier,
        "priority_score": priority_score,
        "status": "QUALIFIED",
        "routing_queue": routing_queue,
        "assigned_sla_hours": assigned_sla_hours,
        "discount_eligible": discount_eligible
    }


# ------------------------------------------------------------------------------
# SIMULATION / DRIVER EXECUTION
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Sample Test Inquiries for Vizione Labs
    test_leads = [
        {
            "client_name": "Acme Fintech Corp",
            "estimated_budget": 12500.0,
            "deadline_days": 4,
            "requires_custom_architecture": True,
            "is_existing_client": False
        },
        {
            "client_name": "Nexus Retail Analytics",
            "estimated_budget": 8000.0,
            "deadline_days": 6,
            "requires_custom_architecture": True,
            "is_existing_client": True
        },
        {
            "client_name": "Local Bistro Tech",
            "estimated_budget": 800.0,
            "deadline_days": 14,
            "requires_custom_architecture": False,
            "is_existing_client": False
        }
    ]

    print("=================================================================")
    print("       VIZIONE LABS AUTOMATED CRM LEAD ROUTER INITIALIZED        ")
    print("=================================================================")

    for lead in test_leads:
        result = evaluate_lead(
            client_name=lead["client_name"],
            estimated_budget=lead["estimated_budget"],
            deadline_days=lead["deadline_days"],
            requires_custom_architecture=lead["requires_custom_architecture"],
            is_existing_client=lead["is_existing_client"]
        )

        print(f"Status: {result['status']}")
        print(f"Tier: {result['lead_tier']} | Queue: {result['routing_queue']}")
        print(f"SLA Target: {result['assigned_sla_hours']} Hours | Discount: {result['discount_eligible']}")
        print("-" * 65)