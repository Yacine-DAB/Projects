
print("Currency Converter: ")
print("#--------------------")

currencies = {"usd":222.00,
              "eur":238.00,
              "gbp":278.00,
              "cad":159.00,
              "cny":30.00}


currency = input("Please choose a currency (usd,eur,gbp,cad cny) to convert into dzd: ").lower()
amount = int(input("Enter how much you want to convert into dzd: "))


if currency in currencies:
    rate = currencies[currency]
    converter = amount * rate
    print(f"with exchange rate, tou'll get {converter:.2f} converted in dzd")
else:
    print("Invalid currency!")








