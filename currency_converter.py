# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk


#fwtching API
import requests
import json

API_KEY="033d77e75ba67cadd50d20b4"

url=f"https://v6.exchangerate-api.com/v6/033d77e75ba67cadd50d20b4/latest/USD"

response=requests.get(f"{url}").json()

currencies=dict(response["conversion_rates"])
#print(currencies)


t=Tk()

t.geometry("500x500")
t.title("Currency converter")

t.resizable(height=False,width=False)

#colors
primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'

#logo background
top_frame = Frame(t, bg=primary, width=500, height=100)
top_frame.grid(row=0, column=0)
#logo text
name_label = Label(top_frame, text='Currency Converter', bg=primary, fg=white, pady=30, padx=160, justify=CENTER, font=('Poppins 30 bold',))
name_label.grid(row=0, column=0)

bottom_frame = Frame(t, width=300, height=250)
bottom_frame.grid(row=1, column=0)

#labels for and to

from_currency_label = Label(bottom_frame, text='FROM:', font=('Poppins 10 bold'), justify=LEFT)
from_currency_label.place(x=5, y=10)
to_currency_label = Label(bottom_frame, text='TO:', font=('Poppins 10 bold'), justify=RIGHT)
to_currency_label.place(x=160, y=10)


#combox for and to
from_currency_combo = ttk.Combobox(bottom_frame,values=list(currencies.keys()), width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=5, y=30)


to_currency_combo = ttk.Combobox(bottom_frame,values=list(currencies.keys()), width=14, font=('Poppins 10 bold'))
to_currency_combo.place(x=160, y=30)

#label for amount
amount_label = Label(bottom_frame, text='AMOUNT:', font=('Poppins 10 bold'))
amount_label.place(x=5, y=55)

#entry for amount
amount_entry = Entry(bottom_frame, width=25, font=('Poppins 15 bold'))
amount_entry.place(x=5, y=80)

#label for Result

result_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
result_label.place(x=5, y=115)

#label for time
time_label = Label(bottom_frame, text='', font=('Poppins 10 bold'))
time_label.place(x=5, y=135)




#creating function to convert currencies
def convert():
    source = from_currency_combo.get()
    source2 = to_currency_combo.get()
    amount = amount_entry.get()
    result = requests.get(f'https://v6.exchangerate-api.com/v6/033d77e75ba67cadd50d20b4/pair/{source}/{source2}/{amount}').json()
    converted_result = result['conversion_result']
    formatted_result = f'{amount} {source} = {converted_result} {source2}'
    result_label.config(text=formatted_result)
    time_label.config(text='Last updated,' + result['time_last_update_utc'])

#convert button
convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'),command=convert)
convert_button.place(x=5, y=165)







t.mainloop()