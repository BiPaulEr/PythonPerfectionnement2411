prenoms = ["Paul", "Martin", "Pierre", ""]
noms = ["Lefbvre", "Aigouyi", "Dupont"]

nom_complets = []
nom_complets_a_corrige = ["INCONNU", "INCONNU", "INCONNU"]

print(enumerate(prenoms))
print(list(enumerate(prenoms))) #[(0, 'Paul'), (1, 'Martin'), (2, 'Pierre')]

for index, prenom in enumerate(prenoms):
    prenoms[index] = prenom.upper()

print(zip(prenoms, noms))
print(list(zip(prenoms, noms))) #[('PAUL', 'Lefbvre'), ('MARTIN', 'Aigouyi'), ('PIERRE', 'Dupont')]

for prenom, nom in zip(prenoms, noms):
    nom_complets.append(prenom + ' ' + nom)

print(list(enumerate(zip(prenoms, noms))))#[(0, ('PAUL', 'Lefbvre')), (1, ('MARTIN', 'Aigouyi')), (2, ('PIERRE', 'Dupont'))]
for index, (prenom, nom) in enumerate(zip(prenoms, noms)): #ValueError: not enough values to unpack (expected 3, got 2)
    nom_complets_a_corrige[index] = prenom + ' ' + nom

print(prenoms)
print(noms)
print(nom_complets) #['PAUL Lefbvre', 'MARTIN Aigouyi', 'PIERRE Dupont']