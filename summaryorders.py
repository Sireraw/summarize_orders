from typing import List, Dict, Tuple, Any

def aggregate_orders(orders: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
    """
    Calculates the total amount spent by each customer and returns the results
    sorted by total spent (highest first).

    Args:
        orders: A list of dicts, expected format:
                {"customer": "Alice", "amount": 29.99}

    Returns:
        A list of tuples: [("CustomerName", TotalSpent), ...].
    """
    customer_totals: Dict[str, float] = {}

    for order in orders:
        customer = order.get("customer")
        
        # 1. Skip orders where the customer name is missing or empty.
        if not customer:
            continue

        # 2. Safely retrieve the amount and ensure it is a float.
        try:
            amount = float(order.get("amount", 0.0))
        except (ValueError, TypeError):
            # Log this error or handle it as appropriate for production,
            # but for now, we'll treat it as zero to maintain flow.
            print(f"Warning: Non-numeric amount found for customer {customer}. Skipping amount.")
            amount = 0.0
        
        # 3. Accumulate total spent per customer using dict.get().
        # This is cleaner than the if/else block.
        customer_totals[customer] = customer_totals.get(customer, 0.0) + amount

    # Return customers sorted by total spent (highest first)
    return sorted(customer_totals.items(), key=lambda x: x[1], reverse=True)