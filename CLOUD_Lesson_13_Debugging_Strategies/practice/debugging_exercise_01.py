# ==============================================================================
# Vizione Labs — Python: Build Real Projects
# Lesson 13: Debugging Strategies, Exception Identification & Code Inspection
# File: practice/debugging_exercise_01.py
# ==============================================================================

"""
PRACTICE EXERCISE 01: Debugging Fundamentals & Exception Diagnostics

This script demonstrates common runtime/logic exceptions encountered during data processing,
along with programmatic code inspection, custom logging state checks, and assertion verification.
"""

import logging
import math

# Configure simple logging to monitor application execution state
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s")


def calculate_discounted_price(original_price: float, discount_percentage: float) -> float:
    """
    Calculates the final price after applying a percentage discount.
    Includes explicit boundary assertions and state inspection.
    """
    logging.info(f"Inspecting Inputs -> original_price: {original_price}, discount_percentage: {discount_percentage}")
    
    # Assert boundary conditions to catch logic errors early
    assert original_price >= 0, f"AssertionError: Original price cannot be negative. Got: {original_price}"
    assert 0 <= discount_percentage <= 100, f"AssertionError: Discount percentage must be between 0 and 100. Got: {discount_percentage}"
    
    discount_amount = original_price * (discount_percentage / 100.0)
    final_price = original_price - discount_amount
    
    # Code Inspection: Inspect internal calculated state
    logging.info(f"State Inspection -> discount_amount: {discount_amount:.2f}, final_price: {final_price:.2f}")
    return round(final_price, 2)


def process_transaction_log(raw_data: list) -> dict:
    """
    Processes a list of raw transaction strings and safely handles bad data formats.
    """
    processed_summary = {
        "valid_count": 0,
        "error_count": 0,
        "total_volume": 0.0,
        "errors": []
    }
    
    for index, record in enumerate(raw_data):
        try:
            logging.info(f"Processing Record Index [{index}] -> Raw: {record}")
            
            # Simulated Exception Handling Demo
            if not isinstance(record, dict):
                raise TypeError(f"Expected dict record, received {type(record).__name__}")
                
            amount = record["amount"]
            category = record["category"]
            
            # Explicit division test (ZeroDivisionError protection demo)
            tax_rate = record.get("tax_rate", 1.0)
            if tax_rate == 0:
                raise ZeroDivisionError("Tax rate calculation divisor cannot be zero.")
                
            tax_adjusted_amount = amount / tax_rate
            processed_summary["total_volume"] += tax_adjusted_amount
            processed_summary["valid_count"] += 1
            
        except KeyError as e:
            error_msg = f"Index {index}: Missing expected key {e}"
            logging.warning(f"Handled Exception -> {error_msg}")
            processed_summary["error_count"] += 1
            processed_summary["errors"].append(error_msg)
            
        except TypeError as e:
            error_msg = f"Index {index}: Invalid data structure - {e}"
            logging.warning(f"Handled Exception -> {error_msg}")
            processed_summary["error_count"] += 1
            processed_summary["errors"].append(error_msg)
            
        except ZeroDivisionError as e:
            error_msg = f"Index {index}: Mathematical anomaly - {e}"
            logging.error(f"Handled Exception -> {error_msg}")
            processed_summary["error_count"] += 1
            processed_summary["errors"].append(error_msg)
            
    return processed_summary


if __name__ == "__main__":
    print("=" * 70)
    print("VIZIONE LABS — DEBUGGING STRATEGIES & CODE INSPECTION DEMO")
    print("=" * 70)

    # 1. State Inspection & Assertion Checks
    print("\n--- [TEST 1] Calculating Valid Discount ---")
    price_result = calculate_discounted_price(150.00, 20.0)
    print(f"Result: ${price_result}")

    # 2. Intentional Assertion Trigger (Demonstrating Early Logic Traps)
    print("\n--- [TEST 2] Testing Boundary Assertion Safeguard ---")
    try:
        calculate_discounted_price(200.00, 150.0)  # Invalid discount > 100%
    except AssertionError as ae:
        print(f"[CAUGHT EXPECTED ASSERTION] {ae}")

    # 3. Exception Diagnostics & Data Processing
    print("\n--- [TEST 3] Batch Processing Records with Fault Ingestion ---")
    mock_batch = [
        {"amount": 100.0, "category": "Cloud Infrastructure", "tax_rate": 1.0},
        {"amount": 250.0},  # Triggers KeyError (missing 'category')
        "CORRUPTED_STRING_LINE",  # Triggers TypeError (not a dict)
        {"amount": 500.0, "category": "Software License", "tax_rate": 0.0},  # Triggers ZeroDivisionError
        {"amount": 750.0, "category": "Hardware", "tax_rate": 1.15}
    ]

    summary = process_transaction_log(mock_batch)
    
    print("\n--- FINAL PROCESSING SUMMARY ---")
    print(f"Valid Records Processed : {summary['valid_count']}")
    print(f"Errors Intercepted     : {summary['error_count']}")
    print(f"Total Volume Adjusted  : ${summary['total_volume']:.2f}")
    print("\nCaptured Error Trace Items:")
    for err in summary["errors"]:
        print(f" - {err}")
    print("=" * 70)