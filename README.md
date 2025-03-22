# 📊 Web Scraper Immobilier – Tunisie

Ce projet récupère des annonces immobilières depuis le site **Tayara.tn** grâce à un script Python (Selenium), et les rend disponibles via une API Flask.

## 🔧 Fonctionnalités

- ✅ Scraping des annonces (titre, prix, localisation, lien)
- ✅ Stockage dans `data/annonces.csv`
- ✅ API REST avec :
  - `GET /annonces` : Liste des annonces
  - `POST /scrape` : Lance une collecte automatique

## ▶️ Lancer le projet

1. Activer l’environnement :
```bash
venv\Scripts\activate
2,Installer les dépendances :
pip install -r requirements.txt
3-Lancer l’API :
python api/app.py
 4-Tester avec Postman
GET http://127.0.0.1:5000/annonces
POST http://127.0.0.1:5000/scrape
