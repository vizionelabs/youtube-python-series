"""
Vizione Labs Master Engine — Enterprise Platform
Lesson 17: Constructing Custom Classes, Initializer (__init__), Methods, Class Attributes
File: main.py

Production System: Client Account Operations & Fleet Licensing Controller
Demonstrates enterprise-grade application of custom class blueprints, dynamic state mutation,
class-level data tracking, and structured record evaluation across multi-tenant clients.
"""

import sys
from typing import Dict, List, Optional


class EnterpriseClientAccount:
    """
    Core Blueprint representing a tenant enterprise account within Vizione Labs Platform.
    Encapsulates client configuration, subscription state, licensing quotas, and billings.
    """
    # Class Attributes: Shared system metadata across all tenant instances
    platform_provider: str = "Vizione Labs Enterprise Engine"
    platform_version: str = "v2.4.0-Production"
    total_tenant_count: int = 0
    total_system_revenue: float = 0.0

    def __init__(self, tenant_id: str, company_name: str, base_tier: str, initial_credit: float):
        """
        Initializer method constructing a new EnterpriseClientAccount instance.
        """
        self.tenant_id: str = tenant_id
        self.company_name: str = company_name
        self.tier: str = base_tier.upper()
        self.account_balance: float = initial_credit
        self.allocated_api_licenses: int = 0
        self.is_active: bool = True
        self.transaction_history: List[Dict[str, float]] = []

        # Update global class-level telemetry metrics upon instantiation
        EnterpriseClientAccount.total_tenant_count += 1
        EnterpriseClientAccount.total_system_revenue += initial_credit

    def allocate_api_licenses(self, license_count: int, cost_per_license: float) -> bool:
        """
        Instance Method: Provisions operational API licenses, charging the account balance.
        """
        if not self.is_active:
            print(f"[REJECTED] Tenant {self.tenant_id} ({self.company_name}) is suspended.")
            return False

        total_cost = license_count * cost_per_license
        if self.account_balance < total_cost:
            print(f"[FAILED] Tenant {self.tenant_id}: Insufficient funds to allocate {license_count} licenses.")
            print(f"         Required: ${total_cost:.2f} | Available: ${self.account_balance:.2f}")
            return False

        self.account_balance -= total_cost
        self.allocated_api_licenses += license_count
        self.transaction_history.append({"action": "LICENSE_PROVISION", "amount": -total_cost})

        print(f"[SUCCESS] Tenant {self.tenant_id}: Provisioned {license_count} licenses.")
        print(f"         Debited: ${total_cost:.2f} | Remaining Balance: ${self.account_balance:.2f}")
        return True

    def deposit_platform_credits(self, amount: float) -> float:
        """
        Instance Method: Ingests billing credits into the tenant balance.
        """
        if amount <= 0:
            print(f"[REJECTED] Invalid deposit amount: ${amount:.2f}")
            return self.account_balance

        self.account_balance += amount
        EnterpriseClientAccount.total_system_revenue += amount
        self.transaction_history.append({"action": "CREDIT_DEPOSIT", "amount": amount})

        print(f"[SUCCESS] Tenant {self.tenant_id}: Credited ${amount:.2f}. New Balance: ${self.account_balance:.2f}")
        return self.account_balance

    def evaluate_tier_upgrade(self) -> str:
        """
        Instance Method: Evaluates account status and automatically upgrades service tiers based on volume.
        """
        if self.allocated_api_licenses >= 50 and self.tier != "ENTERPRISE":
            old_tier = self.tier
            self.tier = "ENTERPRISE"
            print(f"[TIER UPGRADE] Tenant {self.tenant_id} upgraded from {old_tier} -> ENTERPRISE.")
        elif self.allocated_api_licenses >= 20 and self.tier == "STARTER":
            old_tier = self.tier
            self.tier = "PRO"
            print(f"[TIER UPGRADE] Tenant {self.tenant_id} upgraded from {old_tier} -> PRO.")

        return self.tier

    def generate_telemetry_report(self) -> Dict[str, str]:
        """
        Instance Method: Compiles operational metrics for central telemetry dashboards.
        """
        return {
            "tenant_id": self.tenant_id,
            "company_name": self.company_name,
            "tier": self.tier,
            "balance": f"${self.account_balance:.2f}",
            "active_licenses": str(self.allocated_api_licenses),
            "status": "ACTIVE" if self.is_active else "SUSPENDED"
        }


