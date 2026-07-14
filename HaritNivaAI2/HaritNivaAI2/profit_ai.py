def calculate_profit(
    acres,
    yield_per_acre,
    selling_price,
    seed_cost,
    fertilizer_cost,
    labour_cost
):

    total_yield = acres * yield_per_acre

    revenue = total_yield * selling_price

    expenses = acres * (
        seed_cost +
        fertilizer_cost +
        labour_cost
    )

    net_profit = revenue - expenses

    if revenue > 0:
        margin = round((net_profit / revenue) * 100, 1)
    else:
        margin = 0

    if margin >= 40:
        advice = "🟢 Excellent profitability. Continue this farming plan."

    elif margin >= 20:
        advice = "🟡 Good profit. Consider reducing fertilizer or labour costs."

    else:
        advice = "🔴 Low profit. Try a different crop or improve yield."

    return {

        "yield": total_yield,

        "revenue": revenue,

        "expenses": expenses,

        "profit": net_profit,

        "margin": margin,

        "advice": advice

    }