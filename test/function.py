def calculate_discount(total_amount, customer_type):
    if total_amount <= 0:
        raise ValueError("Total amount must be positive")

    if customer_type not in ["regular", "vip", "new"]:
        raise ValueError("Invalid customer type")

    if customer_type == "regular":
        if total_amount > 1000:
            return 0.1
        else:
            return 0.05
    elif customer_type == "vip":
        if total_amount > 500:
            return 0.15
        else:
            return 0.1
    else:  # new customer
        return 0.05