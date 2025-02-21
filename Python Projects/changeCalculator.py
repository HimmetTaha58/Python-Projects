def calculate_change(total, payment):
    change = payment - total
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]  # Para birimleri
    change_distribution = {}

    for denom in denominations:
        count = int(change // denom)
        if count > 0:
            change_distribution[denom] = count
        change = round(change % denom, 2)  # Kalan para üstünü bul

    return change_distribution

total_amount = float(input("Toplam tutar: "))
payment_amount = float(input("Verilen ödeme: "))

if payment_amount < total_amount:
    print("Ödeme miktarı, toplam tutardan az olamaz.")
else:
    change = calculate_change(total_amount, payment_amount)
    print("Para Üstü: ")
    for denom, count in change.items():
        print(f"{count} adet {denom} TL")

