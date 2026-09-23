# ==============================================================================
# Vizione Labs — Python: Build Real Projects
# Lesson 01: Printing, String Manipulation, Input Function, Variable Assignment
# File: main.py
# ==============================================================================

def display_header():
    """Renders the Vizione Labs standard CLI visual banner."""
    divider = "=" * 60
    print(divider)
    print("              VIZIONE LABS ARCHITECTURE PORTAL              ")
    print("         Developer Profile & Onboarding Engine v1.0         ")
    print(divider + "\n")


def collect_developer_profile():
    """
    Collects raw user profile data, performs string sanitization,
    and dynamically binds attributes to profile variables.
    """
    print("[+] INITIALIZING USER ONBOARDING PIPELINE...\n")

    # Interactive Console Input Ingestion
    raw_full_name = input("Enter your full legal or professional name: ")
    raw_primary_track = input("Enter your track (e.g., Python / Full-Stack): ")
    raw_target_role = input("Enter your target career title: ")

    # String Sanitization & Formatting Pipeline
    clean_full_name = raw_full_name.strip().title()
    clean_primary_track = raw_primary_track.strip().upper()
    clean_target_role = raw_target_role.strip().title()

    # Dynamic Variable Binding & Record Assembly
    profile_status = "PROVISIONAL"
    developer_id = "DEV-" + clean_primary_track[:3] + "-2026"

    # Construction of System Confirmation Digest
    print("\n" + "-" * 60)
    print("   VIZIONE LABS DEVELOPER PROFILE RECORD")
    print("-" * 60)
    print(" Developer ID  : " + developer_id)
    print(" Full Name     : " + clean_full_name)
    print(" Active Track  : " + clean_primary_track)
    print(" Target Role   : " + clean_target_role)
    print(" Account Status: " + profile_status)
    print("-" * 60)

    # State Mutation Demonstration (Updating Account Status)
    input("\nPress ENTER to execute automated profile verification...")
    profile_status = "VERIFIED_ACTIVE"

    print("\n[+] System State Mutation Successful!")
    print("Updated Account Status: " + profile_status)
    print("Welcome aboard, " + clean_full_name + "! Your portal environment is ready.\n")


def main():
    display_header()
    collect_developer_profile()


if __name__ == "__main__":
    main()