import random
import tkinter as tk
from PIL import ImageTk, Image


def winconfig():
    principal.title("YastADeck")
    principal.geometry("500x300+200+100")
    principal.resizable(width="False", height="False")


def winconfig2():
    principal.title("YastADeck")
    principal.geometry("1494x2085+200+100")
    principal.resizable(width="False", height="False")


def carta_nueva():
    n_cartas = entrada1.get()
    max_reroll = entrada2.get()
    winconfig2()
    img = ImageTk.PhotoImage(Image.open("Imágenes/",random.randint(1,22)))



f = open("deck", "r", encoding="utf-8")
lista_deck = f.read().splitlines()
f.close()

botones = []

principal = tk.Tk()
winconfig()

txt_cartas = tk.Label(principal, text="Cartas a sacar:").pack()

caja1 = tk.Canvas(principal, width=100, height=50)
entrada1 = tk.Entry(principal)
caja1.create_window(50, 25, window=entrada1)
caja1.pack()

txt_rerolls = tk.Label(principal, text="Rerolls:").pack()

caja2 = tk.Canvas(principal, width=100, height=50)
entrada2 = tk.Entry(principal)
caja2.create_window(50, 25, window=entrada2)
caja2.pack()

botones.append(tk.Button(principal, text="Dame cartas", command=carta_nueva).pack())

principal.mainloop()
