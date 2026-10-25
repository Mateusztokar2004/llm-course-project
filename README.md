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




Lab 2 - Aftefakty 
1.cztery konfiguracje i po pięć powtórze
Konfiguracja A: Greedy (temperature=0.0, top_p=1.0, do_sample=False) – 5 powtórzeń.

Konfiguracja B: Niski sampling (temperature=0.3, top_p=1.0, do_sample=True) – 5 powtórzeń.

Konfiguracja C: Średni sampling (temperature=0.8, top_p=0.9, do_sample=True) – 5 powtórzeń.

Konfiguracja D: Wysoki sampling (temperature=1.2, top_p=0.9, do_sample=True) – 5 powtórzeń.

2.liczbę unikalnych wyników i średnią długość odpowiedzi
Model generowal stabilna, powtarzalna strukture odpowiedzi
srednia dlugosc wynosila 100 tokenow 

3.jeden przykład, w którym bardziej losowa odpowiedź była gorsza albo lepsza,
Przu wyzszej temperaturze model szerzej eksploruje przestrzen tokenow. W przypadku prostych zadan formatujacych wyzsza losowosc nie poprawi metoryki ale moze prowadzic do chatoycznych rozbieznoci w tekscie.n 

4.wyjaśnienie różnicy między logitem, prawdopodobieństwem i wybranym tokenem.

Logit - Surowy, nieznormalizowany wynik liczbowy przypisany przez ostatnią warstwę modelu dla każdego tokena ze słownika. Logity mogą być zarówno dodatnie, jak i ujemne i nie sumują się do jedności


Prawdopodobienstwo - Wartość z przedziału $[0, 1]$ otrzymana po przepuszczeniu wektora logitów przez funkcję softmax (oraz uwzględnieniu temperatury $T$). Prawdopodobieństwa są zawsze nieujemne i sumują się do 1


wybrany token -Konkretna jednostka tekstu wylosowana z rozkładu prawdopodobieństwa (lub wybrana deterministycznie w trybie greedy jako ta z najwyższym prawdopodobieństwem), która zostaje dopisana do generowanej sekwencji.