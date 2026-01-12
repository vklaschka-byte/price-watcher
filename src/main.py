from scraper import ziskej_cenu
from datetime import datetime

URL_PRODUKTU = "https://www.knihydobrovsky.cz/kniha/muz-v-domacnosti-4-528805119"
CILOV_CENA = 250.0 

def main():
    print(f"--- SPUŠTĚN HLÍDAČ CEN (Manga) ---")
    print(f"Sleduji: {URL_PRODUKTU}")
    
    aktualni_cena = ziskej_cenu(URL_PRODUKTU)

    if aktualni_cena is not None:
        print(f"💰 Aktuální cena: {aktualni_cena} Kč")
        
        if aktualni_cena < CILOV_CENA:
            print("✅ SUPER CENA! Kupuj to!")
        else:
            print(f"❌ Cena je {aktualni_cena} Kč (Cíl je pod {CILOV_CENA} Kč).")
    else:
        print("Nepodařilo se zjistit cenu.")

if __name__ == "__main__":
    main()