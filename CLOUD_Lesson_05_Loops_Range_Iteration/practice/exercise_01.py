"""
Vizione Labs — Fundamental Practice Script
Lesson 05: Loops, Range Function, Iteration Logic, and Execution Flow

This script demonstrates fundamental iteration patterns in Python:
1. Iterating over list elements using a basic 'for' loop.
2. Generating sequence boundaries using range(start, stop, step).
3. Accumulating state variables across loop cycles.
4. Applying dynamic condition checks inside iterative blocks.
"""

# -----------------------------------------------------------------------------
# Part 1: Iterating over a List
# -----------------------------------------------------------------------------
servers = ["web-node-01", "db-node-01", "cache-node-01", "queue-node-01"]

print("--- 1. Iterating Over Server Names ---")
for server in servers:
    print(f"Checking status for: {server}")

# -----------------------------------------------------------------------------
# Part 2: Generating Numeric Sequences with range()
# -----------------------------------------------------------------------------
print("\n--- 2. Range Sequences (Default, Custom Start, and Step) ---")

# Standard range (0 to N-1)
print("Standard range(5):")
for count in range(5):
    print(f"Cycle count: {count}")

# Custom range with start and stop (start to stop-1)
print("\nCustom range(1, 6):")
for step_num in range(1, 6):
    print(f"Step {step_num} complete.")

# Range with step parameter (start to stop-1 by step increment)
print("\nStepped range(10, 50, 10):")
for memory_tier in range(10, 50, 10):
    print(f"Allocating {memory_tier}GB RAM allocation block...")

# -----------------------------------------------------------------------------
# Part 3: State Accumulation Across Iterations
# -----------------------------------------------------------------------------
print("\n--- 3. Variable Accumulation Inside Loops ---")
cpu_load_percentages = [12.5, 45.0, 78.2, 33.1, 89.4]
total_load = 0.0

for load in cpu_load_percentages:
    total_load += load
    print(f"Added load: {load}% | Current Running Total: {total_load:.1f}%")

average_load = total_load / len(cpu_load_percentages)
print(f"\nAverage System Load: {average_load:.2f}%")

# -----------------------------------------------------------------------------
# Part 4: Conditionals Inside Loops
# -----------------------------------------------------------------------------
print("\n--- 4. Target Filtering and Threshold Inspection ---")
latency_records_ms = [45, 120, 310, 85, 450, 95]
high_latency_threshold_ms = 200

for latency in latency_records_ms:
    if latency > high_latency_threshold_ms:
        print(f"[ALERT] High latency detected: {latency}ms (Exceeds {high_latency_threshold_ms}ms)")
    else:
        print(f"[OK] Normal response time: {latency}ms")