# ==============================================================================
# VIZIONE LABS — PYTHON: BUILD REAL PROJECTS
# TRACK A: LESSON 16 (main.py)
# TOPIC: Production Enterprise Infrastructure Health & Node Monitoring System
# ==============================================================================

import time
from typing import List, Dict, Any


class InfrastructureNode:
    """
    Enterprise blueprint representing an isolated compute node within a cloud infrastructure cluster.
    Encapsulates node telemetry, health states, and lifecycle operational methods.
    """

    def __init__(self, node_id: str, hostname: str, ip_address: str, region: str, cpu_threshold: float = 85.0):
        # Primary Instance Attributes
        self.node_id: str = node_id
        self.hostname: str = hostname
        self.ip_address: str = ip_address
        self.region: str = region
        self.cpu_threshold: float = cpu_threshold

        # Dynamic Operational Telemetry State
        self.cpu_usage_pct: float = 0.0
        self.memory_usage_pct: float = 0.0
        self.active_connections: int = 0
        self.is_healthy: bool = True
        self.is_active: bool = True

    def ingest_telemetry(self, cpu_pct: float, memory_pct: float, connections: int) -> None:
        """
        Updates node runtime telemetry and evaluates health status against policy thresholds.
        """
        self.cpu_usage_pct = cpu_pct
        self.memory_usage_pct = memory_pct
        self.active_connections = connections
        self._evaluate_health()

    def _evaluate_health(self) -> None:
        """
        Internal operational method to assess health flags based on active metrics.
        """
        if self.cpu_usage_pct > self.cpu_threshold or self.memory_usage_pct > 90.0:
            self.is_healthy = False
        else:
            self.is_healthy = True

    def execute_failover_drain(self) -> None:
        """
        Drains active connections and marks node inactive during emergency protocol execution.
        """
        print(f"[ACTION] Initializing failover connection drain on node: {self.hostname} ({self.ip_address})...")
        self.active_connections = 0
        self.is_active = False
        print(f"[SUCCESS] Node {self.hostname} safely drained and set to INACTIVE.")

    def get_status_report(self) -> Dict[str, Any]:
        """
        Returns a structured telemetry payload representing current node state.
        """
        return {
            "node_id": self.node_id,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "region": self.region,
            "cpu_usage": f"{self.cpu_usage_pct:.1f}%",
            "memory_usage": f"{self.memory_usage_pct:.1f}%",
            "connections": self.active_connections,
            "healthy": self.is_healthy,
            "status": "ONLINE" if self.is_active else "DRAINED"
        }


class ClusterManager:
    """
    Manager orchestration class responsible for registering infrastructure nodes,
    broadcasting telemetry updates, and triggering cluster health evaluations.
    """

    def __init__(self, cluster_name: str, environment: str):
        self.cluster_name: str = cluster_name
        self.environment: str = environment
        self.nodes: Dict[str, InfrastructureNode] = {}

    def register_node(self, node: InfrastructureNode) -> None:
        """
        Registers an instantiated InfrastructureNode into the cluster registry.
        """
        self.nodes[node.node_id] = node
        print(f"[REGISTRY] Node '{node.hostname}' registered in cluster '{self.cluster_name}'.")

    def process_telemetry_batch(self, telemetry_data: List[Dict[str, Any]]) -> None:
        """
        Ingests a batch telemetry payload and dispatches status updates to target nodes.
        """
        for item in telemetry_data:
            node_id = item.get("node_id")
            if node_id in self.nodes:
                target_node = self.nodes[node_id]
                target_node.ingest_telemetry(
                    cpu_pct=item.get("cpu_pct", 0.0),
                    memory_pct=item.get("memory_pct", 0.0),
                    connections=item.get("connections", 0)
                )

    def print_cluster_dashboard(self) -> None:
        """
        Outputs a formatted operational health dashboard for all monitored cluster nodes.
        """
        print(f"\n==================================================================")
        print(f" VIZIONE LABS INFRASTRUCTURE DASHBOARD — {self.cluster_name.upper()} ({self.environment.upper()})")
        print(f"==================================================================")
        print(
            f"{'NODE ID':<12} | {'HOSTNAME':<15} | {'CPU %':<8} | {'MEM %':<8} | {'CONN':<6} | {'HEALTH':<8} | {'STATUS':<8}")
        print("-" * 78)

        for node in self.nodes.values():
            report = node.get_status_report()
            health_str = "OK" if report["healthy"] else "CRITICAL"
            print(
                f"{report['node_id']:<12} | {report['hostname']:<15} | {report['cpu_usage']:<8} | {report['memory_usage']:<8} | {report['connections']:<6} | {health_str:<8} | {report['status']:<8}")
        print("=" * 78)

    def auto_remediate_unhealthy_nodes(self) -> None:
        """
        Scans cluster nodes and triggers failover connection drains on critical instances.
        """
        print("\n[ORCHESTRATOR] Running automated health scan and remediation protocol...")
        for node in self.nodes.values():
            if not node.is_healthy and node.is_active:
                print(f"[CRITICAL ALERT] Node {node.hostname} exceeded safe operating limits! Triggering failover...")
                node.execute_failover_drain()


