"""
Commercial Credit Risk & Loan Approval Engine
Vizione Labs - Lesson 03: Conditional Logic & Business Rules
"""

# Client Evaluation Profile Data
company_name: str = "Apex Logistics Solutions"
credit_score: int = 710
annual_revenue_usd: float = 1_250_000.00
debt_to_equity_ratio: float = 0.35
has_prior_bankruptcy: bool = False
requested_loan_amount_usd: float = 350_000.00

# Risk Analysis Threshold Constants
MIN_CREDIT_SCORE_PRIME: int = 720
MIN_CREDIT_SCORE_STANDARD: int = 650
MAX_DEBT_RATIO_STANDARD: float = 0.45
MAX_DEBT_RATIO_HIGH_RISK: float = 0.30
MIN_REVENUE_FOR_EXPANDED_CREDIT: float = 1_000_000.00

print(f"=== INITIALIZING CREDIT EVALUATION: {company_name.upper()} ===")
print(f"Requested Loan: ${requested_loan_amount_usd:,.2f}")
print(f"Credit Score: {credit_score} | Revenue: ${annual_revenue_usd:,.2f} | D/E Ratio: {debt_to_equity_ratio}\n")

# Top-level Guard Clause: Bankruptcy Filter using logical NOT
if has_prior_bankruptcy:
    approval_status = "REJECTED"
    risk_tier = "CRITICAL"
    reason = "Automatic disqualification due to prior bankruptcy record."
else:
    # Nested Evaluation Logic: Tier 1 - Prime Approval
    if credit_score >= MIN_CREDIT_SCORE_PRIME and debt_to_equity_ratio <= MAX_DEBT_RATIO_STANDARD:
        approval_status = "APPROVED"
        risk_tier = "PRIME"
        reason = "Excellent credit score and healthy leverage ratio."

    # Tier 2 - Standard Approval (Logical AND & OR combination)
    elif credit_score >= MIN_CREDIT_SCORE_STANDARD and debt_to_equity_ratio <= MAX_DEBT_RATIO_STANDARD:
        # Nested check for larger loan requests against annual revenue
        if requested_loan_amount_usd > (annual_revenue_usd * 0.30):
            if annual_revenue_usd >= MIN_REVENUE_FOR_EXPANDED_CREDIT and debt_to_equity_ratio <= MAX_DEBT_RATIO_HIGH_RISK:
                approval_status = "APPROVED"
                risk_tier = "STANDARD (EXPANDED)"
                reason = "High exposure approved based on strong annual revenue and low debt."
            else:
                approval_status = "CONDITIONAL APPROVAL"
                risk_tier = "MODERATE RISK"
                reason = "Loan amount exceeds standard exposure limit relative to revenue; collateral required."
        else:
            approval_status = "APPROVED"
            risk_tier = "STANDARD"
            reason = "Standard eligibility criteria satisfied."

    # Tier 3 - Subprime / High Risk Evaluation
    elif credit_score >= 580 or annual_revenue_usd >= 2_000_000.00:
        approval_status = "UNDER MANUAL REVIEW"
        risk_tier = "HIGH RISK"
        reason = "Underwriting review required due to lower credit score or high revenue offset."

    else:
        approval_status = "REJECTED"
        risk_tier = "UNACCEPTABLE RISK"
        reason = "Credit score and financial metrics fall below minimal threshold requirements."

# Decision Engine Output
print("=== DECISION ENGINE SUMMARY ===")
print(f"Status: {approval_status}")
print(f"Risk Tier: {risk_tier}")
print(f"Underwriting Note: {reason}")