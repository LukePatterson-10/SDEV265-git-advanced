def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total * 1.08 + 5.99  # Adding tax and shipping fee