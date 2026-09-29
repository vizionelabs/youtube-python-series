# practice/exercise_01.py

# ==============================================================================
# LESSON 09: DICTIONARIES & KEY-VALUE MANIPULATION (FUNDAMENTALS)
# ==============================================================================

# 1. Dictionary Creation & Memory Structure
# Dictionaries map unique keys to values using curly braces {} and key: value pairs.
service_ticket = {
    "ticket_id": "TCK-8821",
    "client": "Vizione Corp",
    "status": "OPEN",
    "priority": "HIGH",
    "hours_logged": 12.5
}

print("--- Initial Service Ticket ---")
print(service_ticket)


# 2. Accessing Dictionary Values
# Direct key access using [] brackets:
current_status = service_ticket["status"]
print(f"\nDirect Access - Ticket Status: {current_status}")

# Safe access using .get() to avoid KeyError if key doesn't exist:
assigned_agent = service_ticket.get("assigned_agent", "Unassigned")
print(f"Safe Access (.get) - Assigned Agent: {assigned_agent}")


# 3. Dictionary Mutations: Updating and Adding Pairs
# Updating an existing key's value:
service_ticket["status"] = "IN_PROGRESS"

# Adding a new key-value pair:
service_ticket["lead_engineer"] = "Lucas"

print("\n--- After Mutation (Updated Status & Added Engineer) ---")
print(service_ticket)


# 4. Removing Key-Value Pairs
# Removing a pair with pop() and retrieving its value:
removed_priority = service_ticket.pop("priority")
print(f"\nRemoved Priority Level: {removed_priority}")

# Removing using the 'del' statement:
del service_ticket["hours_logged"]

print("--- After Key Deletions ---")
print(service_ticket)


# 5. Iterating Through Dictionaries
print("\n--- Iterating Over Keys ---")
for key in service_ticket.keys():
    print(f"Key: {key}")

print("\n--- Iterating Over Values ---")
for value in service_ticket.values():
    print(f"Value: {value}")

print("\n--- Iterating Over Key-Value Pairs (.items()) ---")
for key, value in service_ticket.items():
    print(f"{key}: {value}")


# 6. Nested Data Structures
# Dictionaries can contain lists, and lists can contain dictionaries.
project_data = {
    "project_name": "Vizione SaaS Portal",
    "team_members": ["Lucas", "Sarah", "Alex"],
    "modules": [
        {"name": "Auth", "status": "Completed"},
        {"name": "Billing", "status": "In Development"}
    ]
}

print("\n--- Accessing Nested Data ---")
# Accessing a list element inside a dictionary:
first_member = project_data["team_members"][0]
print(f"First Team Member: {first_member}")

# Accessing a value inside a dictionary nested within a list:
second_module_status = project_data["modules"][1]["status"]
print(f"Second Module Status: {second_module_status}")