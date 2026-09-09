"""
Corporate Payroll & Tax Calculation Engine
Lesson 05: Loops, Range Function, and Iteration Logic
Vizione Labs - Business Automation Track
"""

from typing import List, Dict

# Employee payroll raw dataset
EMPLOYEE_NAMES: List[str] = [
    "Alice Smith",
    "Bob Jones",
    "Charlie Brown",
    "Diana Prince",
    "Evan Wright"
]

BASE_SALARIES: List[float] = [
    5500.00,
    3200.00,
    8900.00,
    4100.00,
    12500.00
]

TAX_BRACKET_THRESHOLD: float = 5000.00
HIGH_TAX_RATE: float = 0.22
STANDARD_TAX_RATE: float = 0.15


def Process_corporate_payroll() -> None:
    """
    Executes automated batch payroll processing using for loops,
    range-based sequence indexing, and real-time tax aggregation.
    """
    total_gross_payroll: float = 0.0
    total_tax_withheld: float = 0.0
    total_net_payroll: float = 0.0
    processed_records: List[Dict[str, float]] = []

    employee_count: int = len(EMPLOYEE_NAMES)

    print("=" * 65)
    print("      VIZIONE LABS CORPORATE PAYROLL ENGINE - BATCH EXECUTION")
    print("=" * 65)

    # 1. Iteration using range() and len() for index-matched collection processing
    for index in range(employee_count):
        employee_name: str = EMPLOYEE_NAMES[index]
        gross_salary: float = BASE_SALARIES[index]

        # Conditional tax rate logic based on income bracket
        if gross_salary >= TAX_BRACKET_THRESHOLD:
            applied_tax_rate: float = HIGH_TAX_RATE
        else:
            applied_tax_rate: float = STANDARD_TAX_RATE

        tax_amount: float = gross_salary * applied_tax_rate
        net_salary: float = gross_salary - tax_amount

        # Accumulation pattern for financial reporting
        total_gross_payroll += gross_salary
        total_tax_withheld += tax_amount
        total_net_payroll += net_salary

        processed_records.append({
            "name": employee_name,
            "gross": gross_salary,
            "tax": tax_amount,
            "net": net_salary
        })

        print(f"[{index + 1}/{employee_count}] Processed: {employee_name:<15} | Gross: ${gross_salary:>9.2f} | Tax: ${tax_amount:>8.2f} | Net: ${net_salary:>9.2f}")

    print("-" * 65)
    print("      BATCH SUMMARY & FINANCIAL AUDIT TRAIL")
    print("-" * 65)
    print(f"Total Employees Processed : {employee_count}")
    print(f"Total Gross Payroll       : ${total_gross_payroll:,.2f}")
    print(f"Total Tax Withheld        : ${total_tax_withheld:,.2f}")
    print(f"Total Net Disbursement    : ${total_net_payroll:,.2f}")
    print("=" * 65)

    # 2. Direct sequence iteration over structured output records
    print("\nExecuting Individual Payroll Slip Generation Check:")
    for record in processed_records:
        print(f" -> Disbursement confirmed for {record['name']}: Net Credit ${record['net']:,.2f}")


if __name__ == "__main__":
    Process_corporate_payroll()