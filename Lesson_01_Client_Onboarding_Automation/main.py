# ==============================================================================
# LESSON 01: REAL-WORLD PRODUCTION SYSTEM
# System: Client Onboarding Data Ingestion Engine
# Domain: Client CRM & Communication APIs / Service & Labor Management
# ==============================================================================

# 1. HEADER & SYSTEM INITIALIZATION
print("==================================================")
print("     VIZIONE LABS - CLIENT ONBOARDING ENGINE      ")
print("==================================================")
print("Initializing client intake protocol...\n")

# 2. DATA INGESTION VIA TERMINAL INPUTS
# Capture raw data directly from user prompts and assign them to explicit variables
client_company_name: str = input("Enter Client Company / Name: ")
primary_contact_person: str = input("Enter Primary Contact Name: ")
service_scope: str = input("Enter Requested Service Scope (e.g., Wood Floor Restoration): ")
estimated_square_meters: str = input("Enter Area Size (sq meters): ")
target_start_date: str = input("Enter Target Start Date (YYYY-MM-DD): ")

# 3. DATA PROCESSING & STRING FORMATTING
# Formatting raw variable data into structured business communications and system payloads
print("\n" + "=" * 50)
print("PROCESSING INGESTED DATA...")
print("=" * 50)

# Generating formatted internal record summary
client_profile_record: str = (
    "[CLIENT PROFILE RECORD]\n"
    + "Account Name: " + client_company_name + "\n"
    + "Lead Contact: " + primary_contact_person + "\n"
    + "Service Requested: " + service_scope + "\n"
    + "Project Area: " + estimated_square_meters + " m²\n"
    + "Schedule Date: " + target_start_date
)

# Generating automated onboarding confirmation message for client dispatch
automated_client_welcome_email: str = (
    "Dear " + primary_contact_person + ",\n\n"
    + "Thank you for choosing Vizione Labs. We have successfully registered "
    + client_company_name + " in our service management platform.\n"
    + "Our team is scheduled to begin the " + service_scope + " project ("
    + estimated_square_meters + " m²) on " + target_start_date + ".\n\n"
    + "Best regards,\n"
    + "Operations Team | Vizione Labs"
)

# 4. OUTPUT EXECUTION & SYSTEM DISPATCH
print("\n--- INTERNAL CRM PAYLOAD ---")
print(client_profile_record)

print("\n--- AUTOMATED EMAIL DISPATCH PREVIEW ---")
print(automated_client_welcome_email)

print("\n[SUCCESS] Client intake complete. Data ingested and formatted successfully.")