from datetime import datetime
from typing import List, Dict, Any
import csv, os

CSV_FILE = os.path.join(os.path.dirname(__file__), "workouts.csv")

def monogram(name: str = "Makany Laszlo") -> str:
    parts = [p for p in name.strip().split() if p]
    return "".join(p[0].upper() for p in parts)

def parse_date(iso_date: str) -> datetime:
    return datetime.strptime(iso_date, "%Y-%m-%d")

def validate_positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue <= 0:
        raise ValueError("Csak pozitív egész szám lehet!.")
    return ivalue

def calculate_set_volume(reps: int, weight: float) -> float:
    return reps * weight

def save_entry(entry: Dict[str, Any], file_path: str = CSV_FILE) -> None:
    file_exists = os.path.exists(file_path)
    with open(file_path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "exercise", "sets", "reps", "weight", "volume"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)

def load_entries(file_path: str = CSV_FILE) -> List[Dict[str, Any]]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def clear_all_entries(file_path: str = CSV_FILE) -> None:
     if os.path.exists(file_path):
        os.remove(file_path)
