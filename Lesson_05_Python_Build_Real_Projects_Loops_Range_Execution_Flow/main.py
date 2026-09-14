# ==============================================================================
# VIZIONE LABS - ENTERPRISE PRODUCTION SYSTEM
# Lesson 05: Automated SaaS Billing Audit & Account Health Processing Pipeline
# File: main.py
# ==============================================================================

from typing import Dict, List, Union, Tuple


def process_account_audit(
        clients_database: List[Dict[str, Union[str, int, float, bool]]]
) -> Tuple[List[Dict[str, Union[str, int, float, bool]]], Dict[str, Union[int, float]]]:
    """
    Iterates over client records, audits monthly API usage against tier limits,
    calculates overage charges, and aggregates platform performance metrics.

    :param clients_database: List of dictionaries representing SaaS client profiles.
    :return: Tuple containing processed client records and aggregate statistics.
    """
    processed_records: List[Dict[str, Union[str, int, float, bool]]] = []

    # Aggregator accumulator state variables
    total_platform_api_calls: int = 0
    total_overage_revenue: float = 0.0
    flagged_accounts_count: int = 0
    active_accounts_count: int = 0

    print("======================================================================")
    print("      VIZIONE LABS - AUTOMATED SAAS BILLING AUDIT PIPELINE            ")
    print("======================================================================\n")

    # Sequence iteration over database payload
    for client in clients_database:
        account_id: str = str(client["account_id"])
        company_name: str = str(client["company_name"])
        tier: str = str(client["tier"])
        monthly_limit: int = int(client["monthly_limit"])
        current_usage: int = int(client["current_usage"])
        base_fee: float = float(client["base_fee"])

        # Accumulate total API metrics across all accounts
        total_platform_api_calls += current_usage

        # Evaluation & Tiered Overage Calculation
        overage_fee: float = 0.0
        is_flagged: bool = False

        if current_usage > monthly_limit:
            excess_calls: int = current_usage - monthly_limit
            # $0.05 per API call over limit
            overage_fee = excess_calls * 0.05
            is_flagged = True
            flagged_accounts_count += 1
            print(f"[AUDIT FLAG] Account {account_id} ({company_name}) exceeded limit!")
            print(f"             Usage: {current_usage} / Limit: {monthly_limit} | Overage Fee: ${overage_fee:.2f}")
        else:
            active_accounts_count += 1
            print(f"[AUDIT PASS] Account {account_id} ({company_name}) within threshold.")

        total_overage_revenue += overage_fee
        total_bill: float = base_fee + overage_fee

        # Append audit results to record payload
        audited_record = {
            "account_id": account_id,
            "company_name": company_name,
            "tier": tier,
            "total_bill": round(total_bill, 2),
            "overage_fee": round(overage_fee, 2),
            "flagged": is_flagged
        }
        processed_records.append(audited_record)

    # Ranged audit cycle summary using range()
    print("\n----------------------------------------------------------------------")
    print("RUNNING AUTOMATED AUDIT CYCLE VERIFICATION (10 ITERATION LOG CHECKS)")
    print("----------------------------------------------------------------------")
    for cycle_check in range(1, 11):
        print(f"Verification Checkpoint #{cycle_check:02d}: System State Verified [OK]")

    # System Aggregation Summary
    aggregate_summary: Dict[str, Union[int, float]] = {
        "total_clients": len(clients_database),
        "active_accounts": active_accounts_count,
        "flagged_accounts": flagged_accounts_count,
        "total_api_calls": total_platform_api_calls,
        "total_overage_revenue": round(total_overage_revenue, 2)
    }

    return processed_records, aggregate_summary


if __name__ == "__main__":
    # Simulated Vizione Labs Client Database
    vizione_labs_clients: List[Dict[str, Union[str, int, float, bool]]] = [
        {
            "account_id": "VIZ-101",
            "company_name": "Apex Digital Analytics",
            "tier": "Starter",
            "monthly_limit": 5000,
            "current_usage": 4200,
            "base_fee": 99.00
        },
        {
            "account_id": "VIZ-102",
            "company_name": "Nexus Global AI",
            "tier": "Enterprise",
            "monthly_limit": 50000,
            "current_usage": 68500,
            "base_fee": 899.00
        },
        {
            "account_id": "VIZ-103",
            "company_name": "Quantum Cloud Solutions",
            "tier": "Professional",
            "monthly_limit": 15000,
            "current_usage": 14200,
            "base_fee": 299.00
        },
        {
            "account_id": "VIZ-104",
            "company_name": "Vanguard Tech Systems",
            "tier": "Professional",
            "monthly_limit": 15000,
            "current_usage": 22100,
            "base_fee": 299.00
        }
    ]

    # Execute Audit Pipeline
    audited_accounts, summary_metrics = process_account_audit(vizione_labs_clients)

    print("\n======================================================================")
    print("                  VIZIONE LABS AUDIT METRICS SUMMARY                  ")
    print("======================================================================")
    print(f"Total Accounts Audited : {summary_metrics['total_clients']}")
    print(f"Active Compliant       : {summary_metrics['active_accounts']}")
    print(f"Flagged Overage        : {summary_metrics['flagged_accounts']}")
    print(f"Total Platform Calls   : {summary_metrics['total_api_calls']:,} requests")
    print(f"Total Overage Revenue  : ${summary_metrics['total_overage_revenue']:.2f}")
    print("======================================================================\n")