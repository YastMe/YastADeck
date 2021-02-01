import random
import tkinter as tk

def winconfig():
    principal.title("YastADeck")
    principal.geometry("500x300+200+100")
    principal.resizable(width="False", height="False")

def quit():
    global n_cartas, max_reroll, carta
    n_cartas = entrada1.get()
    max_reroll = entrada2.get()
    carta = random.randint(1, 22)
    principal.destroy()

def winconfig2():
    principal.title("YastADeck")
    principal.geometry("500x800+200+100")
    principal.resizable(width="False", height="True")


def ventana2():
    winconfig2()

def sacar():
    carta = random.randint(1, 22)
    ruta = "Imagenes/" + str(random.randint(1, 22)) + ".png"
    img = tk.PhotoImage(file=ruta)
    img = img.zoom(10)
    img = img.subsample(32)
    boton1 = tk.Button(principal, text="Reroll?", image = img, command=sacar).grid(column=0, row=0, padx=10, pady=1)


f = open("deck", "r", encoding="utf-8")
lista_deck = f.read().splitlines()
f.close()

principal = tk.Tk()
winconfig()

txt_cartas = tk.Label(principal, text="Cartas a sacar:").grid(column=0, row=0, padx=10, pady=10)

caja1 = tk.Canvas(principal, width=100, height=50)
entrada1 = tk.Entry(principal)
caja1.create_window(50, 25, window=entrada1)
caja1.grid(column=1, row=0, padx=10, pady=10)

txt_rerolls = tk.Label(principal, text="Rerolls:").grid(column=2, row=0, padx=10, pady=10)

caja2 = tk.Canvas(principal, width=100, height=50)
entrada2 = tk.Entry(principal)
caja2.create_window(50, 25, window=entrada2)
caja2.grid(column=3, row=0, padx=10, pady=10)

boton1= tk.Button(principal, text="Dame cartas", command=quit).grid(column=4, row=0, padx=10, pady=10)

principal.mainloop()

principal = tk.Tk()
canvas = tk.Canvas(principal, width=60, height=60)
canvas.pack()
button = tk.Button(principal, text="Reroll", command=sacar)
button.pack()
ventana2()

img = []
for x in range(1,22):
    ruta = "Imagenes/" + str(x) + ".png"
    img.append(tk.PhotoImage(file=ruta))
img = img[random.randint(1,22)].zoom(10)
img = img[random.randint(1,22)].subsample(32)
image_id = canvas.create_image(0, 0, anchor='nw', image=img)
principal.mainloop()

