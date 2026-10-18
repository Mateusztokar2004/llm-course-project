import os
import json
from datetime import datetime, timezone
from dataclasses import asdict
import dotenv

# Ładujemy zmienne z pliku .env
dotenv.load_dotenv()

# Importujemy nasz backend z przygotowanego modułu w src/llm_course/backends.py
from llm_course.backends import LocalBackend, Generation

def append_event(path: str, result: Generation, status: str = "ok") -> None:
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        **{k: v for k, v in asdict(result).items() if k != "text"},
    }
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    print("Inicjalizacja lokalnego modelu LLM...")
    backend = LocalBackend()
    
    print("Wysyłanie zapytania do modelu...")
    result = backend.generate(
        system="Odpowiadaj krótko i jasno po polsku.",
        user="Wyjaśnij w dwóch zdaniach, czym jest token w modelu językowym.",
        max_tokens=160,
    )
    
    print("\n--- OTRZYMANA ODPOWIEDŹ ---")
    print(result.text)
    print("-" * 30)
    print(
        f"Model: {result.model} | Tryb: {result.mode} | "
        f"Wejście: {result.input_tokens} tokenów | "
        f"Wyjście: {result.output_tokens} tokenów | "
        f"Czas: {result.latency_s:.2f} s"
    )
    
    # Zapisujemy zdarzenie do logów JSONL zgodnie z wymaganiami
    log_path = os.getenv("LOG_DIR", "logs") + "/generations.jsonl"
    append_event(log_path, result)
    print(f"Zdarzenie zostało zalogowane do: {log_path}")