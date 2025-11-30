class MLStatistics:
    def __init__(self, rows):
        self.rows = rows
    def count_entries(self) -> int:
        return len(self.rows)
    def total_volume(self) -> float:
        t = 0.0
        for r in self.rows:
            try:
                t += float(r[5])
            except Exception:
                pass
        return round(t, 2)

def ml_szamitas(n: int) -> str:
    return f"ML: {n} sor"