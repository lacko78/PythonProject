# Edzésnapló alkalmazás — Projektleírás

**Hallgató:** Makany László (ML)  
**Tantárgy:** Szkript nyelvek Python  
**Projekt:** Tkinter alapú edzésnapló (CSV-kezeléssel)

## 1. Projekt rövid leírása
A program egy Pythonban készült, Tkinter alapú grafikus edzésnapló.  
A felhasználó megadhatja:
- dátum  
- gyakorlat  
- sorozat  
- ismétlés  
- súly  

A rendszer automatikusan számolja a volument, táblázatban jeleníti meg az adatokat, és CSV fájlba menti, illetve képes azt betölteni.  

A GUI modern megjelenését a `ttkbootstrap` biztosítja, a felület pedig világos és sötét mód között kapcsolható.

---

## 2. Fő funkciók
- Új edzésadat rögzítése  
- Adat szerkesztése dupla kattintással  
- Enter → hozzáadás / frissítés  
- Kijelölt sor törlése (gombbal vagy Delete)  
- Teljes táblázat és CSV törlése  
- CSV mentése (fájlválasztóval)  
- CSV betöltése  
- Automatikus volumen-számítás  
- Statisztika: bejegyzésszám, összvolumen, ML számítás  
- Sötét mód kapcsolása (`flatly` ↔ `darkly`)

---

## 3. Fájlstruktúra
```
app/
│── main.py
│── mymodule.py
│── mlmodule.py
│── workouts.csv   (ha létrejön)
│── README.md
```

---

## 4. Modulok rövid leírása

### mymodule.py
- `monogram()`
- `parse_date()`
- `validate_positive_int()`
- `calculate_set_volume()`
- `save_entry()`
- `load_entries()`
- `clear_all_entries()`

### mlmodule.py
- `MLStatistics` osztály (bejegyzés és volumen összesítése)
- `ml_szamitas()` saját statisztikai függvény

### main.py
- GUI, események, gombok, táblázat
- CSV betöltés és mentés
- Sötét mód
- Statisztika frissítése

---

## 5. Futtatás
```
python app/main.py
```

A program üres táblázattal indul, a CSV betöltése és mentése fájlválasztóval történik.

---

## 6. Összegzés
A projekt egy moduláris, Tkinter-alapú edzésnapló alkalmazás.
Tartalmaz modern  dizájnos GUI-t, CSV-kezelést, saját modulokat és statisztikai számításokat.

**Készült: 2025 – Makany László (ML)**
