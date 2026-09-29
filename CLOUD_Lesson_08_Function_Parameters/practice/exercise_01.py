# practice/exercise_01.py
# ==============================================================================
# VIZIONE LABS — PYTHON AUTOMATION CURRICULUM
# Lesson 08: Function Parameters, Keyword Arguments & Positional Mapping
# File: practice/exercise_01.py
# ==============================================================================

# 1. Defining a function with multiple parameters
def format_user_welcome(first_name, last_name, user_role, status_flag):
    """
    Formats a user greeting using exact positional input mapping.
    """
    greeting = f"User: {first_name} {last_name} | Role: {user_role} | Active: {status_flag}"
    return greeting


# 2. Invoking function using strict Positional Arguments (Order Sensitivity)
print("--- 1. Positional Arguments Execution ---")
# Arguments are assigned strictly in sequence:
# first_name="Lucas", last_name="Quaia", user_role="Admin", status_flag=True
pos_message = format_user_welcome("Lucas", "Quaia", "Admin", True)
print(pos_message)

# Positional Error Demonstration (Swapping argument order changes execution logic)
mismatched_message = format_user_welcome("Admin", "Lucas", True, "Quaia")
print(f"Mismatched Output: {mismatched_message}\n")


# 3. Invoking function using Keyword Arguments (Explicit Binding)
print("--- 2. Keyword Arguments Execution ---")
# Explicitly naming parameters removes sequence dependency
kw_message_1 = format_user_welcome(
    first_name="Lucas",
    last_name="Quaia",
    user_role="Developer",
    status_flag=True
)

# Order can be changed safely when explicitly using parameter keywords
kw_message_2 = format_user_welcome(
    status_flag=True,
    user_role="Architect",
    last_name="Quaia",
    first_name="Lucas"
)

print(f"Standard Keyword Binding: {kw_message_1}")
print(f"Reordered Keyword Binding: {kw_message_2}\n")


# 4. Combining Positional and Keyword Arguments
print("--- 3. Mixed Argument Execution ---")
# Rule: Positional arguments MUST come before any keyword arguments
mixed_message = format_user_welcome("Lucas", "Quaia", status_flag=True, user_role="Lead")
print(mixed_message)


# 5. Functions with Default Parameter Values
def generate_system_alert(message, alert_type="INFO", send_email=False):
    """
    Generates a formatted alert, utilizing default values for optional parameters.
    """
    alert_output = f"[{alert_type}] {message} (Email Dispatch: {send_email})"
    return alert_output


print("\n--- 4. Default Parameter Values Execution ---")
# Relying on default parameters (alert_type="INFO", send_email=False)
default_alert = generate_system_alert("Database connection established.")
print(default_alert)

# Overriding default parameters using keyword arguments
custom_alert = generate_system_alert(
    message="Unauthorized access attempt detected!",
    alert_type="CRITICAL",
    send_email=True
)
print(custom_alert)