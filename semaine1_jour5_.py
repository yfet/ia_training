# ============================================================
# SEMAINE 1 / JOUR 5 — NumPy
# ============================================================

import numpy as np
import csv

CHEMIN_CSV = 'data/ventes.csv'


# ── 1. CONSTRUCTION DE TABLEAUX DEPUIS LE CSV ────────────────
# TODO 1 : lire data/ventes.csv et construire DEUX np.arrays :
#   - quantites  (dtype=int)
#   - prix       (dtype=float)
#
# Indice :
#   quantites_list = []
#   prix_list = []
#   with open(...) as f:
#       reader = csv.DictReader(f)
#       for ligne in reader:
#           quantites_list.append(int(ligne['quantite']))
#           prix_list.append(float(ligne['prix_unitaire']))
#   quantites = np.array(quantites_list)
#   prix = np.array(prix_list)
quantites_list = []
prix_list = []
with open(CHEMIN_CSV) as f:
    reader = csv.DictReader(f)
    for ligne in reader:
        quantites_list.append(int(ligne['quantite']))
        prix_list.append(float(ligne['prix_unitaire']))

quantities = np.array(quantites_list)
prices = np.array(prix_list)

print(f"Quantités : {quantities}")
print(f"Prix :", prices)


# ── 2. OPÉRATIONS VECTORISÉES ────────────────────────────────
# TODO 2 : calculer le tableau `montants = quantites * prix`
#          (UNE seule ligne, pas de boucle)
montants = quantities * prices
print(f"Montants : {montants}")
#
# TODO 3 : afficher
#   "Nombre de ventes : {len}"
#   "CA total : {sum:.2f}€"
#   "Vente moyenne : {mean:.2f}€"
#   "Vente max : {max:.2f}€"
#   "Vente min : {min:.2f}€"
#   "Écart-type : {std:.2f}€"
print(f"Nombre de ventes : {len(montants)}")
print(f"CA total : {montants.sum():.2f}€")
print(f"Vente moyenne : {montants.mean():.2f}€")
print(f"Vente max : {montants.max():.2f}€")
print(f"Vente min : {montants.min():.2f}€")
print(f"Écart-type : {montants.std():.2f}€")


# ── 3. BOOLEAN INDEXING ──────────────────────────────────────
# TODO 4 : trouver les ventes > 100€
#   - créer le masque : masque = montants > 100
#   - filtrer : grosses_ventes = montants[masque]
#   - afficher "Ventes > 100€ : {nombre} ventes pour un total de {sum:.2f}€"
masque = montants > 100
grosses_ventes = montants[masque]
print(f"Ventes > 100€ : {len(grosses_ventes)} ventes pour un total de {grosses_ventes.sum():.2f}€")
#
# TODO 5 : trouver les ventes avec quantité > 1 ET prix > 50
#   (combiner avec & et parenthèses)
masque = (quantities > 1) & (prices > 50)
nb_correspondances = masque.sum()
q_filtre = quantities[masque]
p_filtre = prices[masque]
montants_filtre = montants[masque]
print(f"Ventes avec quantité > 1 ET prix > 50 : {nb_correspondances} ventes")
for q, p, m in zip(q_filtre, p_filtre, montants_filtre):
    print(f"qte : {q} - prix : {p:.2f}€ - montants : {m:.2f}€")



# ── 4. NORMALISATION (pattern ML) ────────────────────────────
# TODO 6 : normaliser le tableau `prix` selon la formule
#   prix_normalise = (prix - prix.mean()) / prix.std()
#   afficher prix_normalise et vérifier que sa moyenne ≈ 0 et son std ≈ 1
prix_normalise = (prices - prices.mean()) / prices.std()
print(f"Prix normalisé : {prix_normalise}")
print(f"Moyenne : {prix_normalise.mean():.2f}")
print(f"Écart-type : {prix_normalise.std():.2f}")

# ── 5. MATRICE 2D ────────────────────────────────────────────
# TODO 7 : construire une matrice 2D `data` de shape (n_ventes, 2)
#          colonne 0 = quantites, colonne 1 = prix
#   indice : np.column_stack([quantites, prix])
data = np.column_stack([quantities, prices])
print(f"Data :{data}")
#
# TODO 8 : afficher
#   - data.shape
#   - la moyenne par colonne (axis=0)
#   - la 3e ligne (3e vente) avec data[2]
print(f"Shape : {data.shape}")
print(f"Moyenne par colonne : {data.mean(axis=0)}")
print(f"3e ligne : {data[2]}")