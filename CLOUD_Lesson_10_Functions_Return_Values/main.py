"""
==============================================================================
Vizione Labs — Python: Build Real Projects Series
Lesson 10: Functions with Return Values, Docstrings, Multi-Return & Recursion
File: main.py
Project: Vizione Labs Financial Calculation & Audit Engine
==============================================================================
"""

import sys
from typing import Dict, List, Tuple, Union


# ------------------------------------------------------------------------------
# 1. Financial Calculation Engine (Return Values & Docstrings)
# ------------------------------------------------------------------------------
def calculate_invoice_net_payable(gross_amount: float, tax_rate: float, discount_rate: float = 0.0) -> Dict[str, float]:
    """
    Calculates the breakdown of an invoice line item including tax and discount.

    Args:
        gross_amount (float): Initial invoice gross total before taxes/discounts.
        tax_rate (float): Percentage rate of tax (e.g., 0.15 for 15%).
        discount_rate (float, optional): Percentage discount rate (e.g., 0.05 for 5%). Defaults to 0.0.

    Returns:
        Dict[str, float]: Detailed monetary summary with 'gross', 'discount',
                          'taxable_amount', 'tax', and 'net_payable'.
    """
    discount_amount = gross_amount * discount_rate
    taxable_base = gross_amount - discount_amount
    tax_amount = taxable_base * tax_rate
    net_payable = taxable_base + tax_amount

    return {
        "gross": round(gross_amount, 2),
        "discount": round(discount_amount, 2),
        "taxable_amount": round(taxable_base, 2),
        "tax": round(tax_amount, 2),
        "net_payable": round(net_payable, 2)
    }


# ------------------------------------------------------------------------------
# 2. Multi-Return Logic & Early Exit Safeguards
# ------------------------------------------------------------------------------
def evaluate_sla_performance(resolution_time_hours: float, client_tier: str) -> Tuple[bool, str, float]:
    """
    Evaluates SLA compliance for enterprise support tickets based on client tier.

    Args:
        resolution_time_hours (float): Time taken to resolve ticket in hours.
        client_tier (str): Service level ('Enterprise', 'Business', or 'Standard').

    Returns:
        Tuple[bool, str, float]:
            - is_compliant (bool): True if within SLA, False otherwise.
            - SLA_status (str): Descriptive performance label.
            - penalty_percentage (float): Financial penalty applied to invoice.
    """
    if resolution_time_hours < 0:
        return False, "INVALID_METRIC", 0.0

    tier = client_tier.upper().strip()

    if tier == "ENTERPRISE":
        target = 4.0
    elif tier == "BUSINESS":
        target = 12.0
    elif tier == "STANDARD":
        target = 24.0
    else:
        return False, "UNKNOWN_TIER", 0.0

    if resolution_time_hours <= target:
        return True, "SLA_MET_OPTIMAL", 0.0
    elif resolution_time_hours <= target * 1.5:
        return False, "SLA_BREACH_MINOR", 0.05
    else:
        return False, "SLA_BREACH_CRITICAL", 0.15


# ------------------------------------------------------------------------------
# 3. Recursive Compound Revenue Projection Engine
# ------------------------------------------------------------------------------
def forecast_compound_revenue(initial_revenue: float, annual_growth_rate: float, years: int) -> float:
    """
    Recursively forecasts financial growth over a sequence of years.

    Formula: Revenue(n) = Revenue(n-1) * (1 + rate)

    Args:
        initial_revenue (float): Starting baseline revenue.
        annual_growth_rate (float): Annual percentage increase (e.g., 0.12 for 12%).
        years (int): Number of future forecasting projection periods.

    Returns:
        float: Projected total revenue at year N.
    """
    # Base Case: Year 0 returns starting capital
    if years <= 0:
        return initial_revenue

    # Recursive Step: Accumulate compounded revenue year by year
    return forecast_compound_revenue(initial_revenue * (1 + annual_growth_rate), annual_growth_rate, years - 1)


# ------------------------------------------------------------------------------
# 4. Main Production Audit Orchestrator
# ------------------------------------------------------------------------------
def run_financial_audit_pipeline() -> None:
    """
    Orchestrates financial ledger processing, SLA validation, and long-term
    revenue forecasting for Vizione Labs enterprise clients.
    """
    print("=" * 80)
    print("VIZIONE LABS — FINANCIAL AUDIT & FORECASTING ENGINE")
    print("=" * 80)

    # Sample Enterprise Client Invoices
    invoice_batch = [
        {"client": "Acme Corp", "tier": "ENTERPRISE", "gross": 15000.0, "tax": 0.10, "disc": 0.05, "resolution_time": 3.5},
        {"client": "Stark Ind", "tier": "ENTERPRISE", "gross": 45000.0, "tax": 0.15, "disc": 0.10, "resolution_time": 5.2},
        {"client": "Nexus Ltd", "tier": "BUSINESS", "gross": 8500.0, "tax": 0.08, "disc": 0.00, "resolution_time": 18.0},
        {"client": "Global Tech", "tier": "STANDARD", "gross": 3200.0, "tax": 0.05, "disc": 0.00, "resolution_time": 22.0},
    ]

    total_pipeline_payable = 0.0

    print("\n--- 1. PROCESSING INVOICE BATCH & SLA COMPLIANCE ---")
    for idx, item in enumerate(invoice_batch, start=1):
        # 1. Financial breakdown
        financials = calculate_invoice_net_payable(
            gross_amount=item["gross"],
            tax_rate=item["tax"],
            discount_rate=item["disc"]
        )

        # 2. SLA SLA Evaluation
        is_compliant, sla_status, penalty_rate = evaluate_sla_performance(
            resolution_time_hours=item["resolution_time"],
            client_tier=item["tier"]
        )

        # 3. Apply penalty adjustment if applicable
        adjusted_payable = financials["net_payable"] * (1 - penalty_rate)
        total_pipeline_payable += adjusted_payable

        print(f"\n[Record #{idx}] Client: {item['client']} | Tier: {item['tier']}")
        print(f"  Gross: ${financials['gross']:,.2f} | Discount: ${financials['discount']:,.2f} | Tax: ${financials['tax']:,.2f}")
        print(f"  Net Payable: ${financials['net_payable']:,.2f}")
        print(f"  SLA Time: {item['resolution_time']}h -> Status: {sla_status} (Penalty: {penalty_rate * 100:.0f}%)")
        print(f"  Final Adjusted Invoice Total: ${adjusted_payable:,.2f}")

    print("\n" + "-" * 80)
    print(f"TOTAL AUDITED NET REVENUE ACROSS BATCH: ${total_pipeline_payable:,.2f}")
    print("-" * 80)

    # Forecasting Engine Demonstration using Recursion
    print("\n--- 2. RECURSIVE REVENUE GROWTH FORECAST (5-YEAR PROJECTION) ---")
    baseline_annual_revenue = total_pipeline_payable
    expected_growth_rate = 0.15  # 15% annual growth
    projection_years = 5

    projected_future_val = forecast_compound_revenue(
        initial_revenue=baseline_annual_revenue,
        annual_growth_rate=expected_growth_rate,
        years=projection_years
    )

    print(f"Baseline Year 0 Revenue: ${baseline_annual_revenue:,.2f}")
    print(f"Target Annual Growth: {expected_growth_rate * 100:.0f}%")
    print(f"Projected Year {projection_years} Revenue: ${projected_future_val:,.2f}")
    print("=" * 80)


if __name__ == "__main__":
    run_financial_audit_pipeline()