import requests
from tkinter import *
import pprint
from forex_python.converter import CurrencyRates
euro_rates = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=045d8de5a2c200393f42779edcec9add&format=1') #api key may stop working in a while
rates = CurrencyRates()

root = Tk()
root.geometry("300x100")

class CurrencyConverter:
    def __init__(self, main):
        main.title('Currency Converter')
        self.entry_1 = Entry(main, width=14, borderwidth=5)
        self.entry_1.grid(row=0, column=0, columnspan=1, padx=10, pady=10)
        self.entry_2 = Entry(main, width=14, borderwidth=5)
        self.entry_2.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        self.options = ['Select Option', 'US Dollar $', 'Euro €', 'Japanese Yen ¥', 'British Pound £', 'Indian Rupee ₹']
        self.option_detect_1 = StringVar(main)
        self.option_detect_1.set(self.options[0])
        self.option_detect_2 = StringVar(main)
        self.option_detect_2.set(self.options[0])
        option_menu_1 = OptionMenu(main, self.option_detect_1, *self.options).grid(row=1, column=0)
        option_menu_2 = OptionMenu(main, self.option_detect_2, *self.options).grid(row=1, column=2)   
        self.option_detect_1.trace("w", self.get_current_option)
        self.option_detect_2.trace("w", self.get_current_option)      
        self.calculate = Button(main, text='Calculate', command=lambda:[self.clear_entry(), self.get_values(), self.get_current_option(), self.calculation()]).grid(row=1, column=1, sticky=NS)

    def clear_entry(self):
        self.entry_2.delete(0, END)
    def get_values(self):
        self.value = self.entry_1.get()
        self.value = float(self.value)

    def get_current_option(self, *args):
        self.option_1 = self.option_detect_1.get()
        self.option_2 = self.option_detect_2.get()

    def calculation(self):
        if self.option_1 == 'US Dollar $' and self.option_2 == 'Euro €': self.entry_2.insert(0, round(self.value*rates.get_rate('USD', 'EUR'), 2))
        if self.option_1 == 'US Dollar $' and self.option_2 == 'Japanese Yen ¥': self.entry_2.insert(0, round(self.value*rates.get_rate('USD', 'JPY'), 2))
        if self.option_1 == 'US Dollar $' and self.option_2 == 'British Pound £': self.entry_2.insert(0, round(self.value*rates.get_rate('USD', 'GBP'), 2))
        if self.option_1 == 'US Dollar $' and self.option_2 == 'Indian Rupee ₹': self.entry_2.insert(0, round(self.value*rates.get_rate('USD', 'INR'), 2)) 

        if self.option_1 == 'Euro €' and self.option_2 == 'US Dollar $': self.entry_2.insert(0, round(self.value*euro_rates.json()['rates']['USD'], 2))
        if self.option_1 == 'Euro €' and self.option_2 == 'Japanese Yen ¥': self.entry_2.insert(0, round(self.value*euro_rates.json()['rates']['JPY'], 2))
        if self.option_1 == 'Euro €' and self.option_2 == 'British Pound £': self.entry_2.insert(0, round(self.value*euro_rates.json()['rates']['GBP'], 2))  
        if self.option_1 == 'Euro €' and self.option_2 == 'Indian Rupee ₹': self.entry_2.insert(0, round(self.value*euro_rates.json()['rates']['INR'], 2)) 
        
        if self.option_1 == 'Japanese Yen ¥' and self.option_2 == 'US Dollar $': self.entry_2.insert(0, round(self.value*rates.get_rate('JPY', 'USD'), 2))
        if self.option_1 == 'Japanese Yen ¥' and self.option_2 == 'Euro €': self.entry_2.insert(0, round(self.value*rates.get_rate('JPY', 'EUR'), 2))
        if self.option_1 == 'Japanese Yen ¥' and self.option_2 == 'British Pound £': self.entry_2.insert(0, round(self.value*rates.get_rate('JPY', 'GBP'), 2))  
        if self.option_1 == 'Japanese Yen ¥' and self.option_2 == 'Indian Rupee ₹': self.entry_2.insert(0, round(self.value*rates.get_rate('JPY', 'INR'), 2))

        if self.option_1 == 'British Pound £' and self.option_2 == 'US Dollar $': self.entry_2.insert(0, round(self.value*rates.get_rate('GBP', 'USD'), 2))
        if self.option_1 == 'British Pound £' and self.option_2 == 'Japanese Yen ¥': self.entry_2.insert(0, round(self.value*rates.get_rate('GBP', 'JPY'), 2))
        if self.option_1 == 'British Pound £' and self.option_2 == 'Euro €': self.entry_2.insert(0, round(self.value*rates.get_rate('GBP', 'EUR'), 2))  
        if self.option_1 == 'British Pound £' and self.option_2 == 'Indian Rupee ₹': self.entry_2.insert(0, round(self.value*rates.get_rate('GBP', 'INR'), 2)) 

        if self.option_1 == 'Indian Rupee ₹' and self.option_2 == 'US Dollar $': self.entry_2.insert(0, round(self.value*rates.get_rate('INR', 'USD'), 2))
        if self.option_1 == 'Indian Rupee ₹' and self.option_2 == 'Japanese Yen ¥': self.entry_2.insert(0, round(self.value*rates.get_rate('INR', 'JPY'), 2))
        if self.option_1 == 'Indian Rupee ₹' and self.option_2 == 'Euro €': self.entry_2.insert(0, round(self.value*rates.get_rate('INR', 'EUR'), 2))  
        if self.option_1 == 'Indian Rupee ₹' and self.option_2 == 'British Pound £': self.entry_2.insert(0, round(self.value*rates.get_rate('INR', 'GBP'), 2)) 
        
run = CurrencyConverter(root)
root.mainloop()