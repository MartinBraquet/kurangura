## 1. Architecture globale du projet

Avant d’écrire une ligne de code, définis cette structure :

```
kurangura/
│
├── main.py
├── buildozer.spec
├── database/
│   └── shop.db
│
├── models/
│   ├── product.py
│   ├── transaction.py
│
├── services/
│   ├── database.py
│   ├── inventory.py
│   ├── finance.py
│
├── ui/
│   ├── main_screen.kv
│   ├── buy_screen.kv
│   ├── sell_screen.kv
│   ├── stats_screen.kv
│
└── utils/
    └── charts.py
```

**Pourquoi c’est crucial**
Si tu mets toute la logique dans `main.py`, tu échoueras à maintenir l’app quand les règles de calcul évolueront.

---

## 2. Base de données (SQLite) – À faire en premier

### Schéma minimal conseillé

```sql
Product(
    id INTEGER PRIMARY KEY,
    name TEXT,
    purchase_price REAL,
    stock INTEGER
)

Transaction(
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    type TEXT,        -- 'BUY' ou 'SELL'
    date TEXT
)
```

### Erreur fréquente à éviter

❌ Ne stocke pas le bénéfice directement
✅ **Calcule-le dynamiquement** à partir des transactions

Pourquoi ?

* Tu éviteras les incohérences
* Tu pourras refaire les calculs plus tard

---

## 3. Logique métier (sans interface)

Tu dois pouvoir **faire tourner toute l’application dans un terminal** avant Kivy.

### Achat d’un produit

Pseudo-code :

```
si produit existe:
    stock += quantité
    mettre à jour prix d'achat moyen
sinon:
    créer produit
insérer transaction BUY
```

### Vente d’un produit

```
si stock < quantité:
    refuser vente
sinon:
    stock -= quantité
    insérer transaction SELL
```

### Calculs financiers

* Dépenses = somme(BUY.quantity * BUY.price)
* Recettes = somme(SELL.quantity * SELL.price)
* Bénéfice = recettes - dépenses
* Capital actuel = stock valorisé + cash

👉 **Tu n’as pas parlé de cash**, mais tu en as besoin pour un vrai suivi. Même si c’est implicite.

---

## 4. Kivy – Interface utilisateur

### Organisation des écrans

Utilise `ScreenManager` :

* Écran principal (résumé)
* Achat produit
* Vente produit
* Statistiques

### Exemple de flux utilisateur

1. Ouvre l’app
2. Voit capital + stock
3. Achète ou vend
4. Consulte graphique

### Erreur classique

❌ Mettre la logique SQL dans les fichiers `.kv`
✅ Le `.kv` sert uniquement à l’affichage

---

## 5. Graphiques (point délicat)

### Deux options réalistes

#### Option 1 (la plus stable Android)

* `matplotlib`
* Générer une image PNG
* L’afficher dans Kivy

Avantage : fiable sur Android
Inconvénient : moins interactif

#### Option 2

* `kivy_garden.graph`

Avantage : graphique dynamique
Inconvénient : parfois instable avec buildozer

👉 Pour une formation **je recommande option 1**.

---

## 6. Tests continus sur Android (indispensable)

Dès que tu as :

* un écran
* une base SQLite
* un bouton fonctionnel

➡ compile un APK **immédiatement**.

### Installation outils Windows

Installe WSL avec Ubuntu.

Ouvre WSL via la powershell et en tapant `wsl`.

### Installation outils Linux

Deplace le projet dans le dossier `/mnt/c/Users/...`

Dans WSL :

```bash
sudo apt update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y \
    python3.10 \
    python3.10-venv \
    python3.10-pip \
    openjdk-17-jdk \
    unzip \
    zip \
    git \
    autoconf \
    automake \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    cmake \
    libffi-dev \
    libssl-dev
```

### Environnement virtuel Python

```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-compilation.txt
pip install --upgrade pip setuptools wheel pyjnius
```

### Compilation initiale

```bash
buildozer init
buildozer -v android debug
```

❗ Attends-toi à des erreurs. C’est normal. Copie-colle les erreurs dans ChatGPT pour les résoudre, et puis relance la compilation:
```bash
buildozer android clean
buildozer -v android debug
```

---

## 7. Buildozer.spec – points critiques

Dans `buildozer.spec` :

```
requirements = python3,kivy,sqlite3,matplotlib
android.permissions = WRITE_EXTERNAL_STORAGE
```

Erreur fréquente :
❌ Ajouter trop de librairies
✅ Minimalisme absolu

---

## 8. Analyse des meilleurs produits

Méthode simple et efficace :

* Produits les plus vendus (quantité)
* Produits les plus rentables (bénéfice par produit)
* Rotation de stock

SQL exemple :

```sql
SELECT product_id, SUM(quantity)
FROM Transactions
WHERE type='SELL'
GROUP BY product_id
ORDER BY SUM(quantity) DESC
```

---

## 9. Itérations pédagogiques (important pour une formation)

Ne fais PAS tout d’un coup.

### Étapes recommandées

Jour 1:
1. Base de données: SQLite + logique achat/vente
2. Interface Kivy (boutons, pages, etc.) 

-> APK minimale

Jour 2:

1. Historique transactions
2. Calculs financiers
3. Graphiques

-> APK stable
