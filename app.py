import requests
import json
from tkinter import *
from tkinter import ttk


def pegarCotacao():
    currentQuote = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    valueQuote = currentQuote.json()

    USDBRL = valueQuote['USDBRL']['bid']
    EURBRL = valueQuote['USDBRL']['bid']
    BTCBRL = valueQuote['BTCBRL']['bid']

    textAll = f'''
    Dólar Americano/Real Brasileiro => {USDBRL}
    Euro/Real Brasileiro => {EURBRL}
    Bitcoin/Real Brasileiro => {BTCBRL}'''

    T["text"] = textAll


janela = Tk()
janela.title("Titulo Tkinter")

T = Label(janela, text='Cotação Dólar/Euro/Bitcoin em tempo real')
T.grid(column=0, row=0, pady=10, padx=15)

B = Button(janela, text="Exibir cotação", command=pegarCotacao)
B.grid(column=0, row=1, pady=10, padx=15)

T = Label(janela, text='')
T.grid(column=0, row=2, pady=10, padx=15)

janela.mainloop()
