import random
import tkinter as ttk
from tkinter import messagebox


class KockaDobas:
    def __init__(self, master):
        self.master = master
        master.title("Kockadobás statisztika")
        master.geometry("700x400")

        self.cim_cimke = ttk.Label(text="Kockadobások", font=("Ariel", 20))
        self.cim_cimke.grid(column=1, row=0, pady=10)

        self.dobasok_szama_bemenet = ttk.StringVar(value="10")
        self.dobasszam = ttk.Entry(self.master, textvariable=self.dobasok_szama_bemenet, font=("Arial", 20))
        self.dobasszam.grid(column=0, row=1, padx=10)

        self.eredmeny_cimke_szoveg = ttk.StringVar(value="...\n...\n...")
        self.eredmeny_cimke = ttk.Label(self.master, textvariable=self.eredmeny_cimke_szoveg, font=("Arial", 20))
        self.eredmeny_cimke.grid(column=1, row=2, padx=10)

        self.gomb = ttk.Button(self.master, text="Dobás", command=self.on_dobas)
        self.gomb.grid(column=2, row=1, padx=10)

        self.kilepes = ttk.Button(root, text="Kilepes", command=root.destroy, bg="red", fg="white")
        self.kilepes.grid(column=3, row=1, padx=10)






    def dobas (self,dobasok):
        self.eredmenyek=[0 for i in range(7)]
        for i in range (self.dobasok):
            self.szam = random.randint(1,6)
            self.eredmenyek[self.szam]+=1
        self.eredmeny_cimke_szoveg.set(
            f"1 -- {self.eredmenyek[1]}\n"
            f"2 -- {self.eredmenyek[2]}\n"
            f"3 -- {self.eredmenyek[3]}\n"
            f"4 -- {self.eredmenyek[4]}\n"
            f"5 -- {self.eredmenyek[5]}\n"
            f"5 -- {self.eredmenyek[6]}"
        )

    def on_dobas(self):
        try:
            self.dobasok_szama=int(self.dobasok_szama_bemenet.get())
            self.dobas(self.dobasok_szama)
        except:
            messagebox.showerror("Hiba", "Rossz értéket adtál meg a dobásnál!")


root = ttk.Tk()
app=KockaDobas(root)
ttk.mainloop()