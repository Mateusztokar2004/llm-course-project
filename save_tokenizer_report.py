import json
from pathlib import Path
from transformers import AutoTokenizer

# Definicja modeli i próbek tekstowych
models = [
    "Qwen/Qwen2.5-0.5B-Instruct",
    "bert-base-cased"
]

samples = [
    "kot",
    "nieprzewidywalność",
    "Large language model",
    "Duży model językowy",
    "print('Hello!')",
    "LLM-y 🤖 kosztują 0.01 USD",
    "Mateusz Tokarski",
]

report_data = []

for model_name in models:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model_results = {"model_name": model_name, "tests": []}
    
    for text in samples:
        ids = tokenizer.encode(text, add_special_tokens=False)
        pieces = [tokenizer.decode([token_id]) for token_id in ids]
        
        model_results["tests"].append({
            "text": text,
            "token_ids": ids,
            "pieces": pieces,
            "count": len(ids)
        })
    
    report_data.append(model_results)

# Zapis raportu do katalogu reports/lab01a.json
reports_dir = Path("reports")
reports_dir.mkdir(parents=True, exist_ok=True)
output_path = reports_dir / "lab01a.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print(f"Raport z tokenizacji został zapisany pomyślnie do pliku: {output_path}")