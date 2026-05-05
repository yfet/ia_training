# ============================================================
# SEMAINE 1 / JOUR 3 — CSV & JSON
# ============================================================

import csv
from collections import defaultdict   # utile pour le TODO 5

CHEMIN_CSV = 'data/ventes.csv'

# id,client,produit,quantite,prix_unitaire,date

ca_total = 0.0
ca_par_client = defaultdict(float)
meilleur_client = None
nb_ventes = 0

# ── 1. LECTURE et AFFICHAGE ──────────────────────────────────
# TODO 1 : ouvrir le fichier en mode lecture, encoding='utf-8'
with open(CHEMIN_CSV, mode='r', encoding='utf-8') as f:

# TODO 2 : créer un DictReader
    reader = csv.DictReader(f)

# TODO 3 : pour chaque ligne, calculer montant_total = quantite * prix_unitaire
#          (attention : convertir en int/float — tout est str par défaut)
    

    for ligne in reader:
        client = ligne['client']
        produit = ligne['produit']
        quantite = int(ligne['quantite'])
        prix_unitaire = float(ligne['prix_unitaire'])
        montant_total = quantite * prix_unitaire
        ca_par_client[client] += montant_total
        nb_ventes += 1

# TODO 4 : afficher "{client} a acheté {qte}× {produit} pour {montant:.2f}€"
        print(f"{client} a acheté {quantite}× {produit} pour {montant_total:.2f}€")


# ── 2. CHIFFRE D'AFFAIRES TOTAL ──────────────────────────────
# TODO 5 : pendant la lecture, accumuler le total dans une variable `ca_total`
        ca_total += montant_total

# TODO 6 : afficher "CA total : XXXX.XX€"
    print(f"CA total : {ca_total:.2f}€")

# ── 3. MEILLEUR CLIENT ───────────────────────────────────────
# TODO 7 : utiliser un defaultdict(float) pour accumuler le montant par client
#          ex: ca_par_client['Alice Rakoto'] += montant_total
# TODO 8 : trouver le client avec le max
#          (indice : max(dict, key=dict.get) retourne la clé du max)

    meilleur_client = max(ca_par_client, key=ca_par_client.get)
# TODO 9 : afficher "Meilleur client : {nom} avec {montant:.2f}€"
    print(f"Meilleur client : {meilleur_client} avec {ca_par_client[meilleur_client]:.2f}€")


import json
from datetime import datetime

CHEMIN_JSON = 'data/ventes.json'

recap = {
    'genere_le': datetime.now().isoformat(),
    'ca_total': ca_total,
    'nb_ventes': nb_ventes,
    'meilleur_client': {
        'nom': meilleur_client,
        'montant': ca_par_client[meilleur_client]
    },
    'ca_par_client': dict(ca_par_client)
}

with open(CHEMIN_JSON, mode='w', encoding='utf-8') as f:
    json.dump(recap, f, indent=2, ensure_ascii=False)

with open(CHEMIN_JSON, mode='r', encoding='utf-8') as f:
    data = json.load(f)
    chemin = CHEMIN_JSON
    nb_ventes = int(data['nb_ventes'])
    ca_total = float(data['ca_total'])
    print(f"Fichier écrit : {chemin} - {nb_ventes} ventes pour {ca_total:.2f}€")    