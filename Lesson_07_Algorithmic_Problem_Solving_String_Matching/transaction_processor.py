# ==============================================================================
# VIZIONE LABS - ENTERPRISE AUTOMATION & AUDIT ENGINE
# FILE: transaction_processor.py
# DESCRIPTION: Production transaction reconciliation system utilizing state tracking,
#              pattern matching, and dynamic audit flags for financial compliance.
# ==============================================================================

import re
from typing import List, Dict, Any, Tuple


class AuditState:
    """Explicit state Machine constants for audit tracking lifecycle."""
    IDLE = "IDLE"
    INGESTING = "INGESTING"
    SUSPENDED = "SUSPENDED"
    COMPLETED = "COMPLETED"


class TransactionAuditEngine:
    """
    Engine responsible for processing raw financial audit streams, identifying patterns,
    tracking runtime state transitions, and flagging non-compliant transactions.
    """

    def __init__(self, variance_threshold: float = 500.00) -> None:
        self.variance_threshold: float = variance_threshold
        self.current_state: str = AuditState.IDLE
        self.processed_count: int = 0
        self.reconciled_ledger: List[Dict[str, Any]] = []
        self.flagged_audit_trail: List[Dict[str, Any]] = []

    def transition_state(self, new_state: str) -> None:
        """Mutates the internal operational state of the engine."""
        print(f"[STATE SHIFT] Transitioning from '{self.current_state}' to '{new_state}'")
        self.current_state = new_state

    def parse_transaction_string(self, raw_entry: str) -> Tuple[str, str, float, str]:
        """
        Parses raw unformatted audit logs using pattern extraction.
        Format expected: <TIMESTAMP> | <TXN_ID> | <AMOUNT> | <STATUS_TAG>
        """
        # RegEx pattern for strict string matching across raw entries
        pattern = r"^([\d\-:\s]+)\s*\|\s*(TXN_\d+)\s*\|\s*([\d\.-]+)\s*\|\s*\[(\w+)\]$"
        match = re.match(pattern, raw_entry.strip())

        if not match:
            raise ValueError(f"Malformed log entry pattern detected: '{raw_entry}'")

        timestamp, txn_id, raw_amount, status_flag = match.groups()
        return timestamp, txn_id, float(raw_amount), status_flag

    def process_stream(self, stream_data: List[str]) -> Dict[str, Any]:
        """
        Processes a sequential stream of string records using state tracking
        and algorithmic pattern verification.
        """
        self.transition_state(AuditState.INGESTING)

        for entry in stream_data:
            entry_clean = entry.strip()

            # Command Sentinels for State Control
            if entry_clean == "COMMAND:PAUSE":
                self.transition_state(AuditState.SUSPENDED)
                continue
            elif entry_clean == "COMMAND:RESUME":
                self.transition_state(AuditState.INGESTING)
                continue
            elif entry_clean == "COMMAND:STOP":
                print("[SYSTEM SENTINEL] Stop command received. Terminating ingestion.")
                break

            # Process payload only when engine is in INGESTING state
            if self.current_state != AuditState.INGESTING:
                print(f"[SKIPPED ENTRY] Engine state is '{self.current_state}'. Record ignored: {entry_clean}")
                continue

            try:
                timestamp, txn_id, amount, status_flag = self.parse_transaction_string(entry_clean)

                # Algorithmic Match Logic
                is_anomaly = status_flag in ["SUSPECT", "FAILED"] or abs(amount) >= self.variance_threshold

                record = {
                    "timestamp": timestamp,
                    "txn_id": txn_id,
                    "amount": amount,
                    "status_flag": status_flag,
                    "is_anomaly": is_anomaly
                }

                self.reconciled_ledger.append(record)
                self.processed_count += 1

                if is_anomaly:
                    self.flagged_audit_trail.append(record)
                    print(f"[AUDIT ALERT] Anomaly detected in {txn_id}: ${amount:.2f} [{status_flag}]")

            except ValueError as err:
                print(f"[PARSING ERROR] {err}")

        self.transition_state(AuditState.COMPLETED)
        return self.generate_summary()

    def generate_summary(self) -> Dict[str, Any]:
        """Calculates ledger metrics and returns structured audit output."""
        total_volume = sum(item["amount"] for item in self.reconciled_ledger)
        flagged_volume = sum(item["amount"] for item in self.flagged_audit_trail)

        return {
            "total_processed": self.processed_count,
            "total_flagged": len(self.flagged_audit_trail),
            "total_volume_usd": round(total_volume, 2),
            "flagged_volume_usd": round(flagged_volume, 2),
            "engine_final_state": self.current_state
        }


# ------------------------------------------------------------------------------
# PRODUCTION EXECUTION ENTRY POINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    raw_audit_stream = [
        "2026-09-10 10:00:01 | TXN_1001 | 150.50 | [APPROVED]",
        "2026-09-10 10:01:23 | TXN_1002 | -750.00 | [SUSPECT]",
        "COMMAND:PAUSE",
        "2026-09-10 10:02:00 | TXN_1003 | 200.00 | [APPROVED]",  # Ignored due to state
        "COMMAND:RESUME",
        "2026-09-10 10:03:12 | TXN_1004 | 1250.00 | [APPROVED]",  # Flagged due to threshold
        "2026-09-10 10:04:45 | INVALID_LOG_STRING_WITHOUT_DELIMITERS",
        "2026-09-10 10:05:00 | TXN_1005 | 45.10 | [FAILED]",
        "COMMAND:STOP",
        "2026-09-10 10:06:00 | TXN_1006 | 99.00 | [APPROVED]"  # Ignored after stop
    ]

    print("=== INITIALIZING FINANCIAL RECONCILIATION ENGINE ===")
    engine = TransactionAuditEngine(variance_threshold=500.00)
    summary = engine.process_stream(raw_audit_stream)

    print("\n=== FINAL AUDIT RECONCILIATION REPORT ===")
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")