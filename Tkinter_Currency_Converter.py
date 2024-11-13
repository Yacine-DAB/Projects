import tkinter as tk
from tkinter import ttk

options = ["GBP", "EUR","USD", "CNY", "CAD"]
alg = "DZD"
class CurrencyConverter:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Currency Converter")
        self.window.geometry("500x500")

        # Create label and entry widgets
        self.label_frame = tk.LabelFrame(self.window, text="Conversion Window",
                                         font=("Times New Roman", 22),
                                         bg="brown")

        self.label_frame.pack(ipadx=20, ipady=20, fill="x", expand=True)

        self.label1 = tk.Label(self.label_frame, text="First Currency: ", bg="gray")
        self.label1.pack(ipadx=5, ipady=5)
        self.from_menu = ttk.Combobox(self.label_frame, values=options)
        self.from_menu.pack(ipadx=20, ipady=7, expand=True)
        self.from_menu.current(0)

        self.label2 = tk.Label(self.label_frame, text="DZD Currency: ", bg="gray")
        self.label2.pack(ipadx=5, ipady=5)
        self.to_menu = ttk.Combobox(self.label_frame, values=alg)
        self.to_menu.pack(ipadx=20, ipady=7, expand=True)
        self.to_menu.current(0)

        # Amount
        self.amount_label = tk.Label(self.label_frame, text="Amount: ", bg="gray")
        self.amount_label.pack(ipadx=12, ipady=5, expand=True)
        self.amount_entry = tk.Entry(self.label_frame)
        self.amount_entry.pack(ipadx=20, ipady=5)

        # Convert Button
        self.convert_button = tk.Button(self.label_frame,
                                        text="Convert",
                                        command=self.currency_function,
                                        bg="green")
        self.convert_button.pack(ipadx=10, ipady=5, expand=True)

        self.display_result = tk.Label(self.window, text="", font=("Times New Roman", 16))
        self.display_result.pack(ipadx=10, ipady=5, expand=True)

        self.window.mainloop()

    def currency_function(self):
        try:
            currencies = {
                "usd": 222.00,
                "eur": 238.00,
                "gbp": 278.00,
                "cad": 159.00,
                "cny": 50.00
            }
            alg_currency = {"dzd": 01.00}

            from_currency = self.from_menu.get().lower()
            to_currency = self.to_menu.get().lower()
            amount = float(self.amount_entry.get())

            if from_currency in currencies and to_currency in alg_currency:
                from_rate = currencies[from_currency]
                to_rate = alg_currency[to_currency]
                converted_amount = amount * (from_rate * to_rate)
                self.display_result.config(text=f"You'll get {converted_amount:.2f} {to_currency.upper()}\nfor {amount} {from_currency.upper()}")
            else:
                self.display_result.config(text="Invalid currency!")

        except ValueError:
            self.display_result.config(text="Please enter a valid number for the amount.")

if __name__ == "__main__":
    CurrencyConverter()
