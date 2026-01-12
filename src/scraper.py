import requests
from bs4 import BeautifulSoup

def ziskej_cenu(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        page = requests.get(url, headers=headers)
        page.raise_for_status()
        
        soup = BeautifulSoup(page.content, "html.parser")
        
        container = soup.find(class_="js-price")
        
        if container:
            price_element = container.find("strong")
            
            if price_element:
                price_text = price_element.get_text()
            
                clean_text = price_text.replace("Kč", "").replace(" ", "").replace("\xa0", "").replace(",", ".").strip()
                return float(clean_text)
        
        print("Cena nenalezena. Zkuste zkontrolovat selektor.")
        return None

    except Exception as e:
        print(f"Chyba: {e}")
        return None