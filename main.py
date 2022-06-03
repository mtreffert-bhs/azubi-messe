name = input("Bitte gib deinen Namen ein: ")

print("Hallo " + name + ". Schön, dass Du deinen Strompreis mit mir berechnest.")

base_price_per_month = 14.90
kwh_price = 0.3977
discount_percent = 5
kwh_per_year = 0

while (kwh_per_year <= 0):
    try:
        kwh_per_year = int(input("Bitte gib deinen Stromverbrauch pro Jahr in kwh ein: "))
    except Exception:
        print("Bitte gib eine positive ganze Zahl ein!")

new_customer = input("Bist Du ein Neukunde? (ja/nein): ")

price = 12 * base_price_per_month + kwh_price * kwh_per_year

if new_customer.lower() == "ja" or kwh_per_year > 5000:
    print("Prima, du erhältst einen Rabatt von " + str(discount_percent) + " Prozent!")
    price = price * (1 - discount_percent / 100)

print(f"Deine Stromkosten betragen {round(price, 2)} € pro Jahr, bzw. {round(price / 12, 2)} € pro Monat.")
