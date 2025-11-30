import tkinter as ttk
from tkinter import messagebox
import random

def dobas (dobasok):
    eredmenyek=[0 for i in range(7)]
    for i in range (dobasok):
        szam = random.randint(1,6)
        eredmenyek[szam]+=1
    eredmeny_cimke_szoveg.set(
        f"1 -- {eredmenyek[1]}\n"
        f"2 -- {eredmenyek[2]}\n"
        f"3 -- {eredmenyek[3]}\n"
        f"4 -- {eredmenyek[4]}\n"
        f"5 -- {eredmenyek[5]}\n"
        f"5 -- {eredmenyek[6]}"
    )

def on_dobas():
    try:
        dobasok_szama=int(dobasok_szama_bemenet.get())
        dobas(dobasok_szama)
    except:
        messagebox.showerror("Hiba", "Rossz értéket adtál meg a dobásnál!")



root = ttk.Tk()
root.title("Kockadobás statisztika")
root.geometry("700x400")

cim_cimke=ttk.Label(text="Kockadobások", font=("Ariel", 20))
cim_cimke.grid(column=1, row=0, pady=10)

dobasok_szama_bemenet=ttk.StringVar(value="10")
dobasszam = ttk.Entry(root, textvariable=dobasok_szama_bemenet, font=("Arial", 20))
dobasszam.grid(column=0, row=1, padx=10)

eredmeny_cimke_szoveg=ttk.StringVar(value="...\n...\n...")
eredmeny_cimke=ttk.Label(root, textvariable=eredmeny_cimke_szoveg, font=("Arial", 20))
eredmeny_cimke.grid(column=1, row=2, padx=10)

gomb=ttk.Button(root, text="Dobás", command=on_dobas)
gomb.grid(column=2, row=1, padx=10)

kilepes=ttk.Button(root, text="Kilepes", command=root.destroy, bg="red", fg="white")
kilepes.grid(column=3, row=1, padx=10)

ttk.mainloop()