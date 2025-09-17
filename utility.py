def calculate_profit_margin(net_income: float, revenue: float) -> float:
    """
    Calculate the profit margin percentage.

    Args:
        net_income (float): Net income value.
        revenue (float): Revenue value.

    Returns:
        float: Profit margin percentage. Returns 0.0 if revenue is zero.
    """
    if revenue == 0:
        return 0.0
    return (net_income / revenue) * 100