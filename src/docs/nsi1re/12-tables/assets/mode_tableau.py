import csv

# Lecture du fichier CSV
fichier = open("jo_beijing_2022.csv")
tableau = list(csv.reader(fichier, delimiter=','))
fichier.close()

# Filtrage des données
tableau_filtre = []

for ligne in range(1, len(tableau)):
    if int(tableau[ligne][1]) > 0:
        tableau_filtre.append([tableau[ligne][0], tableau[ligne][1]])


# Tri du tableau
def trier_par_medaille(item):
    return int(item[1])


tableau_filtre.sort(key=trier_par_medaille, reverse=True)

# Écriture des données dans un nouveau fichier CSV
fichier = open("medailles_or.csv", "w")

w = csv.writer(fichier)
w.writerow(['pays', 'or'])
w.writerows(tableau_filtre)

fichier.close()
