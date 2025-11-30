import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import ttkbootstrap as tb
from mymodule import (
    monogram, parse_date, validate_positive_int, calculate_set_volume,
    save_entry, load_entries, clear_all_entries
)
from mlmodule import MLStatistics, ml_szamitas

edit_item = None
current_file = None
dark_mode = False

def add_or_update():
    global edit_item
    try:
        parse_date(var_date.get())
        sets = validate_positive_int(var_sets.get())
        reps = validate_positive_int(var_reps.get())
        weight = float(var_weight.get())
        if weight <= 0:
            raise ValueError("A súlynak pozitív számnak kell lennie!")
        volume = calculate_set_volume(reps * sets, weight)
        vals = (
            var_date.get(),
            var_ex.get(),
            sets,
            reps,
            round(weight, 2),
            round(volume, 2)
        )
        if edit_item is not None:
            tree.item(edit_item, values=vals)
            exit_edit_mode()
        else:
            tree.insert("", "end", values=vals)
        update_stats()
    except Exception as e:
        messagebox.showerror("Hiba", str(e))

def save_selected_or_all():
    global current_file
    items = tree.selection() or tree.get_children()
    if not items:
        messagebox.showinfo("Info", "Nincs menthető sor.")
        return
    if current_file is None:
        filename = filedialog.asksaveasfilename(
            title="Mentés CSV-be",
            defaultextension=".csv",
            filetypes=[("CSV fájlok", "*.csv"), ("Minden fájl", "*.*")]
        )
        if not filename:
            return
        current_file = filename
    for item in items:
        v = tree.item(item, "values")
        entry = {
            "date": v[0],
            "exercise": v[1],
            "sets": int(v[2]),
            "reps": int(v[3]),
            "weight": float(v[4]),
            "volume": float(v[5])
        }
        save_entry(entry, file_path=current_file)
    messagebox.showinfo("Kész", f"Bejegyzések elmentve ide:\n{current_file}")

def load_all():
    global current_file, edit_item
    filename = filedialog.askopenfilename(
        title="Válassz egy CSV fájlt",
        filetypes=[("CSV fájlok", "*.csv"), ("Minden fájl", "*.*")]
    )
    if not filename:
        return
    current_file = filename
    tree.delete(*tree.get_children())
    for r in load_entries(file_path=current_file):
        tree.insert("", "end", values=(
            r["date"], r["exercise"], r["sets"],
            r["reps"], r["weight"], r["volume"]
        ))
    update_stats()
    exit_edit_mode()

def update_stats():
    rows = [tree.item(i, "values") for i in tree.get_children()]
    stats = MLStatistics(rows)
    summary = (
        f"Összes bejegyzés: {stats.count_entries()} | "
        f"Össz. volumen: {stats.total_volume()} | "
        f"{ml_szamitas(len(rows))} | {monogram()}"
    )
    lbl_stats.config(text=summary)

def delete_selected():
    global edit_item
    items = tree.selection()
    if not items:
        messagebox.showinfo("Info", "Nincs kijelölt sor.")
        return
    if not messagebox.askyesno("Megerősítés", "Biztos törlöd a kijelölt sorokat?"):
        return
    for item in items:
        tree.delete(item)
        if edit_item == item:
            exit_edit_mode()
    update_stats()

def delete_all():
    global current_file, edit_item
    if not tree.get_children():
        messagebox.showinfo("Info", "Nincs törölhető adat.")
        return
    if not messagebox.askyesno("Megerősítés", "Biztos törlöd az ÖSSZES bejegyzést? (Fájlban is!)"):
        return
    tree.delete(*tree.get_children())
    edit_item = None
    if current_file:
        clear_all_entries(file_path=current_file)
    update_stats()

def load_selected_to_form(event=None):
    global edit_item
    items = tree.selection()
    if not items:
        return
    edit_item = items[0]
    vals = tree.item(edit_item, "values")
    var_date.set(vals[0])
    var_ex.set(vals[1])
    var_sets.set(vals[2])
    var_reps.set(vals[3])
    var_weight.set(vals[4])
    btn_add.config(text="Frissítés (Enter)")

