"""
Vizione Labs - Lesson 02: Automated Payroll & Tax Calculation Engine
Focus: Data Types, Type Casting, Mathematical Operations, String Interpolation (f-strings)
"""


def run_payroll_engine() -> None:
    # 1. Header Display
    print("=" * 65)
    print("     VIZIONE LABS - AUTOMATED PAYROLL & TAX ENGINE     ")
    print("=" * 65 + "\n")

    # 2. Raw Input Ingestion (All inputs initially captured as string data)
    raw_employee_name: str = input("Enter Employee Name: ")
    raw_hourly_rate: str = input("Enter Hourly Pay Rate (USD): ")
    raw_hours_worked: str = input("Enter Hours Worked (Current Cycle): ")
    raw_tax_rate: str = input("Enter Tax Deduction Rate (e.g., 15 for 15%): ")

    # 3. Explicit Type Casting & Mathematical Operations
    # Converting string inputs to float and int types for math processing
    hourly_rate: float = float(raw_hourly_rate.strip())
    hours_worked: float = float(raw_hours_worked.strip())
    tax_rate_percent: float = float(raw_tax_rate.strip())

    # Financial calculations using mathematical operators
    gross_pay: float = hourly_rate * hours_worked
    tax_deduction: float = gross_pay * (tax_rate_percent / 100.0)
    net_payout: float = gross_pay - tax_deduction

    # Data type inspection for debugging & verification
    employee_name: str = raw_employee_name.strip().title()

    # 4. Dynamic Output Generation (f-strings & Precision Formatting)
    print("\n" + "-" * 65)
    print("PROCESSING FINANCIAL PAYROLL DATA...")
    print("-" * 65)

    payroll_statement: str = f"""
[OFFICIAL PAYROLL STATEMENT RECORD]
-----------------------------------------------------------------
Employee Name    : {employee_name}
Hourly Pay Rate  : ${hourly_rate:.2f}/hr
Hours Worked     : {hours_worked:.1f} hrs
-----------------------------------------------------------------
Gross Earnings   : ${gross_pay:.2f}
Tax Deduction    : ${tax_deduction:.2f} ({tax_rate_percent:.1f}%)
-----------------------------------------------------------------
NET PAYOUT       : ${net_payout:.2f}
System Status    : AUDITED & PREPARED FOR DISBURSEMENT
-----------------------------------------------------------------
"""
    print(payroll_statement)
    print("✅ Payroll calculations completed and formatted successfully.\n")


if __name__ == "__main__":
    run_payroll_engine()