def order_summary(customer, *items, **details):
    result = f"Замовлення для {customer}:"

    result += f"\nТовари: {', '.join(items)}"

    for key, value in details.items():
        result += f"\n{key}: {value}"

    return result

print(order_summary("Shura", "піца", "кола", city="Lviv", express=True))