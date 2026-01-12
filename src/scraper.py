import requests
from bs4 import BeautifulSoup

def ziskej_cenu(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    try:
        page = requests.get(url, headers=headers)
        page.raise_for_status() 
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        price_element = soup.find(class_="price_color") 
        
        if price_element:
            price_text = price_element.get_text()

            price_cislo = float(price_text.replace("£", "").replace("$", "").replace("Kč", "").strip())
            return price_cislo
        else:
            print("Cena na stránce nebyla nalezena. Zkontroluj selektor (class/id).")
            return None

    except Exception as e:
        print(f"Chyba při stahování: {e}")
        return None