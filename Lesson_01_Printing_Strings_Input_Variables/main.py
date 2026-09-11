# ==============================================================================
# VIZIONE LABS - AUTOMATED CLIENT PROPOSAL GENERATOR (CLI TOOL)
# Production Architecture: String Manipulation, Input Parsing, and State Management
# ==============================================================================

def generate_client_proposal() -> None:
    # --------------------------------------------------------------------------
    # 1. HEADER BRANDING & SYSTEM INITIALIZATION
    # --------------------------------------------------------------------------
    print("=" * 60)
    print("      VIZIONE LABS | AUTOMATED CLIENT ONBOARDING & QUOTE ENGINE      ")
    print("=" * 60)
    print("System Status: Active | Environment: Production CLI\n")

    # --------------------------------------------------------------------------
    # 2. INTERACTIVE DATA INGESTION (INPUT CAPTURE)
    # --------------------------------------------------------------------------
    print(">>> STEP 1: CLIENT & PROJECT INGESTION")
    client_name: str = input("Enter Client Full Name: ")
    project_address: str = input("Enter Project Service Address: ")
    service_type: str = input("Enter Service Type (e.g., Sanding & Varnishing): ")
    estimated_area_sqm: str = input("Enter Total Floor Area (in m²): ")
    estimated_cost: str = input("Enter Base Investment Quote ($): ")

    print("\n" + "-" * 60)
    print("Processing payload and compiling dynamic proposal document...")
    print("-" * 60 + "\n")

    # --------------------------------------------------------------------------
    # 3. DYNAMIC PROPOSAL TEMPLATE ASSEMBLY (STRING CONCATENATION)
    # --------------------------------------------------------------------------
    proposal_header: str = "============================================================\n" + \
                           "                OFFICIAL SERVICE AGREEMENT                  \n" + \
                           "                    VIZIONE RESTORATION                     \n" + \
                           "============================================================"

    client_section: str = "\nCLIENT DETAILS:\n" + \
                          "  • Client Name:    " + client_name + "\n" + \
                          "  • Location:       " + project_address

    project_section: str = "\n\nPROJECT SCOPE & ESTIMATE:\n" + \
                           "  • Requested Service: " + service_type + "\n" + \
                           "  • Total Surface Area: " + estimated_area_sqm + " sq. meters\n" + \
                           "  • Total Investment:   $" + estimated_cost

    terms_section: str = "\n\nTERMS & EXECUTION:\n" + \
                         "  • Workmanship Guaranteed by Vizione Labs Architecture.\n" + \
                         "  • Proposal valid for 15 calendar days from issuance."

    proposal_footer: str = "\n============================================================\n" + \
                           "  Status: READY FOR CLIENT SIGNATURE                        \n" + \
                           "============================================================"

    # Compile complete proposal payload
    full_proposal_document: str = proposal_header + client_section + project_section + terms_section + proposal_footer

    # --------------------------------------------------------------------------
    # 4. TERMINAL DISPATCH & OUTPUT
    # --------------------------------------------------------------------------
    print(full_proposal_document)


if __name__ == "__main__":
    generate_client_proposal()