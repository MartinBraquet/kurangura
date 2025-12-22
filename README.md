# kurangura
Formation Python: app mobile pour gérer les stocks et ventes d’une boutique

# Objectifs
- Ajouter les produits achetés (quantité, prix)
- Vendre les produits (stock mis à jour automatiquement)
- Calculer les bénéfices et voir l’évolution avec des graphiques
- Analyser les meilleurs produits
- Partager la boutique avec les travailleurs pour qu’ils puissent aussi enregistrer ventes et achats

# Fonctionnalités prévues
- 1 boutique, 2 rôles (admin & vendeur)
- Ajout produit, vente, stock, bénéfices
- Historique simple et 1 graphique
- Fonctionne sur un seul téléphone

Ce qu’on va apprendre : 
- Kivy
- SQLite
- logique stock/vente
- graphiques
- compilation APK Android

# Installation

Fork le projet sur GitHub.

Dans pycharm, clonez le projet.

Sinon, clonez le projet en ligne de commande (en remplaçant `votre-pseudo` par votre pseudo GitHub) :
```bash
git clone https://github.com/votre-pseudo/kurangura.git
cd kurangura
```

Créez un environnement virtuel et installez les dépendances :

```bash
python -m venv .venv
.venv\Scripts\activate  # Sur Windows
# source .venv/bin/activate  # Sur macOS/Linux
pip install -r requirements.txt
```

# Implémentation

Voir [implementation.md](implementation.md).
