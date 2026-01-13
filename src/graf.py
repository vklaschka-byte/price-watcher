import matplotlib.pyplot as plt
from datetime import datetime

casy = []
ceny = []

print("--- NAČÍTÁM DATA ---")

try:
    with open("ceny.csv", "r") as soubor:
        for radek in soubor:
            casti = radek.strip().split(",")
    
            if len(casti) == 2:
                cas_text = casti[0].strip()
                cena_text = casti[1].strip()
                
                ceny.append(float(cena_text))
                casy.append(datetime.strptime(cas_text, "%Y-%m-%d %H:%M:%S"))

    print(f"Načteno {len(ceny)} záznamů.")

    plt.figure(figsize=(10, 5))
    plt.plot(casy, ceny, marker='o', linestyle='-', color='blue', label='Cena knihy')
    
    plt.title("Vývoj ceny knihy: Muž v domácnosti 4")
    plt.xlabel("Čas")
    plt.ylabel("Cena (Kč)")
    plt.grid(True)
    plt.legend()
    
    plt.gcf().autofmt_xdate()

    nazev_obrazku = "vyvoj_ceny.png"
    plt.savefig(nazev_obrazku)
    print(f"✅ Graf byl úspěšně uložen do souboru: {nazev_obrazku}")

except FileNotFoundError:
    print("Chyba: Soubor ceny.csv neexistuje. Nejdřív spusťte main.py!")