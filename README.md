# 📚 Hlídač cen knih (Price Watcher)

Jednoduchý Python skript, který automaticky sleduje cenu vybrané knihy na e-shopu. Pokud cena klesne pod nastavenou hranici, program vás upozorní.

## 🚀 Funkce
* ✅ Stahuje aktuální cenu z webu (Web Scraping).
* ✅ Porovnává cenu s vaším limitem.
* ✅ Čistá struktura kódu připravená pro rozšíření (např. o e-mailové notifikace).

## 🛠 Použité technologie
* **Python 3**
* **BeautifulSoup4** (analýza HTML)
* **Requests** (stahování stránek)

## ⚙️ Jak spustit
1. Nainstalujte závislosti:
   pip install -r requirements.txt

2. Spusťte hlídače:
   python src/main.py
