# ==============================================================================
# VIZIONE LABS - ENTERPRISE AUTOMATION ENGINE
# File: main.py
# Module: Client Intake & Terminal Ingestion Pipeline
# Lesson 01: Printing, String Manipulation, Input Function, Variable Assignment
# ==============================================================================

def format_system_header(system_name: str) -> str:
    """
    Generates a standardized ASCII banner for Vizione Labs terminal tools.
    """
    border = "=" * 60
    return f"{border}\n  VIZIONE LABS | {system_name.upper()}\n{border}"


def process_client_intake() -> dict[str, str]:
    """
    Captures raw client intake parameters from the terminal console
    and normalizes user input into a structured dictionary record.
    """
    print(format_system_header("CLIENT INGESTION PIPELINE"))
    print("[STATUS] Initializing CLI Data Parsing...\n")

    # Step 1: Capture Raw Terminal Inputs
    raw_company_name = input("Enter Client Company Name: ")
    raw_primary_contact = input("Enter Primary Technical Contact: ")
    raw_contract_tier = input("Enter Service Tier (Standard/Enterprise): ")

    # Step 2: String Manipulation & Data Normalization
    clean_company_name = raw_company_name.strip().title()
    clean_primary_contact = raw_primary_contact.strip().title()
    clean_contract_tier = raw_contract_tier.strip().upper()

    # Step 3: Construct Normalized Client Record
    client_record = {
        "company_name": clean_company_name,
        "primary_contact": clean_primary_contact,
        "contract_tier": clean_contract_tier,
        "system_status": "PROVISIONED"
    }

    return client_record


def display_ingestion_summary(record: dict[str, str]) -> None:
    """
    Prints a formatted summary report to the terminal console.
    """
    print("\n" + format_system_header("INGESTION SUMMARY REPORT"))

    # Utilizing string concatenation and clean variable output
    summary_output = (
            "Client Name   : " + record["company_name"] + "\n" +
            "Tech Lead     : " + record["primary_contact"] + "\n" +
            "Service Level : " + record["contract_tier"] + "\n" +
            "Status        : " + record["system_status"]
    )

    print(summary_output)
    print("=" * 60)
    print("[SUCCESS] Client profile ingested successfully into Vizione Labs DB.\n")


def main() -> None:
    """
    Execution entry point for the Vizione Labs Client Intake Tool.
    """
    client_data = process_client_intake()
    display_ingestion_summary(client_data)


if __name__ == "__main__":
    main()