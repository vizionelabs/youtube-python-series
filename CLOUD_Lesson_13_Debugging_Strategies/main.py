# ==============================================================================
# Vizione Labs — Python: Build Real Projects
# Lesson 13: Debugging Strategies, Exception Identification & Code Inspection
# File: main.py
# ==============================================================================

"""
PRODUCTION REAL-WORLD IMPLEMENTATION:
Enterprise Data Ingestion & Audit Pipeline with Defensive State Inspection

This script acts as an automated audit engine for incoming client usage records.
It applies comprehensive debugging strategies, input bounds checks, defensive exception
handling, and audit logging to isolate corrupted payload entries without crashing the system.
"""

import logging
from typing import Dict, List, Any, Tuple

# Initialize system logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s"
)
logger = logging.getLogger("VizioneLabs.AuditEngine")


class SystemAuditEngine:
    """
    Core engine responsible for parsing, validating, and auditing high-throughput
    service usage records for Vizione Labs platform accounts.
    """

    def __init__(self, platform_id: str):
        self.platform_id = platform_id
        self.processed_records: int = 0
        self.failed_records: int = 0

    def validate_payload_structure(self, record: Dict[str, Any]) -> None:
        """
        Validates structure using explicit bounds checking and assertions.
        Raises ValueError or AssertionError if bounds are violated.
        """
        required_keys = {"account_id", "compute_units", "tier"}
        missing_keys = required_keys - set(record.keys())
        
        if missing_keys:
            raise KeyError(f"Missing mandatory payload key(s): {missing_keys}")

        # Code Inspection Assertion: Validate numeric boundaries
        assert isinstance(record["compute_units"], (int, float)), "Compute units must be numeric."
        assert record["compute_units"] >= 0, f"Negative compute value detected: {record['compute_units']}"

    def calculate_adjusted_cost(self, units: float, rate_multiplier: float) -> float:
        """
        Calculates compute usage bill with defensive error handling for zero/negative multipliers.
        """
        if rate_multiplier <= 0:
            raise ZeroDivisionError("Rate multiplier must be strictly greater than zero.")
            
        base_cost = units * 0.045
        adjusted_cost = base_cost / rate_multiplier
        return round(adjusted_cost, 4)

    def process_audit_batch(self, batch_payload: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Audits a batch of telemetry payloads while executing defensive state tracking.
        """
        valid_audits = []
        audit_summary = {
            "platform_id": self.platform_id,
            "total_ingested": len(batch_payload),
            "successfully_billed": 0,
            "flagged_anomalies": 0,
            "anomalies_log": []
        }

        logger.info(f"Initiating batch processing for {len(batch_payload)} records...")

        for idx, payload in enumerate(batch_payload):
            try:
                # 1. Inspect Payload Structure
                self.validate_payload_structure(payload)

                # 2. Extract Key Fields
                account_id = payload["account_id"]
                units = payload["compute_units"]
                tier_multiplier = payload.get("tier_multiplier", 1.0)

                # 3. Perform Business Calculation
                billable_amount = self.calculate_adjusted_cost(units, tier_multiplier)

                audit_record = {
                    "account_id": account_id,
                    "compute_units": units,
                    "billed_amount": billable_amount,
                    "status": "VERIFIED"
                }
                
                valid_audits.append(audit_record)
                self.processed_records += 1

            except KeyError as ke:
                self.failed_records += 1
                error_entry = f"Record [{idx}] Schema Fault: {ke}"
                logger.warning(error_entry)
                audit_summary["anomalies_log"].append(error_entry)

            except AssertionError as ae:
                self.failed_records += 1
                error_entry = f"Record [{idx}] Boundary Violation: {ae}"
                logger.warning(error_entry)
                audit_summary["anomalies_log"].append(error_entry)

            except ZeroDivisionError as zde:
                self.failed_records += 1
                error_entry = f"Record [{idx}] Multiplier Anomaly: {zde}"
                logger.error(error_entry)
                audit_summary["anomalies_log"].append(error_entry)

            except Exception as unhandled:
                self.failed_records += 1
                error_entry = f"Record [{idx}] Unexpected Exception ({type(unhandled).__name__}): {unhandled}"
                logger.critical(error_entry)
                audit_summary["anomalies_log"].append(error_entry)

        audit_summary["successfully_billed"] = self.processed_records
        audit_summary["flagged_anomalies"] = self.failed_records

        return valid_audits, audit_summary


if __name__ == "__main__":
    print("=" * 80)
    print("VIZIONE LABS ENTERPRISE — AUDIT INGESTION ENGINE (LESSON 13)")
    print("=" * 80)

    # Simulated Batch Telemetry Stream with Intentional Telemetry Anomalies
    telemetry_stream = [
        {"account_id": "ACC-101", "compute_units": 1500, "tier": "Enterprise", "tier_multiplier": 1.2},
        {"account_id": "ACC-102", "compute_units": -500, "tier": "Pro"},  # Triggers AssertionError
        {"account_id": "ACC-103", "tier": "Developer", "tier_multiplier": 1.0},  # Triggers KeyError
        {"account_id": "ACC-104", "compute_units": 3200, "tier": "Standard", "tier_multiplier": 0.0},  # Triggers ZeroDivisionError
        {"account_id": "ACC-105", "compute_units": 450, "tier": "Starter", "tier_multiplier": 0.9}  # Valid
    ]

    engine = SystemAuditEngine(platform_id="VIZIONE-CLOUD-PROD-01")
    verified_records, summary = engine.process_audit_batch(telemetry_stream)

    print("\n--- VERIFIED BILLED TELEMETRY RECORDS ---")
    for rec in verified_records:
        print(f" Account: {rec['account_id']} | Units: {rec['compute_units']} | Final Bill: ${rec['billed_amount']}")

    print("\n--- ENTERPRISE AUDIT SUMMARY ---")
    print(f" Platform Instance    : {summary['platform_id']}")
    print(f" Total Records Streamed: {summary['total_ingested']}")
    print(f" Verified & Billed     : {summary['successfully_billed']}")
    print(f" Flagged Anomaly Count : {summary['flagged_anomalies']}")
    print("\n--- ANOMALY INCIDENT LOG ---")
    for incident in summary["anomalies_log"]:
        print(f" [!] {incident}")
    print("=" * 80)