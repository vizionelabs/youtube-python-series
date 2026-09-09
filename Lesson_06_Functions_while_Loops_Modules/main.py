"""
Main Execution Script
Module: main.py
Orchestrates client interaction using an interactive while loop and delegates logic to inventory_engine.
"""

import sys
from typing import Dict, Union
from inventory_engine import generate_job_quote


def main() -> None:
    print("==================================================")
    print("   VIZIONE LABS | SERVICE QUOTE AUTOMATION SYSTEM ")
    print("==================================================\n")

    system_active: bool = True

    while system_active:
        print("\n--- CREATE NEW CLIENT ESTIMATE ---")

        try:
            sqft_input: float = float(input("Enter surface area (sq ft): "))
            if sqft_input <= 0:
                print("Error: Area must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numerical value for area.")
            continue

        print("Select Material Tier: [standard / premium / industrial]")
        material_input: str = input("Material selection: ").strip().lower()
        if material_input not in ["standard", "premium", "industrial"]:
            print("Invalid tier selected. Defaulting to 'standard'.")
            material_input = "standard"

        rush_input: str = input("Expedited rush job? (y/n): ").strip().lower()
        is_rush: bool = rush_input == 'y'

        # Invoke custom module logic
        quote_summary: Dict[str, Union[float, str]] = generate_job_quote(
            area_sqft=sqft_input,
            material_type=material_input,
            rush_job=is_rush
        )

        # Output dynamic quote report
        print("\n========================================")
        print("          OFFICIAL JOB ESTIMATE         ")
        print("========================================")
        print(f" Surface Area   : {quote_summary['area']} sq ft")
        print(f" Material Tier  : {quote_summary['material_tier']}")
        print(f" Material Cost  : ${quote_summary['material_cost']:.2f}")
        print(f" Labor Cost     : ${quote_summary['labor_cost']:.2f}")
        print("----------------------------------------")
        print(f" Subtotal       : ${quote_summary['subtotal']:.2f}")
        print(f" Municipal Tax  : ${quote_summary['tax']:.2f}")
        print(f" FINAL TOTAL    : ${quote_summary['total']:.2f}")
        print("========================================\n")

        # Interactive state loop controller
        user_choice: str = input("Generate another quote? (y/n): ").strip().lower()
        if user_choice != 'y':
            system_active = False
            print("\nShutting down quote engine... All calculations finalized.")


if __name__ == "__main__":
    main()