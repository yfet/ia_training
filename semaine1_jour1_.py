# ============================================================
# SEMAINE 1 / JOUR 1 — Python pour développeur
# Si tu connais JS/PHP, tu vas reconnaître 90% de ça
# ============================================================

# ── 1. TYPES DE BASE ────────────────────────────────────────
# Pas de déclaration de type, pas de let/const/var
nom = "Tefy"
age = 30
score = 98.5
actif = True

# f-string = template literal JS
print(f"Bonjour {nom}, tu as {age} ans")

# Vérifier le type (utile en ML)
print(type(score))   # <class 'float'>
print(type(actif))   # <class 'bool'>


# ── 2. LISTES (= tableaux JS) ────────────────────────────────
clients = ["Alice", "Bob", "Charlie"]

print(clients[0])        # Alice
print(clients[-1])       # Charlie (dernier élément)
print(clients[1:3])      # ['Bob', 'Charlie'] — slicing

clients.append("David")  # push en JS
clients.remove("Bob")
print(len(clients))      # 3

# List comprehension — très utilisé en ML
scores = [10, 45, 78, 92, 33]
scores_eleves = [s for s in scores if s >= 50]
print(scores_eleves)     # [78, 92]


# ── 3. DICTIONNAIRES (= objets JS) ──────────────────────────
client = {
    "nom": "Alice",
    "age": 28,
    "actif": True,
    "commandes": 14
}

print(client["nom"])           # Alice
print(client["email"])
print(client.get("email", "non renseigné"))  # valeur par défaut

client["email"] = "alice@mail.com"   # ajouter une clé

# Itérer sur un dict
for cle, valeur in client.items():
    print(f"{cle} : {valeur}")


# ── 4. FONCTIONS ─────────────────────────────────────────────
# Syntaxe similaire, pas de function keyword
def calculer_score_client(commandes, actif):
    """Calcule un score de fidélité client."""
    base = commandes * 10
    bonus = 50 if actif else 0
    return base + bonus

score = calculer_score_client(14, True)
print(f"Score : {score}")   # 190

# Valeurs par défaut
def saluer(nom, message="Bienvenue"):
    return f"{message}, {nom} !"

print(saluer("Tefy"))                   # Bienvenue, Tefy !
print(saluer("Tefy", "Bonjour"))        # Bonjour, Tefy !


# ── 5. CLASSES ───────────────────────────────────────────────
# __init__ = constructor, self = this
class Client:
    def __init__(self, nom, age, commandes=0):
        self.nom = nom
        self.age = age
        self.commandes = commandes

    def passer_commande(self):
        self.commandes += 1
        print(f"{self.nom} a passé une commande. Total : {self.commandes}")

    def est_vip(self):
        return self.commandes >= 10
    
    def score_fidelite(self):
        base = self.commandes * 10
        bonus = 50 if self.est_vip() else 0
        return base + bonus

    def __str__(self):
        # équivalent de toString()
        return f"Client({self.nom}, {self.age} ans, {self.commandes} commandes)"


alice = Client("Alice", 28, commandes=12)
alice.passer_commande()
print(alice.est_vip())   # True
print(alice.score_fidelite())  # 170
print(alice)             # Client(Alice, 28 ans, 13 commandes)