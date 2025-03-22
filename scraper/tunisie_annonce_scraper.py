from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
import os

def scrape_tayara(nb_pages=2):
    annonces = []

    chromedriver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for page in range(1, nb_pages + 1):
            url = f"https://www.tayara.tn/ads/immobilier/?page={page}"
            print(f"Scraping page {page}: {url}")
            driver.get(url)
            time.sleep(5)

            articles = driver.find_elements(By.CSS_SELECTOR, "li.snap-start article")
            print(f"→ {len(articles)} annonces trouvées sur la page {page}")

            for article in articles:
                try:
                    titre = article.find_element(By.CSS_SELECTOR, "h2.card-title").text.strip()
                    prix_elem = article.find_elements(By.CSS_SELECTOR, "data")
                    prix = prix_elem[0].text.strip() if prix_elem else "Non spécifié"
                    locs = article.find_elements(By.CSS_SELECTOR, "div.text-neutral-500")
                    localisation = locs[-1].text.strip() if locs else "Inconnu"
                    a_tag = article.find_element(By.TAG_NAME, "a")
                    lien = a_tag.get_attribute("href")
                    if lien.startswith("/"):
                        lien = "https://www.tayara.tn" + lien

                    annonces.append({
                        "titre": titre,
                        "prix": prix,
                        "localisation": localisation,
                        "url": lien
                    })
                except Exception as e:
                    print("❌ Erreur sur une annonce :", e)

    finally:
        driver.quit()

    if not annonces:
        print("⚠️ Aucune annonce trouvée.")
        return

    os.makedirs("data", exist_ok=True)
    with open("data/annonces.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=annonces[0].keys())
        writer.writeheader()
        writer.writerows(annonces)

    print(f"✅ {len(annonces)} annonces sauvegardées dans data/annonces.csv")

# Pour exécution directe
if __name__ == "__main__":
    scrape_tayara(nb_pages=2)






