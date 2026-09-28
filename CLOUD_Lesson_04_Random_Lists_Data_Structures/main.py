"""
Vizione Labs — Track A: Python: Build Real Projects
Lesson 04: Randomization Modules, Python Lists, Data Structures, Index Errors
File: main.py

Enterprise System: Vizione Labs Automated Cloud Resource & Worker Dispatcher

Objective:
Demonstrate enterprise production application of random sampling, list mutations,
dynamic payload balancing, index safety guards, and custom data structure mapping
for automated cloud node provisioning.
"""

import random
import sys


def build_initial_cluster_pool() -> list:
    """
    Instantiates and returns the primary sequence of available compute nodes.

    Returns:
        list: Sequence of initial active node identifiers.
    """
    return [
        "node-us-east-01",
        "node-us-east-02",
        "node-eu-west-01",
        "node-sa-east-01"
    ]


def provision_expansion_nodes(cluster_pool: list, new_nodes: list) -> list:
    """
    Mutates the cluster pool sequence by expanding it with new capacity.

    Args:
        cluster_pool (list): Active node collection.
        new_nodes (list): Additional nodes to register.

    Returns:
        list: Updated cluster pool reference.
    """
    # Append a dedicated backup node individually
    cluster_pool.append("node-backup-01")

    # Extend cluster pool with additional regional worker nodes
    cluster_pool.extend(new_nodes)
    return cluster_pool


def select_dispatch_target(cluster_pool: list) -> str:
    """
    Selects a target compute node pseudo-randomly using standard library choice.

    Args:
        cluster_pool (list): Sequence of candidate compute nodes.

    Returns:
        str: Selected node identifier.
    """
    return random.choice(cluster_pool)


def safe_access_node_by_index(cluster_pool: list, target_index: int) -> str:
    """
    Safely retrieves a node by positional index with boundary protection
    to prevent runtime IndexError exceptions.

    Args:
        cluster_pool (list): Sequence of node identifiers.
        target_index (int): Positional index requested.

    Returns:
        str: Node identifier or fallback boundary alert message.
    """
    pool_length = len(cluster_pool)

    # Boundary guard rule: valid index range is [-pool_length, pool_length - 1]
    if -pool_length <= target_index < pool_length:
        return cluster_pool[target_index]
    else:
        return f"[OUT OF BOUNDS GUARD] Index {target_index} is invalid for cluster size {pool_length}."


def main():
    print("==================================================================")
    print("      VIZIONE LABS: AUTOMATED CLOUD RESOURCE DISPATCHER           ")
    print("==================================================================")

    # Step 1: Initialize Core Cluster Nodes
    active_nodes = build_initial_cluster_pool()
    print(f"\n[INITIALIZATION] Active Cluster Pool ({len(active_nodes)} nodes):")
    for idx, node in enumerate(active_nodes):
        print(f"  -> Index [{idx}]: {node}")

    # Step 2: Dynamically Expand Capacity (.append & .extend)
    expansion_nodes = ["node-ap-southeast-01", "node-us-west-01"]
    active_nodes = provision_expansion_nodes(active_nodes, expansion_nodes)
    print(f"\n[EXPANSION] Updated Cluster Pool after provisioning ({len(active_nodes)} nodes):")
    for idx, node in enumerate(active_nodes):
        print(f"  -> Index [{idx}]: {node}")

    # Step 3: Pseudo-Random Task Dispatching
    print("\n[DISPATCHER] Executing dynamic workload distribution...")
    workload_tasks = ["AI Model Training", "Database Indexing", "Video Rendering Pipeline"]

    for task in workload_tasks:
        selected_node = select_dispatch_target(active_nodes)
        load_score = random.randint(15, 98)  # Random CPU load metric simulation
        print(f"  [TASK ASSIGNED] '{task}' -> Assigned to {selected_node} (Simulated Load: {load_score}%)")

    # Step 4: Positional Indexing & Boundary Safety Verification
    print("\n[INDEX SAFETY CHECK] Testing direct positional sequence access:")

    # Valid Access Scenarios
    first_node = safe_access_node_by_index(active_nodes, 0)
    last_node = safe_access_node_by_index(active_nodes, -1)
    print(f"  -> Primary Node [Index 0]: {first_node}")
    print(f"  -> Failover Node [Index -1]: {last_node}")

    # Out of Bounds Boundary Test (Intentionally requesting invalid index)
    invalid_index = len(active_nodes) + 5
    boundary_result = safe_access_node_by_index(active_nodes, invalid_index)
    print(f"  -> Boundary Test [Index {invalid_index}]: {boundary_result}")

    print("\n[SUCCESS] Resource dispatching pipeline executed cleanly.")


if __name__ == "__main__":
    main()