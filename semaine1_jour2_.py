# Syntaxe 1 - imnport du module entier
import math
print(math.pi)
print(math.sqrt(16))

# Syntaxe 2 - import avec alias
import math as m
print(m.pi)

#Syntaxe 3 - import sélectif
from math import pi, sqrt
print(pi)
print(sqrt(25))

#Syntaxe 4 - import de tout
from math import *
print(cos(0))

import requests

#TODO 1 faire un get vers github
response = requests.get('https://api.github.com/users/yfet')

#TODO 2 verifier le status code
if response.status_code == 200:
    print('Requête réussie')
else:
    print('Erreur lors de la requête')

#TODO 3 récuperer le JSON de la réponse
data = response.json()
print(f"Réponse JSON: {data}")

#TODO 4 afficher le nom et le nombre de repos publics
print(f"Nom: {data['name']}")
print(f"Nombre de repos publics: {data['public_repos']}")