"""
Vizione Labs - Enterprise Production Systems
Lesson 04: Dynamic Client Dispatching, Random Audit & Multi-Tier Load Balancer

This engine routes incoming enterprise clients across operational nodes,
executes random compliance audits, and dynamically updates system state
with complete index safety and array mutation management.
"""

import random
from typing import List, Dict, Union, Optional


class VizioneLabsDispatcher:
    """
    Enterprise dispatch engine that manages client queues, load balances node routing,
    and conducts stochastic quality control audits on Vizione Labs pipelines.
    """

    def __init__(self, operational_nodes: List[str]) -> None:
        """
        Initializes the dispatcher with a validated list of operational processing nodes.

        :param operational_nodes: Non-empty sequence of server/worker identifiers.
        """
        if not operational_nodes:
            raise ValueError("Dispatcher initialization failed: Node sequence cannot be empty.")

        self.nodes: List[str] = operational_nodes
        self.active_clients: List[Dict[str, Union[str, int]]] = []
        self.audit_log: List[Dict[str, Union[str, float]]] = []

    def ingest_client(self, client_id: str, priority_level: int) -> Dict[str, Union[str, int]]:
        """
        Ingests a new Vizione Labs client into the active queue.

        :param client_id: Unique string identifier for the client payload.
        :param priority_level: Numerical weight (1-10) for routing priority.
        :return: Dictionary representation of the registered client record.
        """
        client_record: Dict[str, Union[str, int]] = {
            "client_id": client_id,
            "priority": priority_level,
            "status": "Queued"
        }
        self.active_clients.append(client_record)
        return client_record

    def assign_node_load_balanced(self) -> List[Dict[str, Union[str, int]]]:
        """
        Distributes all active clients across operational nodes using round-robin index access
        guaranteed against IndexError exceptions through modular arithmetic.

        :return: Mutated list of active client records with assigned processing nodes.
        """
        total_nodes = len(self.nodes)

        for index, client in enumerate(self.active_clients):
            # Index Safety: Using modulo operator (%) ensures safe cyclic index selection
            node_index = index % total_nodes
            assigned_node = self.nodes[node_index]
            client["assigned_node"] = assigned_node
            client["status"] = "Dispatched"

        return self.active_clients

    def trigger_stochastic_audit(self) -> Optional[Dict[str, Union[str, float]]]:
        """
        Executes a random sample audit across dispatched clients.

        :return: Audit record dictionary or None if no active clients exist.
        """
        if not self.active_clients:
            print("[AUDIT ENGINE WARNING] No active clients available for audit.")
            return None

        # Stochastic selection using random.choice to pull a uniform random element
        sampled_client = random.choice(self.active_clients)

        # Generating audit metrics using random module float precision
        audit_score = round(random.uniform(85.0, 100.0), 2)

        audit_record: Dict[str, Union[str, float]] = {
            "client_id": str(sampled_client["client_id"]),
            "assigned_node": str(sampled_client.get("assigned_node", "Unassigned")),
            "audit_score": audit_score
        }

        self.audit_log.append(audit_record)
        return audit_record

    def reorder_priority_queue(self) -> List[Dict[str, Union[str, int]]]:
        """
        Shuffles the active queue order to simulate load redistribution across worker threads.
        """
        random.shuffle(self.active_clients)
        return self.active_clients


# ==============================================================================
# ENTERPRISE EXECUTION PIPELINE
# ==============================================================================

if __name__ == "__main__":
    print("==================================================================")
    print(" VIZIONE LABS: ENTERPRISE DISPATCH & AUDIT ENGINE INITIALIZING   ")
    print("==================================================================\n")

    # 1. Instantiate Dispatcher with Operational Server Nodes
    cluster_nodes = ["node-alpha-us-east", "node-beta-eu-central", "node-gamma-ap-south"]
    dispatcher = VizioneLabsDispatcher(operational_nodes=cluster_nodes)

    # 2. Ingest Enterprise Client Inflow
    clients_to_ingest = [
        ("VIZ-1001", 9),
        ("VIZ-1002", 5),
        ("VIZ-1003", 8),
        ("VIZ-1004", 3),
        ("VIZ-1005", 10),
    ]

    for cid, prio in clients_to_ingest:
        record = dispatcher.ingest_client(client_id=cid, priority_level=prio)
        print(f"[INGEST SUCCESS] Client Registered: {record['client_id']} | Priority: {record['priority']}")

    # 3. Execute Safe Load-Balanced Node Assignment
    print("\n--- Executing Cyclic Load Balancing ---")
    dispatched_queue = dispatcher.assign_node_load_balanced()
    for item in dispatched_queue:
        print(f"Client: {item['client_id']} -> Routed to: {item['assigned_node']} [{item['status']}]")

    # 4. Trigger Stochastic Quality Assurance Audit
    print("\n--- Executing Stochastic System Audit ---")
    audit_result = dispatcher.trigger_stochastic_audit()
    if audit_result:
        print(
            f"[AUDIT COMPLETED] Target: {audit_result['client_id']} | Node: {audit_result['assigned_node']} | Quality Score: {audit_result['audit_score']}%")

    print("\n==================================================================")
    print(" VIZIONE LABS: PIPELINE EXECUTION COMPLETED SUCCESSFULLY          ")
    print("==================================================================")