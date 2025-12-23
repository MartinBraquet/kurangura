# kurangura 
Formation Python: app mobile pour gérer les stocks et ventes d’une boutique

# Objectifs
- Ajouter les produits achetés (quantité, prix)
- Vendre les produits (stock mis à jour automatiquement)
- Calculer les bénéfices et voir l’évolution avec des graphiques
- Analyser les meilleurs produits

# Fonctionnalités prévues
- 1 boutique, pas d'identification / utilisateur
- Fonctionne sur un seul téléphone
- Acheter / vendre des produits (nombre et prix par pièce)
- Inventaire des stocks présents
- Capital actuel, depenses et recettes, benefices
- Historique simple et 1 graphique

Ce qu’on va apprendre : 
- Kivy
- SQLite
- logique achat / vente
- graphiques
- compilation APK Android sur buildozer

# Installation

Fork le projet sur GitHub.

Dans pycharm, clonez le projet.

Sinon, clonez le projet en ligne de commande (en remplaçant `votre-pseudo` par votre pseudo GitHub) :
```bash
git clone https://github.com/votre-pseudo/kurangura.git
cd kurangura
```
Installer python 3.10. Sur windows, vous pouvez utiliser [python.org](https://www.python.org/downloads/).

Créez un environnement virtuel et installez les dépendances :

```bash
python3.10 -m venv .venv
.venv\Scripts\activate  # Sur Windows
# source .venv/bin/activate  # Sur macOS/Linux
pip install -r requirements.txt -r requirements-compilation.txt
```

# Implémentation

Voir [implementation.md](implementation.md).