# --- PRODUCTION EXECUTION & ORCHESTRATION ---
if __name__ == "__main__":
    print("=== VIZIONE LABS: ENTERPRISE INFRASTRUCTURE MONITORING ENGINE ===\n")

    # 1. Instantiate the Cluster Manager
    prod_cluster = ClusterManager(cluster_name="us-east-prod-01", environment="Production")

    # 2. Instantiate and Register Production Infrastructure Nodes
    node_a = InfrastructureNode(node_id="node-101", hostname="api-gateway-01", ip_address="10.0.1.10",
                                region="us-east-1a")
    node_b = InfrastructureNode(node_id="node-102", hostname="auth-service-01", ip_address="10.0.1.11",
                                region="us-east-1a")
    node_c = InfrastructureNode(node_id="node-103", hostname="worker-node-01", ip_address="10.0.1.12",
                                region="us-east-1b")

    prod_cluster.register_node(node_a)
    prod_cluster.register_node(node_b)
    prod_cluster.register_node(node_c)

    # 3. Simulate Incoming Telemetry Cycles
    print("\n--- Cycle 1: Ingesting Normal System Telemetry ---")
    telemetry_cycle_1 = [
        {"node_id": "node-101", "cpu_pct": 34.2, "memory_pct": 45.0, "connections": 1250},
        {"node_id": "node-102", "cpu_pct": 52.8, "memory_pct": 61.2, "connections": 840},
        {"node_id": "node-103", "cpu_pct": 21.0, "memory_pct": 30.5, "connections": 120}
    ]
    prod_cluster.process_telemetry_batch(telemetry_cycle_1)
    prod_cluster.print_cluster_dashboard()

    print("\n--- Cycle 2: Ingesting Spike Telemetry (High Load Event) ---")
    telemetry_cycle_2 = [
        {"node_id": "node-101", "cpu_pct": 42.0, "memory_pct": 48.0, "connections": 1400},
        {"node_id": "node-102", "cpu_pct": 94.5, "memory_pct": 88.0, "connections": 3100},  # CPU breach (>85%)
        {"node_id": "node-103", "cpu_pct": 25.0, "memory_pct": 32.0, "connections": 150}
    ]
    prod_cluster.process_telemetry_batch(telemetry_cycle_2)
    prod_cluster.print_cluster_dashboard()

    # 4. Automated Remediations
    prod_cluster.auto_remediate_unhealthy_nodes()

    # 5. Final Cluster Health Dashboard Verification
    print("\n--- Final Status Post-Remediation ---")
    prod_cluster.print_cluster_dashboard()