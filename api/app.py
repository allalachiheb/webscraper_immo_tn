from flask import Flask, jsonify
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import direct du scraper
from scraper.tunisie_annonce_scraper import scrape_tayara

app = Flask(__name__)

DATA_FILE = os.path.join(os.getcwd(), "data", "annonces.csv")

@app.route("/")
def home():
    return "<h3>🚀 API Scraping Immobilier</h3><p>Endpoints disponibles : /annonces (GET), /scrape (POST)</p>"

@app.route("/annonces", methods=["GET"])
def get_annonces():
    if not os.path.exists(DATA_FILE):
        return jsonify({"message": "Aucune donnée disponible"}), 404
    df = pd.read_csv(DATA_FILE)
    return jsonify(df.to_dict(orient="records")), 200

@app.route("/scrape", methods=["POST"])
def run_scraper():
    try:
        scrape_tayara(nb_pages=2)
        return jsonify({"message": "Scraping lancé et terminé ✅"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
