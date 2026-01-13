# 📚 Hlídač cen knih (Price Watcher)

Tento projekt automaticky sleduje cenu vybrané knihy na e-shopu **Knihy Dobrovský**, ukládá historii cen a umí vykreslit graf vývoje.

## 🚀 Funkce
* **Web Scraping:** Stahuje aktuální cenu přímo ze stránky produktu.
* **Automatizace:** Běží v nekonečné smyčce a kontroluje cenu každou minutu.
* **Ukládání dat:** Historie cen se zapisuje do souboru `ceny.csv`.
* **Vizualizace:** Skript `graf.py` vykreslí graf vývoje ceny (`vyvoj_ceny.png`).

## 🛠️ Použité technologie
* Python 3
* BeautifulSoup4 (analýza HTML)
* Requests (stahování stránek)
* Matplotlib (vykreslování grafů)

## ⚙️ Jak spustit

1. **Nainstalujte závislosti:**
   ```bash
   pip install -r requirements.txt