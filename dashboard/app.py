import os
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Détection du chemin du CSV
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "annonces.csv")

# Chargement des données
df = pd.read_csv(data_path)

# Nettoyage de la colonne prix
def nettoyer_prix(valeur):
    try:
        valeur = valeur.replace("DT", "").replace(" ", "").replace(",", "")
        return float(valeur)
    except:
        return None

df["prix_nettoye"] = df["prix"].apply(nettoyer_prix)
df = df[df["prix_nettoye"].notnull()]

# Filtrer les villes valides
df = df[df["ville"].str.lower() != "inconnu"]

# Initialisation de l'application Dash
app = dash.Dash(__name__)
app.title = "Dashboard Immobilier Tunisie"

# Layout avec style
app.layout = html.Div(style={"fontFamily": "Arial", "margin": "40px"}, children=[
    html.H1("📊 Tableau de bord - Annonces immobilières en Tunisie", style={"textAlign": "center"}),

    html.Div([
        html.P(f"Nombre total d'annonces connues : {len(df)}", style={"fontSize": "18px"})
    ], style={"textAlign": "center", "marginBottom": "40px"}),

    html.Div([
        dcc.Graph(
    id="annonces-par-ville",
    figure=px.bar(
        df["ville"].value_counts().nlargest(10).reset_index(name="count").rename(columns={"index": "ville"}),
        x="ville",
        y="count",
        labels={"ville": "Ville", "count": "Nombre d'annonces"},
        title="Top 10 des villes avec le plus d'annonces"
    )
)

    ], style={"marginBottom": "60px"}),

    html.Div([
        dcc.Graph(
            id="distribution-prix",
            figure=px.histogram(
                df,
                x="prix_nettoye",
                nbins=30,
                title="Distribution des prix des annonces",
                labels={"prix_nettoye": "Prix (DT)", "count": "Nombre d'annonces"}
            )
        )
    ], style={"marginBottom": "60px"}),

    html.Div([
        dcc.Graph(
            id="prix-par-ville",
            figure=px.box(
                df,
                x="ville",
                y="prix_nettoye",
                points="outliers",
                title="Distribution des prix par ville",
                labels={"prix_nettoye": "Prix (DT)", "ville": "Ville"}
            )
        )
    ])
])

if __name__ == "__main__":
    print("✅ Serveur Dash démarré")
    app.run(debug=True)
