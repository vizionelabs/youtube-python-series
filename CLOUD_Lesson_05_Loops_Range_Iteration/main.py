"""
Vizione Labs — Production System Implementation
Lesson 05: Enterprise Infrastructure Node Auditor & Batch Rollout Engine

This script executes production-grade iteration logic across server clusters:
1. Iterating through multi-region cluster nodes to inspect resource utilization.
2. Calculating system-wide aggregated telemetry metrics using numeric iteration.
3. Executing sequential batch rolling updates using controlled step sequences.
4. Filtering nodes against strict health SLA thresholds to identify failing instances.
"""

import time

# -----------------------------------------------------------------------------
# Configuration & Cluster Telemetry Data
# -----------------------------------------------------------------------------
CLUSTER_NODES = [
    {"node_id": "us-east-node-01", "cpu_usage": 42.1, "memory_gb": 16, "status": "ONLINE"},
    {"node_id": "us-east-node-02", "cpu_usage": 88.5, "memory_gb": 32, "status": "CRITICAL"},
    {"node_id": "eu-west-node-01", "cpu_usage": 31.0, "memory_gb": 16, "status": "ONLINE"},
    {"node_id": "eu-west-node-02", "cpu_usage": 94.2, "memory_gb": 64, "status": "WARNING"},
    {"node_id": "ap-south-node-01", "cpu_usage": 15.8, "memory_gb": 16, "status": "ONLINE"},
]

CPU_WARN_THRESHOLD = 80.0
TOTAL_BATCH_STAGES = 3

print("=====================================================================")
print("  VIZIONE LABS — INFRASTRUCTURE CLUSTER AUDITOR & BATCH DEPLOYMENT  ")
print("=====================================================================")

# -----------------------------------------------------------------------------
# Stage 1: Iterative Cluster Telemetry Audit
# -----------------------------------------------------------------------------
print("\n[STAGE 1] Executing Node-by-Node Resource Audit...")

total_cpu_accumulated = 0.0
total_memory_allocated = 0
critical_node_count = 0

for node in CLUSTER_NODES:
    node_id = node["node_id"]
    cpu = node["cpu_usage"]
    ram = node["memory_gb"]
    status = node["status"]

    # Accumulate metrics across iteration cycles
    total_cpu_accumulated += cpu
    total_memory_allocated += ram

    # Threshold evaluation inside iteration
    if cpu >= CPU_WARN_THRESHOLD:
        critical_node_count += 1
        print(f"  [ALERT] {node_id:<18} | CPU: {cpu:>5.1f}% | RAM: {ram:>2}GB | STATUS: {status} (HIGH LOAD)")
    else:
        print(f"  [OK]    {node_id:<18} | CPU: {cpu:>5.1f}% | RAM: {ram:>2}GB | STATUS: {status}")

# -----------------------------------------------------------------------------
# Stage 2: System Aggregation & Metric Summary
# -----------------------------------------------------------------------------
print("\n[STAGE 2] Calculating Aggregated Cluster Metrics...")

node_count = len(CLUSTER_NODES)
average_cpu_load = total_cpu_accumulated / node_count

print(f"  Total Monitored Nodes   : {node_count}")
print(f"  Total RAM Provisioned  : {total_memory_allocated} GB")
print(f"  Cluster Average CPU    : {average_cpu_load:.2f}%")
print(f"  Nodes Exceeding Threshold: {critical_node_count}")

# -----------------------------------------------------------------------------
# Stage 3: Batch Deployment Pipeline Execution (using range)
# -----------------------------------------------------------------------------
print("\n[STAGE 3] Initiating Multi-Stage Rolling Deployment Sequence...")

for stage_index in range(1, TOTAL_BATCH_STAGES + 1):
    print(f"\n  >>> Deploying Batch Stage {stage_index}/{TOTAL_BATCH_STAGES}...")

    # Simulate processing subsets of nodes during deployment stages
    progress_percentage = (stage_index / TOTAL_BATCH_STAGES) * 100
    print(f"      Validation check in progress... {progress_percentage:.1f}% complete.")

    # Iterating step-by-step for health check simulation
    for retry_count in range(1, 4):
        print(f"      Ping check iteration {retry_count}/3... Pass.")

print("\n=====================================================================")
print("  [SUCCESS] Cluster audit completed. Batch deployment verified.       ")
print("=====================================================================")