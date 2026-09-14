# ==============================================================================
# VZIONE LABS - ENTERPRISE AUTOMATION PIPELINE
# Lesson 03: Automated Lead Scoring & Qualification System
# File Path: main.py
# ==============================================================================

import json
from typing import Dict, Any, Union


def calculate_lead_score(payload: Dict[str, Any]) -> int:
    """
    Evaluates raw inbound client metrics and calculates an aggregate lead score.

    Parameters:
        payload (Dict[str, Any]): Inbound client metadata dictionary.

    Returns:
        int: Total computed lead score (0 - 100+).
    """
    score: int = 0

    # Revenue evaluation rules
    annual_revenue: float = payload.get("annual_revenue", 0.0)
    if annual_revenue >= 1_000_000.0:
        score += 40
    elif annual_revenue >= 250_000.0:
        score += 25
    elif annual_revenue >= 50_000.0:
        score += 10
    else:
        score += 0

    # Team scale evaluation
    engineering_team_size: int = payload.get("engineering_team_size", 0)
    if engineering_team_size > 20:
        score += 30
    elif engineering_team_size >= 5:
        score += 20
    else:
        score += 5

    # Strategic alignment scoring
    if payload.get("requires_custom_ai", False):
        score += 20

    if payload.get("immediate_start", False):
        score += 10

    return score


def evaluate_client_qualification(
        payload: Dict[str, Any]
) -> Dict[str, Union[str, int, bool]]:
    """
    Applies multi-variable boolean logic to qualify leads and determine target routing.

    Parameters:
        payload (Dict[str, Any]): Inbound client payload containing metadata.

    Returns:
        Dict[str, Union[str, int, bool]]: Evaluated qualification report.
    """
    client_name: str = payload.get("client_name", "Unknown Entity")
    lead_score: int = calculate_lead_score(payload)

    has_budget_approval: bool = payload.get("has_budget_approval", False)
    is_competitor: bool = payload.get("is_competitor", False)
    has_blacklisted_domain: bool = payload.get("has_blacklisted_domain", False)

    # Hard qualification gate using Boolean logic (not / or)
    is_blocked: bool = is_competitor or has_blacklisted_domain
    if is_blocked:
        return {
            "client_name": client_name,
            "lead_score": lead_score,
            "tier": "DISQUALIFIED",
            "action": "Drop Lead / Route to Security Logs",
            "is_actionable": False
        }

    # Nested & Multi-Condition Logic Gates (and / or)
    if lead_score >= 80 and has_budget_approval:
        tier: str = "ENTERPRISE_GOLD"
        action: str = "Direct Dispatch -> Senior Solutions Architect Calendar"
        is_actionable: bool = True
    elif lead_score >= 50 or (has_budget_approval and not is_blocked):
        tier: str = "MID_MARKET_SILVER"
        action: str = "Automated Dispatch -> Account Executive Follow-Up"
        is_actionable: bool = True
    else:
        tier: str = "NURTURE_BRONZE"
        action: str = "Route -> Automated Email Nurture Sequence"
        is_actionable: bool = False

    return {
        "client_name": client_name,
        "lead_score": lead_score,
        "tier": tier,
        "action": action,
        "is_actionable": is_actionable
    }


def process_inbound_pipeline() -> None:
    """Executes batch lead processing for Vizione Labs incoming payloads."""
    inbound_leads = [
        {
            "client_name": "Nexus Software Systems",
            "annual_revenue": 1_500_000.0,
            "engineering_team_size": 25,
            "requires_custom_ai": True,
            "immediate_start": True,
            "has_budget_approval": True,
            "is_competitor": False,
            "has_blacklisted_domain": False
        },
        {
            "client_name": "Apex Cloud Dynamics",
            "annual_revenue": 150_000.0,
            "engineering_team_size": 6,
            "requires_custom_ai": True,
            "immediate_start": False,
            "has_budget_approval": True,
            "is_competitor": False,
            "has_blacklisted_domain": False
        },
        {
            "client_name": "Rival Analytics Corp",
            "annual_revenue": 5_000_000.0,
            "engineering_team_size": 50,
            "requires_custom_ai": True,
            "immediate_start": True,
            "has_budget_approval": True,
            "is_competitor": True,
            "has_blacklisted_domain": False
        }
    ]

    print("==================================================================")
    print(" VZIONE LABS - INBOUND LEAD QUALIFICATION REPORT")
    print("==================================================================\n")

    for lead in inbound_leads:
        qualification_report = evaluate_client_qualification(lead)
        print(json.dumps(qualification_report, indent=4))
        print("-" * 66)


if __name__ == "__main__":
    process_inbound_pipeline()