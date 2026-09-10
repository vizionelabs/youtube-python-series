from typing import Dict, List, Tuple


class WorkOrderStateTracker:
    """
    Tracks and validates state transitions for wood floor restoration job orders.
    Processes stream logs to ensure sequential execution of job status updates.
    """

    VALID_TRANSITIONS: Dict[str, List[str]] = {
        "PENDING": ["SCHEDULED", "CANCELLED"],
        "SCHEDULED": ["IN_PROGRESS", "CANCELLED"],
        "IN_PROGRESS": ["CALAFETACAO_COMPLETED", "SANDING_COMPLETED", "HALTED"],
        "CALAFETACAO_COMPLETED": ["SANDING_COMPLETED", "HALTED"],
        "SANDING_COMPLETED": ["VARNISH_APPLIED", "HALTED"],
        "VARNISH_APPLIED": ["COMPLETED", "INSPECTION_FAILED"],
        "INSPECTION_FAILED": ["VARNISH_APPLIED", "HALTED"],
        "HALTED": ["IN_PROGRESS", "CANCELLED"],
        "COMPLETED": [],
        "CANCELLED": []
    }

    def __init__(self, initial_state: str = "PENDING") -> None:
        self.current_state: str = initial_state
        self.history: List[Tuple[str, str]] = [("INITIALIZATION", initial_state)]

    def transition_to(self, new_state: str, timestamp: str) -> bool:
        """
        Validates and executes a state transition. Returns True if valid, False otherwise.
        """
        allowed_next_states: List[str] = self.VALID_TRANSITIONS.get(self.current_state, [])

        if new_state in allowed_next_states:
            self.current_state = new_state
            self.history.append((timestamp, new_state))
            return True
        else:
            return False

    def get_audit_trail(self) -> List[Tuple[str, str]]:
        """Returns the full history of recorded state updates."""
        return self.history