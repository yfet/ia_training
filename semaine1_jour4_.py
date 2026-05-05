# ============================================================
# SEMAINE 1 / JOUR 4 — Comprehensions, lambdas, gestion erreurs
# ============================================================

import csv
from collections import defaultdict

CHEMIN_CSV = 'data/ventes_sales.csv'

# Listes pour collecter les résultats
ventes_valides = []     # liste de dicts {client, produit, quantite, prix, montant}
erreurs = []            # liste de dicts {ligne, raison, contenu}


# ── 1. PARSING ROBUSTE ───────────────────────────────────────
# TODO 1 : ouvrir le CSV avec encoding='utf-8'

with open(CHEMIN_CSV, mode='r', encoding='utf-8') as f:

# TODO 2 : créer un DictReader, et utiliser enumerate() pour avoir le n° de ligne
#          (ex: for num, ligne in enumerate(reader, start=2)
#           — start=2 car ligne 1 = headers)
    reader = csv.DictReader(f)
    for num, ligne in enumerate(reader, start=2):
#
# TODO 3 : pour chaque ligne, dans un try/except :
#   - Vérifier que client n'est pas vide → sinon raise ValueError("client vide")
#   - Convertir quantite en int, prix en float
#   - Vérifier que quantite > 0 → sinon raise ValueError("quantite <= 0")
#   - Calculer montant = quantite * prix
#   - Ajouter à ventes_valides un dict {client, produit, quantite, prix, montant}
        try:
            client = ligne['client']
            if not client:
                raise ValueError("client vide")
            quantite = int(ligne['quantite'])
            prix = float(ligne['prix_unitaire'])
            if quantite <= 0:
                raise ValueError("quantite <= 0")
            montant = quantite * prix
            ventes_valides.append({
                'client': client,
                'produit': ligne['produit'],
                'quantite': quantite,
                'prix': prix,
                'montant': montant
            })
#
# TODO 4 : dans le except, ajouter à erreurs :
#   {'ligne': num, 'raison': str(e), 'contenu': dict(ligne)}
        except Exception as e:
            erreurs.append({
                'ligne': num,
                'raison': str(e),
                'contenu': dict(ligne)
            })


# ── 2. RAPPORT D'ERREURS ─────────────────────────────────────
# TODO 5 : afficher un rapport :
#   "X ventes valides, Y erreurs"
#   puis pour chaque erreur : "  Ligne {num} : {raison}"
print(f"{len(ventes_valides)} ventes valides, {len(erreurs)} erreurs")
for err in erreurs:
    print(f"  Ligne {err['ligne']} : {err['raison']}")

# ── 3. STATS AVEC COMPREHENSIONS ─────────────────────────────
# TODO 6 : avec une LIST COMPREHENSION, calculer le CA total
#   ca_total = sum(...) en une ligne
ca_total = sum(v['montant'] for v in ventes_valides)
#
# TODO 7 : avec une DICT COMPREHENSION, créer un dict
#   {client: nb_achats} où nb_achats = nombre de fois que ce client apparaît
#   (indice : utilise un set pour les clients uniques, puis comprehension)
#   Plus simple alternative : utilise defaultdict(int) avec une boucle
clients = {v['client'] for v in ventes_valides}
achats_par_client = {client: sum(1 for v in ventes_valides if v['client'] == client) for client in clients}

# ── 4. TRI AVEC LAMBDA ───────────────────────────────────────
# TODO 8 : trier ventes_valides par montant DESCENDANT
#   indice : sorted(ventes_valides, key=lambda v: v['montant'], reverse=True)
#
ventes_valides_triees = sorted(ventes_valides, key=lambda v: v['montant'], reverse=True)

# TODO 9 : afficher le TOP 3 :
#   "TOP 3 :"
#   "  1. {client} — {produit} : {montant}€"
#   "  2. ..."
print("TOP 3 :")
for i, v in enumerate(ventes_valides_triees[:3], start=1):
    print(f"  {i}. {v['client']} — {v['produit']} : {v['montant']:.2f}€")


# ── 5. PRODUITS UNIQUES (set comprehension) ──────────────────
# TODO 10 : avec une SET COMPREHENSION, extraire l'ensemble des produits uniques
#   produits_uniques = {... for v in ventes_valides}
#   puis afficher "{N} produits différents : {liste triée}"
produits_uniques = {v['produit'] for v in ventes_valides}
print(f"{len(produits_uniques)} produits différents : {sorted(produits_uniques)}")
