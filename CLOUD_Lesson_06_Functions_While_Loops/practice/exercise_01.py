# practice/exercise_01.py

def format_service_log(agent_name: str, task_count: int) -> str:
    """Format an agent operational activity log line."""
    log_entry = f"Agent: {agent_name} | Tasks Completed: {task_count}"
    return log_entry


def evaluate_performance(task_count: int) -> str:
    """Evaluate performance tier based on completed tasks."""
    if task_count >= 10:
        status = "OPTIMAL"
    elif task_count >= 5:
        status = "MODERATE"
    else:
        status = "LOW_OUTPUT"
    return status


def run_interactive_session():
    """Run an interactive console session tracking agent tasks using a while loop."""
    print("=== Vizione Labs Agent Activity Tracker ===")

    session_active = True
    session_count = 0

    while session_active:
        user_input = input("\nEnter agent name (or type 'exit' to stop): ").strip()

        if user_input.lower() == "exit":
            print("\nShutting down activity tracker...")
            session_active = False
        else:
            raw_tasks = input(f"Enter tasks completed for {user_input}: ").strip()

            if raw_tasks.isdigit():
                tasks = int(raw_tasks)
                log_msg = format_service_log(user_input, tasks)
                tier = evaluate_performance(tasks)

                session_count += 1
                print(f"[LOG #{session_count}] {log_msg} | Status Tier: {tier}")
            else:
                print("[ERROR] Invalid task count. Please enter a numerical integer.")


if __name__ == "__main__":
    run_interactive_session()