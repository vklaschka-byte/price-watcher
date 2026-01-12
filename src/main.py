from scraper import ziskej_cenu
import time
from datetime import datetime

URL_PRODUKTU = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
CILOV_CENA = 55.0  
def main():
    print(f"--- SPUŠTĚN HLÍDAČ CEN ---")
    print(f"Sleduji: {URL_PRODUKTU}")
    print(f"Čas spuštění: {datetime.now().strftime('%H:%M:%S')}\n")

    aktualni_cena = ziskej_cenu(URL_PRODUKTU)

    if aktualni_cena is not None:
        print(f"💰 Aktuální cena: {aktualni_cena}")
        
        if aktualni_cena < CILOV_CENA:
            print("✅ SUPER CENA! Měl bys nakoupit (nebo poslat e-mail).")
            
        else:
            print(f"❌ Cena je stále vysoká (Cíl je pod {CILOV_CENA}).")
    else:
        print("Nepodařilo se zjistit cenu.")

if __name__ == "__main__":
    main()