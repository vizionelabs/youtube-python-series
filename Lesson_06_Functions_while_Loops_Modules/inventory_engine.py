"""
Service Quote & Labor Calculation Engine
Module: inventory_engine.py
Provides reusable calculation algorithms for job estimates, material costs, and tax applications.
"""

from typing import Dict, Union

# Constant rate definitions
TAX_RATE: float = 0.08  # 8% municipal/state sales tax
LABOR_RATE_PER_SQFT: float = 2.50  # Base labor cost per square foot


def calculate_material_cost(area_sqft: float, material_type: str) -> float:
    """
    Computes material cost based on square footage and coating selection.

    :param area_sqft: Total surface area in square feet.
    :param material_type: Selected finish ('standard', 'premium', or 'industrial').
    :return: Total raw material cost.
    """
    material_rates: Dict[str, float] = {
        "standard": 1.20,
        "premium": 2.15,
        "industrial": 3.50
    }

    unit_price = material_rates.get(material_type.lower(), 1.20)
    return round(area_sqft * unit_price, 2)


def calculate_labor_cost(area_sqft: float, rush_job: bool = False) -> float:
    """
    Computes total labor cost with optional expedited processing surcharge.

    :param area_sqft: Total surface area in square feet.
    :param rush_job: Boolean flag indicating if expedited labor is required.
    :return: Total labor cost.
    """
    base_labor = area_sqft * LABOR_RATE_PER_SQFT
    if rush_job:
        base_labor *= 1.35  # 35% surcharge for rush deployment
    return round(base_labor, 2)


def generate_job_quote(area_sqft: float, material_type: str, rush_job: bool) -> Dict[str, Union[float, str]]:
    """
    Aggregates subtotal, applies tax rate, and compiles a structured quote output dictionary.

    :param area_sqft: Total square footage for the service job.
    :param material_type: Material finish tier chosen by client.
    :param rush_job: Priority scheduling status.
    :return: Structured summary of all billing line items.
    """
    materials = calculate_material_cost(area_sqft, material_type)
    labor = calculate_labor_cost(area_sqft, rush_job)
    subtotal = materials + labor
    tax_amount = subtotal * TAX_RATE
    final_total = subtotal + tax_amount

    return {
        "area": area_sqft,
        "material_tier": material_type.capitalize(),
        "material_cost": materials,
        "labor_cost": labor,
        "subtotal": round(subtotal, 2),
        "tax": round(tax_amount, 2),
        "total": round(final_total, 2)
    }