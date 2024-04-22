import csv

# Lecture du fichier CSV
fichier = open("jo_beijing_2022.csv")
tableau = list(csv.DictReader(fichier, delimiter=','))
fichier.close()

# Filtrage des données
tableau_filtre = []

for ligne in range(1, len(tableau)):
    if int(tableau[ligne]['or']) > 0:
        tableau_filtre.append({'pays': tableau[ligne]['pays'], 'or': tableau[ligne]['or']})


# Tri du tableau
def trier_par_medaille(item):
    return int(item['or'])


tableau_filtre.sort(key=trier_par_medaille, reverse=True)

# Écriture des données dans un nouveau fichier CSV
fichier = open("medailles_or.csv", "w")

w = csv.DictWriter(fichier, fieldnames=['pays', 'or'])
w.writeheader()
w.writerows(tableau_filtre)

fichier.close()
