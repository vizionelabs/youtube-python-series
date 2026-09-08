"""
Vizione Labs - Lesson 01: Client Onboarding Automation Engine
Focus: Printing, String Manipulation, Input Function, Variable Assignment
"""


def run_onboarding_engine() -> None:
    # 1. Header Display (Multi-line String & String Concatenation)
    print("=" * 60)
    print("      VIZIONE LABS - AUTOMATED CLIENT ONBOARDING ENGINE      ")
    print("=" * 60 + "\n")

    # 2. Raw Input Ingestion (Input Function)
    raw_client_name: str = input("Enter Client Full Name: ")
    raw_company_name: str = input("Enter Company / Business Name: ")
    raw_service_tier: str = input("Enter Service Tier (Basic/Pro/Enterprise): ")
    raw_contract_val: str = input("Enter Contract Value (USD): ")

    # 3. String Manipulation & Data Cleaning
    # Cleaning whitespace and applying title/upper casing
    clean_client_name: str = raw_client_name.strip().title()
    clean_company_name: str = raw_company_name.strip().upper()
    clean_service_tier: str = raw_service_tier.strip().capitalize()
    clean_contract_val: str = raw_contract_val.strip()

    # 4. Dynamic String Concatenation & Variable Assignment
    client_id: str = clean_company_name[:3] + "_" + clean_client_name.replace(" ", "")

    # 5. Output Summary (Formatted Output & Multi-line Strings)
    print("\n" + "-" * 60)
    print("PROCESSING CLIENT INTAKE DATA...")
    print("-" * 60)

    formatted_summary: str = f"""
[ONBOARDING SUMMARY RECORD]
------------------------------------------------------------
Client ID       : {client_id}
Full Name       : {clean_client_name}
Organization    : {clean_company_name}
Assigned Tier   : {clean_service_tier}
Contract Amount : ${clean_contract_val}
System Status   : READY FOR DATABASE INGESTION
------------------------------------------------------------
"""
    print(formatted_summary)
    print("✅ Client onboarding record generated successfully.\n")


if __name__ == "__main__":
    run_onboarding_engine()