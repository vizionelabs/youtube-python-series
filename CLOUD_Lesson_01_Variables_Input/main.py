"""
Vizione Labs — Python: Build Real Projects Series
Lesson 01: Variables, Data Types, and User Input
File: main.py

Description: Real-world CLI User Profile & Onboarding Engine for Vizione Labs.
Demonstrates structured user data ingestion, explicit type validation, runtime memory
binding, and clean terminal presentation.
"""

import sys


def collect_profile_data() -> dict:
    """
    Prompts the user for profile details via CLI input, performs explicit type conversion,
    and returns a structured dictionary containing validated developer attributes.
    """
    print("=======================================================")
    print("   VIZIONE LABS — CLI USER PROFILE ONBOARDING ENGINE   ")
    print("=======================================================\n")

    # Raw String Ingestion
    full_name = input("--> Enter full name: ").strip()
    primary_language = input("--> Enter primary programming language: ").strip()

    # Numeric Ingestion with Type Casting
    raw_age = input("--> Enter developer age: ").strip()
    age = int(raw_age)

    raw_weekly_hours = input("--> Enter committed weekly learning hours: ").strip()
    weekly_hours = float(raw_weekly_hours)

    # Boolean Evaluation from Input String
    raw_pro_member = input("--> Are you enrolled in Vizione Pro Tier? (yes/no): ").strip().lower()
    is_pro_member = raw_pro_member in ("yes", "y", "true", "1")

    # Derived Calculations using Primitive Types
    annual_committed_hours = weekly_hours * 52.0

    profile_payload = {
        "full_name": full_name,
        "primary_language": primary_language,
        "age": age,
        "weekly_hours": weekly_hours,
        "annual_committed_hours": annual_committed_hours,
        "is_pro_member": is_pro_member
    }

    return profile_payload


def display_profile_summary(profile: dict) -> None:
    """
    Formats and prints the user profile dictionary into a production terminal card.
    """
    tier_label = "PRO TIER MEMBER" if profile["is_pro_member"] else "STANDARD MEMBER"

    summary_output = f"""
=======================================================
               VIZIONE LABS PROFILE SUMMARY            
=======================================================
 Developer Name   : {profile['full_name']}
 Age              : {profile['age']} years old
 Primary Track    : {profile['primary_language']}
 Membership Tier  : {tier_label}
-------------------------------------------------------
 Weekly Dedication: {profile['weekly_hours']:.1f} hrs/week
 Annual Target    : {profile['annual_committed_hours']:,.1f} hrs/year
=======================================================
 [STATUS] Profile successfully registered in local runtime.
=======================================================
"""
    print(summary_output)


def main() -> None:
    """
    Main execution pipeline entry point.
    """
    try:
        user_profile = collect_profile_data()
        display_profile_summary(user_profile)
    except ValueError as err:
        print(f"\n[ERROR] Invalid numerical input received: {err}", file=sys.stderr)
        print("[ERROR] Please re-run the program and provide valid numbers.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()