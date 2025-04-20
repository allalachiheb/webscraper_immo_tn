#  Webscraper Immobilier Tunisie

Ce projet a pour but de scraper automatiquement des annonces immobilières depuis le site [Tayara.tn](https://www.tayara.tn) et de les afficher dans un tableau de bord interactif.

##  Technologies utilisées

- **Python**
- **Selenium** pour le scraping
- **Pandas** pour la manipulation de données
- **Plotly & Dash** pour le tableau de bord interactif
- **Flask** (partie 1) pour l'API REST

##  Structure du projet

```
webscraper_immo_tn/
├── api/                        # API Flask (Partie 1)
├── scraper/                    # Script de scraping
│   └── tunisie_annonce_scraper.py
├── dashboard/                  # Tableau de bord Dash (Partie 2)
│   └── app.py
├── data/
│   └── annonces.csv            # Données extraites
├── requirements.txt
└── README.md
```

##  Lancer le projet

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Lancer le scraping
```bash
python scraper/tunisie_annonce_scraper.py
```

### 3. Lancer le dashboard Dash
```bash
python dashboard/app.py
```

Puis ouvrir [http://127.0.0.1:8050](http://127.0.0.1:8050) dans le navigateur.

##  Graphiques disponibles

- Nombre d’annonces par ville
- Distribution des prix
- Analyse comparative des prix par ville

##  Auteur

Projet réalisé par **Chiheb Allala et Mounir Hannouna** dans le cadre du module **Web Scraping & Visualisation - 2025**

---

> Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue !