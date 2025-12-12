from __future__ import annotations

from typing import Any, Dict, Iterable, Optional


# -----------------------------
# Helpers
# -----------------------------

def _to_int(value: Any) -> Optional[int]:
    """Try to convert a value to int. Return None if not possible."""
    try:
        if value is None:
            return None
        # Accept strings like "001", "12", etc.
        return int(str(value).strip())
    except (ValueError, TypeError):
        return None


# -----------------------------
# Public functions
# -----------------------------

def generate_sequential_id(employees: Iterable[Dict[str, Any]]) -> int:
    """
    Generate the next sequential employee ID based on existing records.

    Rules:
    - If there are no employees, start at 1
    - Ignore missing or non-numeric employee_id values
    - Return (max_numeric_id + 1)
    """
    max_id = 0

    for emp in employees or []:
        emp_id = _to_int(emp.get("employee_id"))
        if emp_id is not None and emp_id > max_id:
            max_id = emp_id

    return max_id + 1


def format_address(address: Optional[Dict[str, Any]]) -> str:
    """
    Format an address dict into a single string.

    Expected keys:
    - street, city, state, zip

    This function is defensive:
    - Missing keys won't crash
    - Returns 'N/A' if nothing useful is found
    """
    if not isinstance(address, dict):
        return "N/A"

    street = str(address.get("street", "")).strip()
    city = str(address.get("city", "")).strip()
    state = str(address.get("state", "")).strip()
    zip_code = str(address.get("zip", "")).strip()

    parts = []

    if street:
        parts.append(street)

    location = []
    if city:
        location.append(city)
    if state:
        location.append(state)

    # "City - ST"
    if location:
        if len(location) == 2:
            parts.append(f"{location[0]} - {location[1]}")
        else:
            parts.append(location[0])

    if zip_code:
        parts.append(zip_code)

    return ", ".join(parts) if parts else "N/A"
