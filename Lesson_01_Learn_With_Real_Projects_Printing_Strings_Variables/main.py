# ==============================================================================
# VIZIONE LABS: REAL-WORLD PRODUCTION ENGINE
# Lesson 01: Automated Client Reception & Proposal Ingestion Engine
# Core Concepts: String Manipulation, Terminal Formatting, Input Sanitization
# ==============================================================================

def main() -> None:
    # --- TERMINAL HEADER & SYSTEM BANNER ---
    print("=" * 60)
    print("       APLICADORA VIZIONE - CLIENT ONBOARDING CLI")
    print("=" * 60)
    print("System Status: ONLINE")
    print("Initialization Engine: Active\n")

    # --- CLIENT DATA CAPTURE ---
    # Capturing primary client identity and project details
    raw_client_name: str = input("Enter Client Full Name: ")
    raw_project_address: str = input("Enter Property Address: ")
    raw_wood_type: str = input("Enter Wood Floor Type (e.g., Taco, Cumaru, Ipê): ")
    raw_area_sqm: str = input("Enter Total Area (in Square Meters): ")

    # --- INPUT SANITIZATION & STRING FORMATTING ---
    # Stripping leading/trailing whitespaces and formatting casing
    client_name: str = raw_client_name.strip().title()
    project_address: str = raw_project_address.strip().title()
    wood_type: str = raw_wood_type.strip().capitalize()
    area_sqm: str = raw_area_sqm.strip()

    # --- SYSTEM PROPOSAL SUMMARY OUTPUT ---
    print("\n" + "-" * 60)
    print("           AUTOMATED INTAKE PROPOSAL SUMMARY")
    print("-" * 60)
    print("Client Identity : " + client_name)
    print("Site Location   : " + project_address)
    print("Material Spec   : " + wood_type + " Flooring")
    print("Total Surface   : " + area_sqm + " m²")
    print("-" * 60)
    print("Status: Proposal record formatted successfully.")
    print("Action: Ready for restoration cost estimation and database dispatch.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()