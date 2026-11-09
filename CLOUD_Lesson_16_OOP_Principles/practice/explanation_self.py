
# ==============================================================================
# VIZIONE LABS — TEACHING SCRIPT: DEMYSTIFYING FUNCTIONS VS. CLASSES & 'self'
# CONCEPT: The Pocket Calculator vs. The Master Paper Form & Clerk
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE STANDALONE FUNCTION (The Pocket Calculator)
# ------------------------------------------------------------------------------
# A standalone function is purely a calculation tool (like a pocket calculator).
# It receives temporary numbers in its parentheses, calculates a result, and
# the moment it finishes or turns off, it FORGETS everything from memory.
# It owns NO data and has NO permanent paper document. Thus, it needs NO 'self'.

def calculate_status_standalone(cpu_usage: float) -> str:
    if cpu_usage > 85.0:
        return "CRITICAL"
    return "HEALTHY"


# ------------------------------------------------------------------------------
# 2. THE CLASS & THE '__init__' CONSTRUCTOR (Printing & Filling the Paper Form)
# ------------------------------------------------------------------------------
class CoreServerNode:
    """
    CLASS BLUEPRINT: The master architectural blueprint for creating paper forms.
    """

    def __init__(self, hostname: str, cpu_usage: float, memory_usage: float):
        """
        DUNDER INIT (__init__): The Form-Printing & Initial Filling Method

        - 'self' : Represents THIS specific sheet of paper currently sitting on the desk.
        - hostname, cpu_usage, memory_usage : Temporary envelopes bringing external data.
        """

        # CREATING PERMANENT FORM FIELDS ON 'self':
        # We write: self.hostname = hostname
        # Meaning: On THIS paper form sheet ('self'), take the name printed on the box ('self.hostname')
        # and fill it with the data coming from the temporary incoming envelope ('hostname').

        self.hostname: str = hostname  # Permanent box 'hostname' filled with incoming data
        self.cpu_usage: float = cpu_usage  # Permanent box 'cpu_usage' filled with incoming data
        self.memory_usage: float = memory_usage  # Permanent box 'memory_usage' filled with incoming data

    # --------------------------------------------------------------------------
    # 3. CLASS METHODS & 'self' (The Clerk Reading the Filled Form)
    # --------------------------------------------------------------------------
    def evaluate_status(self) -> str:
        """
        EVALUATE_STATUS METHOD:

        - Why does parentheses contain ONLY 'self'?
          Because this method acts like a clerk holding a pocket calculator in one hand
          and grabbing THIS specific filled paper form ('self') in the other hand.

        - The clerk does NOT need new data passed in from outside because all the data
          he needs is ALREADY written inside the form fields on 'self' (self.cpu_usage).
        """
        # The clerk looks directly at the form in his hand ('self') and reads 'self.cpu_usage':
        if self.cpu_usage > 85.0 or self.memory_usage > 90.0:
            return f"[{self.hostname}] CRITICAL"
        return f"[{self.hostname}] HEALTHY"


# ==============================================================================
# RUNTIME EXECUTION IN MEMORY
# ==============================================================================

# Instantiating Form #1 (server_01) and Form #2 (server_02)
server_01 = CoreServerNode(hostname="app-srv-01", cpu_usage=92.5, memory_usage=45.0)
server_02 = CoreServerNode(hostname="db-srv-01", cpu_usage=12.0, memory_usage=30.0)

# Calling evaluate_status():
# Notice we pass NO parameters inside evaluate_status()!
# The clerk simply picks up Form #1 ('server_01') or Form #2 ('server_02') and evaluates it.
print(server_01.evaluate_status())  # Returns: [app-srv-01] CRITICAL
print(server_02.evaluate_status())  # Returns: [db-srv-01] HEALTHY