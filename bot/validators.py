import typer

def validate_quantity(qty: float):
    """Ensures quantity is positive."""
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return qty

def validate_stop_order(order_type: str, stop_price: float):
    """Ensures stop price is provided for STOP_LIMIT orders."""
    if order_type.upper() == "STOP_LIMIT" and (stop_price is None or stop_price <= 0):
        raise ValueError("Stop price is required and must be positive for STOP_LIMIT orders.")