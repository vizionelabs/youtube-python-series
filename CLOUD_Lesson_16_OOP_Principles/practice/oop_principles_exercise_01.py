# ==============================================================================
# VIZIONE LABS — PYTHON: BUILD REAL PROJECTS
# TRACK A: LESSON 16 (practice/oop_principles_exercise_01.py)
# TOPIC: Object-Oriented Programming (OOP) Principles & Attribute Instantiation
# ==============================================================================

class CoreServerNode:
    """
    Represents an isolated server node within a infrastructure monitoring framework.
    Serves as a blueprint for creating independent server instances with dynamic states.
    """
    def __init__(self, hostname: str, ip_address: str, initial_cpu_load: float):
        # Attribute Instantiation: Assigning instance-specific state variables
        self.hostname = hostname
        self.ip_address = ip_address
        self.cpu_load_percent = initial_cpu_load
        self.is_active = True

    def update_cpu_load(self, new_load: float) -> None:
        """
        Updates the CPU load percentage for this specific server instance.
        """
        self.cpu_load_percent = new_load
        print(f"[{self.hostname}] CPU load updated to {self.cpu_load_percent}%")

    def display_status(self) -> None:
        """
        Prints the operational health metrics of the server node.
        """
        status_str = "ACTIVE" if self.is_active else "INACTIVE"
        print(f"Node: {self.hostname} | IP: {self.ip_address} | Status: {status_str} | Load: {self.cpu_load_percent}%")


# --- RUNTIME EXECUTION & INSTANTIATION ---
if __name__ == "__main__":
    print("=== VIZIONE LABS: OOP PRINCIPLES PRACTICE ===\n")

    # Instantiating server node objects from the CoreServerNode class blueprint
    server_01 = CoreServerNode(hostname="app-srv-01", ip_address="192.168.1.10", initial_cpu_load=24.5)
    server_02 = CoreServerNode(hostname="db-srv-01", ip_address="192.168.1.50", initial_cpu_load=78.2)

    # Inspecting distinct dynamic states
    server_01.display_status()
    server_02.display_status()

    print("\n--- Updating Server States ---")
    # Modifying state on server_01 without affecting server_02
    server_01.update_cpu_load(45.0)

    # Verifying object state isolation
    print("\n--- Verifying Encapsulation & State Isolation ---")
    server_01.display_status()
    server_02.display_status()