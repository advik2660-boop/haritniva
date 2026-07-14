def calculate_budget(seed, fertilizer, labour, other, expected_income):

    total_cost = seed + fertilizer + labour + other

    net_profit = expected_income - total_cost

    if net_profit > 0:
        status = "Profit"
    elif net_profit < 0:
        status = "Loss"
    else:
        status = "Break Even"

    return {
        "seed": seed,
        "fertilizer": fertilizer,
        "labour": labour,
        "other": other,
        "total_cost": total_cost,
        "income": expected_income,
        "profit": net_profit,
        "status": status
    }