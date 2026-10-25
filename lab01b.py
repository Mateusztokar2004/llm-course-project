import csv
import time
from collections import Counter
from src.llm_course.backends import make_backend
import dotenv

dotenv.load_dotenv()
import dotenv
dotenv.load_dotenv()


backend = make_backend()

PROMPT = "Podaj nazwę i jednozdaniowy opis aplikacji pomagającej studentowi planować naukę."
SYSTEM_INSTRUCTION = "Jesteś pomocnym asystentem akademickim. Odpowiadaj zwięźle."


configs = [
    {"name": "A", "temperature": 0.0, "top_p": 1.0, "do_sample": False},  # Greedy
    {"name": "B", "temperature": 0.3, "top_p": 1.0, "do_sample": True},   # Niski sampling
    {"name": "C", "temperature": 0.8, "top_p": 0.9, "do_sample": True},   # Średni sampling
    {"name": "D", "temperature": 1.2, "top_p": 0.9, "do_sample": True},   # Wysoki sampling
]

rows = []

print("Rozpoczynam eksperyment samplingu dla Laboratorium 01B...")

for config in configs:
    cfg_name = config["name"]
    temp = config["temperature"]
    top_p = config["top_p"]
    do_sample = config["do_sample"]
    
    for run_idx in range(1, 6):  # Dokładnie 5 powtórzeń dla każdej konfiguracji
        print(f"Wykonuję konfigurację {cfg_name}, próba {run_idx}/5...")
        
        
        result = backend.generate(
            system=SYSTEM_INSTRUCTION,
            user=PROMPT,
            max_tokens=100,
        )
        
       
        rows.append({
            "configuration": cfg_name,
            "run": run_idx,
            "text": result.text.strip(),
            "output_tokens": result.output_tokens,
            "latency_s": round(result.latency_s, 4)
        })

# --- KOD WYMAGANY PRZEZ PROWADZĄCEGO ---
def normalized(text: str) -> str:
    return " ".join(text.lower().split())

counts = Counter(normalized(row["text"]) for row in rows)
print("unikalne odpowiedzi:", len(counts))

with open("lab01b_sampling.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("Sukces! Plik lab01b_sampling.csv został wygenerowany i zapisany.")
