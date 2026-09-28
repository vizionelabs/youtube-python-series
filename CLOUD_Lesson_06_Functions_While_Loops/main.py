# main.py
from practice.exercise_01 import format_service_log, evaluate_performance


def initialize_agent_registry() -> dict:
    """Initialize default active worker nodes and their completed tasks."""
    return {
        "alpha_node": 12,
        "beta_node": 4,
        "gamma_node": 8,
        "delta_node": 0
    }


def process_agent_batch(agent_registry: dict) -> list:
    """Iterate over active nodes, format activity logs, and evaluate status tiers."""
    batch_summary = []
    for agent_name, tasks in agent_registry.items():
        log_entry = format_service_log(agent_name, tasks)
        tier = evaluate_performance(tasks)
        batch_summary.append({
            "agent": agent_name,
            "tasks": tasks,
            "log": log_entry,
            "status_tier": tier
        })
    return batch_summary


def display_batch_report(summary_list: list) -> None:
    """Print formatted operational summary report for all registered agents."""
    print("\n" + "=" * 60)
    print("      VIZIONE LABS - INFRASTRUCTURE WORKER BATCH REPORT      ")
    print("=" * 60)

    for item in summary_list:
        print(f"[{item['status_tier']}] {item['log']}")

    print("=" * 60)


def add_new_agent(agent_registry: dict) -> bool:
    """Interactively prompt user to add a new worker agent node to registry."""
    print("\n--- Register New Worker Node ---")
    agent_name = input("Enter worker node identifier (or type 'cancel'): ").strip()

    if agent_name.lower() == 'cancel' or not agent_name:
        print("Registration canceled.")
        return False

    raw_tasks = input(f"Enter completed task count for '{agent_name}': ").strip()

    if raw_tasks.isdigit():
        tasks = int(raw_tasks)
        agent_registry[agent_name] = tasks
        print(f"[SUCCESS] Node '{agent_name}' registered with {tasks} completed tasks.")
        return True
    else:
        print("[ERROR] Invalid task count. Must be a non-negative integer.")
        return False


def run_control_center() -> None:
    """Main administrative execution loop controlling Vizione Labs agent workflow."""
    agent_registry = initialize_agent_registry()
    system_running = True

    while system_running:
        print("\n=== VIZIONE LABS WORKER CONTROL CENTER ===")
        print("1. View Current Batch Performance Report")
        print("2. Register New Worker Node")
        print("3. Shutdown Control Center")

        choice = input("\nSelect operational option (1-3): ").strip()

        if choice == "1":
            summary = process_agent_batch(agent_registry)
            display_batch_report(summary)
        elif choice == "2":
            add_new_agent(agent_registry)
        elif choice == "3":
            print("\nShutting down Vizione Labs Control Center... All session logs saved.")
            system_running = False
        else:
            print("[ERROR] Invalid choice selected. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    run_control_center()