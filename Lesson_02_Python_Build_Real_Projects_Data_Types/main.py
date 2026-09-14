# main.py
# ==============================================================================
# VIZIONE LABS: SAAS BILLING & INVOICING PIPELINE (LESSON 02)
# Production-Grade Financial Engine with Strict Type Hinting & Interpolation
# ==============================================================================

from typing import Dict, Union, Any


def parse_raw_telemetry(payload: Dict[str, str]) -> Dict[str, Union[int, float, str]]:
    """
    Parses and explicitly type-casts raw API telemetry data into operational numeric types.

    Args:
        payload (Dict[str, str]): Raw dictionary payload received from external API gateway.

    Returns:
        Dict[str, Union[int, float, str]]: Sanitized payload with cast numeric fields.
    """
    account_id: str = payload.get("account_id", "UNKNOWN_ACCOUNT")
    raw_calls: str = payload.get("api_calls_count", "0")
    raw_rate: str = payload.get("per_call_rate", "0.00")

    # Explicit Type Casting
    parsed_calls: int = int(raw_calls)
    parsed_rate: float = float(raw_rate)

    return {
        "account_id": account_id,
        "api_calls_count": parsed_calls,
        "per_call_rate": parsed_rate
    }


def calculate_invoice_total(
        api_calls: int,
        per_call_rate: float,
        base_tier_fee: float = 150.00,
        volume_discount: float = 25.50,
        tax_rate: float = 0.08
) -> float:
    """
    Computes total billed revenue applying explicit order of operations (PEMDAS).

    Formula:
        Total = ((Base Fee + (Calls * Rate)) - Discount) * (1 + Tax Rate)
    """
    usage_cost: float = api_calls * per_call_rate
    subtotal: float = (base_tier_fee + usage_cost) - volume_discount
    tax_multiplier: float = 1.0 + tax_rate

    final_billed_amount: float = subtotal * tax_multiplier
    return final_billed_amount


def generate_production_invoice(telemetry: Dict[str, Any], final_amount: float) -> str:
    """
    Formats enterprise client invoice record using advanced f-string formatting.
    """
    client_id: str = str(telemetry["account_id"])
    total_calls: int = int(telemetry["api_calls_count"])
    rate: float = float(telemetry["per_call_rate"])

    # Calculate capacity usage percentage (assuming 5,000 call cap)
    capacity_limit: int = 2 ** 12  # 4096 capacity threshold
    capacity_usage_pct: float = (total_calls / capacity_limit) * 100

    invoice_document: str = (
        f"======================================================================\n"
        f"                     VIZIONE LABS ENTERPRISE INVOICE                  \n"
        f"======================================================================\n"
        f"Client Account ID : {client_id}\n"
        f"Total API Calls   : {total_calls:,} units\n"
        f"Unit Price        : ${rate:.4f} / request\n"
        f"Capacity Usage    : {capacity_usage_pct:.2f}% of {capacity_limit} cap\n"
        f"----------------------------------------------------------------------\n"
        f"TOTAL AMOUNT DUE  : ${final_amount:,.2f} USD\n"
        f"======================================================================"
    )
    return invoice_document


def run_billing_pipeline() -> None:
    """
    Orchestrates the Vizione Labs SaaS billing pipeline execution context.
    """
    raw_api_payload: Dict[str, str] = {
        "account_id": "VIZ-8894-ENTERPRISE",
        "api_calls_count": "3450",
        "per_call_rate": "0.0125"
    }

    sanitized_data: Dict[str, Union[int, float, str]] = parse_raw_telemetry(raw_api_payload)

    final_total: float = calculate_invoice_total(
        api_calls=int(sanitized_data["api_calls_count"]),
        per_call_rate=float(sanitized_data["per_call_rate"])
    )

    invoice_output: str = generate_production_invoice(sanitized_data, final_total)
    print(invoice_output)


if __name__ == "__main__":
    run_billing_pipeline()