def exit_edit_mode():
    global edit_item
    edit_item = None
    btn_add.config(text="Hozzáadás (Enter)")

def on_enter(event=None):
    add_or_update()

def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        root.style.theme_use("flatly")
        btn_dark.config(text="Sötét mód")
        dark_mode = False
    else:
        root.style.theme_use("darkly")
        btn_dark.config(text="Világos mód")
        dark_mode = True

root = tb.Window(themename="flatly")
root.title("app")
root.geometry("1000x560")

frm = ttk.Frame(root, padding=12)
frm.pack(fill="x")

var_date = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
var_ex = tk.StringVar(value="Fekvenyomás")
var_sets = tk.StringVar(value="3")
var_reps = tk.StringVar(value="10")
var_weight = tk.StringVar(value="40")

ttk.Label(frm, text="Dátum").grid(row=0, column=0, sticky="w")
ttk.Entry(frm, textvariable=var_date, width=16).grid(row=1, column=0)
ttk.Label(frm, text="Gyakorlat").grid(row=0, column=1, sticky="w")
ttk.Entry(frm, textvariable=var_ex, width=24).grid(row=1, column=1)
ttk.Label(frm, text="Sorozat").grid(row=0, column=2, sticky="w")
ttk.Entry(frm, textvariable=var_sets, width=8).grid(row=1, column=2)
ttk.Label(frm, text="Ismétlés").grid(row=0, column=3, sticky="w")
ttk.Entry(frm, textvariable=var_reps, width=8).grid(row=1, column=3)
ttk.Label(frm, text="Súly (kg)").grid(row=0, column=4, sticky="w")
ttk.Entry(frm, textvariable=var_weight, width=10).grid(row=1, column=4)

btn_add = ttk.Button(frm, text="Hozzáadás (Enter)", command=add_or_update)
btn_add.grid(row=1, column=5, padx=8)

cols = ("date", "exercise", "sets", "reps", "weight", "volume")
tree = ttk.Treeview(root, columns=cols, show="headings")
tree.pack(fill="both", expand=True, padx=12, pady=8)

tree.heading("date", text="Dátum")
tree.column("date", width=100, anchor="center")
tree.heading("exercise", text="Gyakorlat")
tree.column("exercise", width=200, anchor="w")
tree.heading("sets", text="Sorozat")
tree.column("sets", width=70, anchor="center")
tree.heading("reps", text="Ismétlés")
tree.column("reps", width=70, anchor="center")
tree.heading("weight", text="Súly (kg)")
tree.column("weight", width=100, anchor="center")
tree.heading("volume", text="Volumen")
tree.column("volume", width=120, anchor="center")

bottom = ttk.Frame(root, padding=12)
bottom.pack(fill="x")

ttk.Button(bottom, text="Mentés CSV-be", command=save_selected_or_all).pack(side="left")
ttk.Button(bottom, text="Betöltés CSV-ből", command=load_all).pack(side="left", padx=8)
ttk.Button(bottom, text="Összesítés", command=update_stats).pack(side="left", padx=8)
ttk.Button(bottom, text="Törlés", command=delete_selected).pack(side="left", padx=8)
ttk.Button(bottom, text="Mind törlése", command=delete_all).pack(side="left", padx=8)
ttk.Button(bottom, text="Mégse szerkesztés", command=exit_edit_mode).pack(side="left", padx=8)

btn_dark = tb.Button(bottom, text="Sötét mód", command=toggle_dark_mode, bootstyle="secondary")
btn_dark.pack(side="left", padx=8)

lbl_stats = ttk.Label(bottom, text="Összes bejegyzés: 0 | Össz. volumen: 0")
lbl_stats.pack(side="right")

root.bind("<Return>", on_enter)
root.bind("<Delete>", lambda e: delete_selected())
tree.bind("<Double-1>", load_selected_to_form)

if __name__ == "__main__":
    root.mainloop()
