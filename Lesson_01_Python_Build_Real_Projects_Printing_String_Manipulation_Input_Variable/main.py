# ==============================================================================
# VIZIONE LABS — ENTERPRISE SOFTWARE AUTOMATION PIPELINE
# Lesson 01: Production Lead & Client Ingestion Engine
# File: main.py
# ==============================================================================

import sys
from typing import Dict, Any


def render_system_header(service_name: str) -> None:
    """Renders a standardized terminal banner for Vizione Labs automation microservices."""
    divider: str = "=" * 65
    print(divider)
    print(f"  VIZIONE LABS AUTOMATION ENGINE | SERVICE: {service_name.upper()}")
    print(divider)


def capture_client_payload() -> Dict[str, str]:
    """Interactively captures raw client onboarding parameters from standard input stream.

    Returns:
        Dict[str, str]: Normalized key-value pairs representing client onboarding state.
    """
    print("\n[INFO] Initializing client payload intake session...")

    company_name: str = input("[INPUT] Enter Client Organization Name: ").strip()
    contact_email: str = input("[INPUT] Enter Primary Contact Email: ").strip()
    project_scope: str = input("[INPUT] Enter Initial Technical Scope (e.g., API, CRM, Web): ").strip()

    return {
        "company_name": company_name,
        "contact_email": contact_email,
        "project_scope": project_scope,
        "status": "INITIALIZED"
    }


def process_and_validate_payload(payload: Dict[str, str]) -> Dict[str, Any]:
    """Validates raw input payload strings and attaches Vizione Labs system metadata.

    Args:
        payload (Dict[str, str]): Raw dictionary received from input ingestion stage.

    Returns:
        Dict[str, Any]: Formatted, system-assigned payload ready for database persistence.
    """
    print("\n[SYSTEM] Validating payload integrity and binding internal state...")

    # Simple validation check on required string content
    is_valid: bool = len(payload["company_name"]) > 0 and len(payload["contact_email"]) > 0

    ingestion_status: str = "ACCEPTED" if is_valid else "REJECTED_INVALID_INPUT"
    system_handler: str = "vizione_labs_intake_service_v1"

    processed_record: Dict[str, Any] = {
        "client_organization": payload["company_name"],
        "lead_email": payload["contact_email"],
        "scope_assigned": payload["project_scope"],
        "ingestion_status": ingestion_status,
        "managed_by": system_handler
    }

    return processed_record


def output_ingestion_summary(record: Dict[str, Any]) -> None:
    """Formats and prints final client ingestion records to console output."""
    print("\n" + "-" * 65)
    print("  VIZIONE LABS — INGESTION SUMMARY REPORT")
    print("-" * 65)
    print(f"  Client Organization : {record['client_organization']}")
    print(f"  Primary Lead Email  : {record['lead_email']}")
    print(f"  Technical Scope     : {record['scope_assigned']}")
    print(f"  Pipeline Status     : {record['ingestion_status']}")
    print(f"  System Process Engine: {record['managed_by']}")
    print("-" * 65)


def main() -> None:
    """Main execution pipeline entry point."""
    render_system_header("Client Ingestion CLI Pipeline")

    try:
        raw_payload: Dict[str, str] = capture_client_payload()
        validated_record: Dict[str, Any] = process_and_validate_payload(raw_payload)
        output_ingestion_summary(validated_record)
        print("\n[SUCCESS] Client intake sequence finished with 0 errors.")
    except Exception as error:
        print(f"\n[FATAL ERROR] System execution halted: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()