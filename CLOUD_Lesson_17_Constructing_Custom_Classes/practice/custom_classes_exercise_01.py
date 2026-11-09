"""
Lesson 17: Constructing Custom Classes, Initializer (__init__), Methods, Class Attributes
File: practice/custom_classes_exercise_01.py

This exercise demonstrates:
1. Defining a custom class blueprint.
2. Initializing instance attributes using __init__ and self.
3. Class-level vs. instance-level attributes.
4. Defining instance methods to read and modify instance state.
"""

class ClientAccount:
    # Class Attribute: Shared across all instances of ClientAccount
    organization_name = "Vizione Labs Enterprise"

    def __init__(self, client_id: str, client_name: str, initial_balance: float):
        """
        Initializer method executed automatically upon object creation.
        Binds specific dynamic state to the newly instantiated object via 'self'.
        """
        self.client_id = client_id
        self.client_name = client_name
        self.account_balance = initial_balance
        self.is_active = True

    def record_deposit(self, amount: float) -> float:
        """
        Instance Method: Mutates the account_balance instance attribute.
        """
        if amount <= 0:
            print(f"[{self.client_id}] Deposit failed: Amount must be positive.")
            return self.account_balance

        self.account_balance += amount
        print(f"[{self.client_id}] Deposited: ${amount:.2f} | New Balance: ${self.account_balance:.2f}")
        return self.account_balance

    def process_withdrawal(self, amount: float) -> bool:
        """
        Instance Method: Validates and updates instance balance upon withdrawal.
        """
        if amount > self.account_balance:
            print(f"[{self.client_id}] Withdrawal rejected: Insufficient funds.")
            return False

        self.account_balance -= amount
        print(f"[{self.client_id}] Withdrew: ${amount:.2f} | Remaining Balance: ${self.account_balance:.2f}")
        return True

    def generate_account_summary(self) -> str:
        """
        Instance Method: Formats and returns a state summary string.
        """
        status = "ACTIVE" if self.is_active else "INACTIVE"
        summary = (
            f"--- Client Summary [{self.organization_name}] ---\n"
            f"ID: {self.client_id} | Name: {self.client_name}\n"
            f"Status: {status} | Balance: ${self.account_balance:.2f}"
        )
        return summary


# --- Practice Execution & State Inspection ---
if __name__ == "__main__":
    print("=== Constructing Custom Classes Practice ===")

    # Instantiating two isolated object instances from the ClientAccount blueprint
    client_01 = ClientAccount(client_id="CL-101", client_name="Apex Global", initial_balance=5000.0)
    client_02 = ClientAccount(client_id="CL-102", client_name="Nexus Technologies", initial_balance=1200.0)

    # Inspecting initial instance states and shared class attribute
    print(f"\nCreated client_01: {client_01.client_name} (ID: {client_01.client_id})")
    print(f"Created client_02: {client_02.client_name} (ID: {client_02.client_id})")
    print(f"Shared Organization (Class Attribute): {ClientAccount.organization_name}")

    # Invoking instance methods on client_01
    print("\n--- Transactions for client_01 ---")
    client_01.record_deposit(1500.0)
    client_01.process_withdrawal(2000.0)

    # Invoking instance methods on client_02
    print("\n--- Transactions for client_02 ---")
    client_02.process_withdrawal(1500.0)  # Should trigger insufficient funds check
    client_02.record_deposit(800.0)

    # Displaying state summaries for both instances
    print("\n" + client_01.generate_account_summary())
    print("\n" + client_02.generate_account_summary())