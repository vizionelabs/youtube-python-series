# ==============================================================================
# VIZIONE LABS | LEARN WITH REAL PROJECTS - LESSON 02
# File: main.py
# System: Vizione Labs Automated Client Invoicing & Retainer Engine
# Architecture: Data Type Processing, Type Casting & String Interpolation
# ==============================================================================

import sys

# ------------------------------------------------------------------------------
# VIZIONE LABS CONFIGURATION & CONSTANTS
# ------------------------------------------------------------------------------
AGENCY_NAME: str = "Vizione Labs"
AGENCY_TAX_RATE: float = 0.08  # 8% Corporate Tax Rate
PLATFORM_FEE_RATE: float = 0.02  # 2% Payment Gateway Processing Fee

# ------------------------------------------------------------------------------
# MOCK RAW INPUT DATA (Simulating Incoming Web Form / API Payload as Strings)
# ------------------------------------------------------------------------------
raw_client_id: str = "VL-8942"
raw_client_name: str = "  Acme Corp Tech  "
raw_hourly_rate: str = "125.50"
raw_hours_billed: str = "48"
raw_retainer_discount: str = "150.00"
raw_is_priority_client: str = "True"

# ------------------------------------------------------------------------------
# 1. INPUT SANITIZATION & TYPE CASTING
# ------------------------------------------------------------------------------
print("=" * 60)
print(f"[{AGENCY_NAME}] PROCESSING CLIENT INVOICE INGESTION")
print("=" * 60)

# Clean string inputs
client_id: str = raw_client_id.strip()
client_name: str = raw_client_name.strip()

# Type Casting: Converting string payloads to high-precision numerical types
try:
    hourly_rate: float = float(raw_hourly_rate)
    hours_billed: int = int(raw_hours_billed)
    retainer_discount: float = float(raw_retainer_discount)
    is_priority_client: bool = raw_is_priority_client.strip().lower() == "true"
except ValueError as e:
    print(f"[CRITICAL ERROR] Failed to cast input data payload: {e}")
    sys.exit(1)

# Inspect internal type mapping
print(f"-> Ingested Client: {client_name} (ID: {client_id})")
print(f"-> Verified Data Types: Rate={type(hourly_rate)}, Hours={type(hours_billed)}, Priority={type(is_priority_client)}")
print("-" * 60)

# ------------------------------------------------------------------------------
# 2. FINANCIAL CALCULATIONS & BUSINESS LOGIC
# ------------------------------------------------------------------------------
# Calculate gross billable work
gross_amount: float = hourly_rate * hours_billed

# Calculate priority surcharge logic (5% bonus surcharge if priority client)
priority_surcharge_rate: float = 0.05 if is_priority_client else 0.00
priority_surcharge: float = gross_amount * priority_surcharge_rate

# Subtotal calculation before tax
subtotal_after_discount: float = (gross_amount + priority_surcharge) - retainer_discount

# Tax and platform processing fees
tax_amount: float = subtotal_after_discount * AGENCY_TAX_RATE
platform_fee: float = subtotal_after_discount * PLATFORM_FEE_RATE

# Final Net Amount Owed
final_invoice_total: float = subtotal_after_discount + tax_amount + platform_fee

# ------------------------------------------------------------------------------
# 3. ADVANCED F-STRING REPORT GENERATION
# ------------------------------------------------------------------------------
invoice_report: str = f"""
============================================================
              OFFICIAL INVOICE: {AGENCY_NAME}              
============================================================
Client ID           : {client_id}
Client Name         : {client_name}
Priority Status     : {"YES (5% Priority Surcharge Applied)" if is_priority_client else "NO"}
------------------------------------------------------------
DEVELOPMENT METRICS:
Hours Logged        : {hours_billed} hrs
Hourly Base Rate    : ${hourly_rate:.2f}/hr
Gross Work Total    : ${gross_amount:.2f}

ADJUSTMENTS & FEES:
Priority Surcharge  : +${priority_surcharge:.2f}
Retainer Discount   : -${retainer_discount:.2f}
Subtotal            : ${subtotal_after_discount:.2f}

TAX & PROCESSING:
Corporate Tax (8%)  : ${tax_amount:.2f}
Platform Fee (2%)   : ${platform_fee:.2f}
------------------------------------------------------------
FINAL AMOUNT DUE    : ${final_invoice_total:.2f}
============================================================
Status: PENDING INGESTION | Engine: Vizione Labs Billing v2.0
============================================================
"""

# Render official financial statement to standard output
print(invoice_report)