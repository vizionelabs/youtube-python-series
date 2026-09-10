from state_tracker import WorkOrderStateTracker


def process_service_log_stream(log_events: list[str]) -> dict[str, WorkOrderStateTracker]:
    """
    Parses dynamic string log streams and maintains state machines for active job orders.
    """
    active_jobs: dict[str, WorkOrderStateTracker] = {}

    for event in log_events:
        # String matching & log parsing (Format: "TIMESTAMP|JOB_ID|TARGET_STATE")
        parts = event.split("|")
        if len(parts) != 3:
            print(f"[LOG ERROR] Malformed event string skipped: {event}")
            continue

        timestamp, job_id, target_state = parts[0].strip(), parts[1].strip(), parts[2].strip()

        # Initialize state machine if new job_id is detected
        if job_id not in active_jobs:
            active_jobs[job_id] = WorkOrderStateTracker(initial_state="PENDING")

        tracker = active_jobs[job_id]
        success = tracker.transition_to(new_state=target_state, timestamp=timestamp)

        if not success:
            print(f"[INVALID TRANSITION] Job {job_id} cannot move from {tracker.current_state} to {target_state} at {timestamp}")

    return active_jobs


if __name__ == "__main__":
    # Simulated incoming event stream from field operators
    raw_log_stream = [
        "2026-09-09 08:00 | JOB-101 | SCHEDULED",
        "2026-09-09 08:30 | JOB-102 | SCHEDULED",
        "2026-09-09 09:15 | JOB-101 | IN_PROGRESS",
        "2026-09-09 10:00 | JOB-101 | VARNISH_APPLIED",  # Invalid transition (Skipped SANDING)
        "2026-09-09 10:30 | JOB-101 | CALAFETACAO_COMPLETED",
        "2026-09-09 12:00 | JOB-101 | SANDING_COMPLETED",
        "2026-09-09 14:30 | JOB-101 | VARNISH_APPLIED",
        "2026-09-09 16:00 | JOB-101 | COMPLETED"
    ]

    print("--- STARTING AUTOMATED LOG AUDIT STREAM PROCESSING ---")
    processed_jobs = process_service_log_stream(raw_log_stream)

    print("\n--- FINAL WORK ORDER AUDIT TRAILS ---")
    for job_id, tracker in processed_jobs.items():
        print(f"\nAudit History for {job_id} (Final State: {tracker.current_state}):")
        for entry in tracker.get_audit_trail():
            print(f"  [{entry[0]}] -> {entry[1]}")