class EnterpriseSystemController:
    """
    Controller Orchestrator: Manages collective fleet of tenant instances and system analytics.
    """

    def __init__(self):
        self.tenant_registry: Dict[str, EnterpriseClientAccount] = {}

    def register_tenant(self, account: EnterpriseClientAccount) -> None:
        """
        Registers an instance of EnterpriseClientAccount into central control registry.
        """
        self.tenant_registry[account.tenant_id] = account
        print(f"[REGISTRY] Registered Tenant ID: {account.tenant_id} ({account.company_name})")

    def execute_fleet_billing_cycle(self, maintenance_fee: float) -> None:
        """
        Iterates over registered tenant instances, deducting platform maintenance fees.
        """
        print(f"\n--- Executing Fleet Maintenance Cycle (Fee: ${maintenance_fee:.2f}) ---")
        for tenant_id, tenant in self.tenant_registry.items():
            if tenant.account_balance >= maintenance_fee:
                tenant.account_balance -= maintenance_fee
                tenant.transaction_history.append({"action": "MAINTENANCE_FEE", "amount": -maintenance_fee})
                print(f"[{tenant_id}] System fee deducted. Balance: ${tenant.account_balance:.2f}")
            else:
                tenant.is_active = False
                print(f"[{tenant_id}] Insufficient funds for system fee. Account SUSPENDED.")

    def render_platform_dashboard(self) -> None:
        """
        Prints high-level operational telemetry overview.
        """
        print("\n=================================================================")
        print(f"        VIZIONE LABS ENTERPRISE DASHBOARD - {EnterpriseClientAccount.platform_version}")
        print("=================================================================")
        print(f"Provider: {EnterpriseClientAccount.platform_provider}")
        print(f"Active Tenants Registered: {EnterpriseClientAccount.total_tenant_count}")
        print(f"Total Cumulative Revenue:  ${EnterpriseClientAccount.total_system_revenue:.2f}")
        print("-----------------------------------------------------------------")
        print("TENANT STATUS OVERVIEW:")

        for tenant in self.tenant_registry.values():
            report = tenant.generate_telemetry_report()
            print(
                f" ID: {report['tenant_id']} | Company: {report['company_name']:<20} | "
                f"Tier: {report['tier']:<10} | Balance: {report['balance']:<10} | "
                f"Licenses: {report['active_licenses']:<3} | Status: {report['status']}"
            )
        print("=================================================================\n")


# --- Main Production Execution Block ---
def main() -> None:
    print("Initializing Vizione Labs Client Operations Engine...\n")

    # Instantiate Controller
    controller = EnterpriseSystemController()

    # Create dynamic client instances using custom EnterpriseClientAccount class blueprint
    client_a = EnterpriseClientAccount("TEN-901", "Acme Cloud Logistics", "STARTER", 3500.0)
    client_b = EnterpriseClientAccount("TEN-902", "Cyberdyne Data Systems", "PRO", 12000.0)
    client_c = EnterpriseClientAccount("TEN-903", "Starlight Media", "STARTER", 800.0)

    # Register instances to central controller
    controller.register_tenant(client_a)
    controller.register_tenant(client_b)
    controller.register_tenant(client_c)

    # Perform operational transactions (State Mutations via Instance Methods)
    print("\n--- Processing API License Allocations ---")
    client_a.allocate_api_licenses(25, cost_per_license=100.0)  # Total $2500 -> Balance $1000
    client_b.allocate_api_licenses(60, cost_per_license=150.0)  # Total $9000 -> Balance $3000
    client_c.allocate_api_licenses(10, cost_per_license=100.0)  # Total $1000 -> Rejected (Balance $800)

    print("\n--- Processing Revenue Ingestion & Upgrades ---")
    client_a.deposit_platform_credits(2000.0)
    client_a.evaluate_tier_upgrade()
    client_b.evaluate_tier_upgrade()

    # Execute system-wide cycle
    controller.execute_fleet_billing_cycle(maintenance_fee: float = 900.0)

    # Render Telemetry Dashboard
    controller.render_platform_dashboard()


if __name__ == "__main__":
    main()