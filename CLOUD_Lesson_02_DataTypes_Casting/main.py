# main.py
"""
Vizione Labs — Python: Build Real Projects
Lesson 02: Production Enterprise Financial Calculation Engine

This enterprise script demonstrates:
1. Handling raw string inputs and applying explicit type casting safely.
2. Complex multi-step mathematical calculations (subtotals, discounts, taxes, unit allocations).
3. Legacy string formatting vs. Modern f-string interpolation.
4. Structuring clear, professional executive summaries for business production.
"""


def process_client_quote(
        raw_service_name: str,
        raw_hours_logged: str,
        raw_hourly_rate: str,
        raw_discount_percent: str,
        raw_tax_rate: str,
        raw_server_node_count: str
) -> None:
    """
    Parses raw client input data, casts values to appropriate numeric types,
    executes production financial logic, and outputs formatted quotes.
    """
    # --------------------------------------------------------------------------
    # 1. INPUT TYPE CASTING & SANITIZATION
    # --------------------------------------------------------------------------
    # Convert raw text inputs from API payloads or user forms into strict primitive types.
    service_name: str = raw_service_name.strip()
    hours_logged: int = int(raw_hours_logged)
    hourly_rate: float = float(raw_hourly_rate)
    discount_percent: float = float(raw_discount_percent)
    tax_rate: float = float(raw_tax_rate)
    server_nodes: int = int(raw_server_node_count)

    # --------------------------------------------------------------------------
    # 2. ENTERPRISE FINANCIAL CALCULATIONS
    # --------------------------------------------------------------------------
    # Base labor calculation
    subtotal: float = hours_logged * hourly_rate

    # Discount calculation: (subtotal * percentage) / 100
    discount_amount: float = (subtotal * discount_percent) / 100.0
    taxable_amount: float = subtotal - discount_amount

    # Tax calculation
    tax_amount: float = taxable_amount * tax_rate
    final_total: float = taxable_amount + tax_amount

    # Advanced division: Distributing cost across allocated compute infrastructure
    cost_per_server: float = final_total / server_nodes
    whole_server_share: int = int(final_total) // server_nodes  # Integer division
    unallocated_cents_remainder: float = final_total % server_nodes  # Modulus operator

    # --------------------------------------------------------------------------
    # 3. LEGACY STRING FORMATTING COMPARISON (HISTORICAL METHODS)
    # --------------------------------------------------------------------------
    # Old Method 1: String Concatenation (+) - Requires explicit str() casting
    legacy_concat_summary = (
            "Service: " + service_name + " | Total: $" + str(round(final_total, 2))
    )

    # Old Method 2: C-Style Positional Modulo Formatting (%)
    legacy_modulo_summary = (
            "Service: %s | Total: $%.2f" % (service_name, final_total)
    )

    # Old Method 3: str.format() Method (Python 2.7 / early Python 3)
    legacy_format_summary = (
        "Service: {} | Total: ${:.2f}".format(service_name, final_total)
    )

    # --------------------------------------------------------------------------
    # 4. MODERN F-STRING INTERPOLATION (ENTERPRISE STANDARD)
    # --------------------------------------------------------------------------
    # Clean, readable, inline expression formatting
    modern_fstring_quote = (
        f"======================================================================\n"
        f"                    VIZIONE LABS — CLIENT QUOTE                       \n"
        f"======================================================================\n"
        f"Service Rendered         : {service_name}\n"
        f"Labor Duration           : {hours_logged} hours @ ${hourly_rate:.2f}/hr\n"
        f"Gross Subtotal           : ${subtotal:.2f}\n"
        f"Discount Applied ({discount_percent:.0f}%)  : -${discount_amount:.2f}\n"
        f"Taxable Net Amount       : ${taxable_amount:.2f}\n"
        f"Estimated Tax ({tax_rate * 100:.1f}%)   : +${tax_amount:.2f}\n"
        f"----------------------------------------------------------------------\n"
        f"FINAL CONTRACT TOTAL     : ${final_total:.2f}\n"
        f"======================================================================\n"
        f"INFRASTRUCTURE COST ALLOCATION:\n"
        f"Allocated Nodes          : {server_nodes} Units\n"
        f"Exact Cost Per Node      : ${cost_per_server:.2f}\n"
        f"Base Whole Unit Split    : ${whole_server_share} / node\n"
        f"Unallocated Remainder    : ${unallocated_cents_remainder:.2f}\n"
        f"======================================================================"
    )

    # Output executive audit block
    print("--- HISTORICAL FORMATTING METHODS (FOR REFERENCE) ---")
    print("1. Plus Concatenation :", legacy_concat_summary)
    print("2. Modulo (%) Format  :", legacy_modulo_summary)
    print("3. str.format() Method:", legacy_format_summary)
    print("\n--- ENTERPRISE MODERN OUTPUT ---")
    print(modern_fstring_quote)


if __name__ == "__main__":
    # Simulate processing raw client payload received as string representations
    process_client_quote(
        raw_service_name="Cloud Infrastructure Security Audit",
        raw_hours_logged="40",
        raw_hourly_rate="125.50",
        raw_discount_percent="10",
        raw_tax_rate="0.085",
        raw_server_node_count="3"
    )