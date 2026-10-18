# LLM Course Project

 "Modele językowe (LLM Basics)".

## Wymagania
- Python >= 3.11

## Instalacja środowiska
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .


1.dlaczego liczby tokenów nie można wiarygodnie oszacować liczbą słów,

Liczba tokenów zależy bezpośrednio od słownika oraz reguł podziału (tokenizacji) konkretnego modelu. Tokenem może być całe krótkie słowo, jego fragment (subword), znak interpunkcyjny, spacja czy emoji. Ponadto teksty w różnych językach (np. język polski zawierający znaki diakrytyczne) są przez modele trenowane głównie na korpusach anglojęzycznych dzielone na znacznie mniejsze fragmenty, co sprawia, że to samo słowo w różnych językach generuje zupełnie inną liczbę tokenów.


