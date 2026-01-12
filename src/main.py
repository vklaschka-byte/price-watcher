from scraper import ziskej_cenu
import time
from datetime import datetime

URL_PRODUKTU = "https://www.knihydobrovsky.cz/kniha/muz-v-domacnosti-4-528805119"
CILOV_CENA = 250.0 
SOUBOR_DATA = "ceny.csv"

def zapis_do_souboru(cena):
    cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(SOUBOR_DATA, "a") as f:
        f.write(f"{cas}, {cena}\n")

def main():
    print(f"--- SPUŠTĚN AUTOMATICKÝ ZÁPISNÍK ---")
    print(f"Data ukládám do souboru: {SOUBOR_DATA}")
    print("Ukončení programu: Ctrl + C")
    print("-" * 30)

    while True:
        aktualni_cena = ziskej_cenu(URL_PRODUKTU)

        if aktualni_cena is not None:
            cas_vypis = datetime.now().strftime("%H:%M:%S")
            print(f"[{cas_vypis}] 📝 Zapisuji cenu: {aktualni_cena} Kč")
            
            zapis_do_souboru(aktualni_cena)
            
            if aktualni_cena < CILOV_CENA:
                print("🚨 CENA JE NÍZKÁ! Jdi nakupovat!")
        else:
            print("Chyba při stahování.")

        time.sleep(60)

if __name__ == "__main__":
    main()