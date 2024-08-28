import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


def convert_time():
    try:

       # Convertendo milissegundos em segundos
        milliseconds = int(entry.get())

       #milliseconds = 1724238057000

        seconds = milliseconds / 1000.0

       # Convertendo para um objeto datetime
        date_time = datetime.utcfromtimestamp(seconds)

       # UTC do Brasil
        brasil_time = date_time - timedelta(hours=3)

       # Saída em um formato de data
        result_label.config(text=f"Data e hora do Brasil:{brasil_time.strftime('%d-%m-%y %H:%M:%S')}")
   
   # Mesagem de erro
    except ValueError:
        messagebox.showerror("Erro. Por favor insira o numero do Timestamp correto!")

root = tk.Tk()
root.title("Conversor Timestamp")

entry_label = tk.Label(root, text="Digite o milisegundo:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

convert_button = tk.Button(root, text="Converter", command=convert_time)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()