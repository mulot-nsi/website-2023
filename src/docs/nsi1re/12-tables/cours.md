# Les données en table

Les exemples donnés ci-après le seront sur la base d'une collection dont les objets sont les médailles remportées
par les pays ayant participés aux jeux olympiques de Beijing de 2022.
Voici un extrait du fichier `jo_beijing_2022.csv` contenant ces informations :

```csv
pays,or,argent,bronze
NORVÈGE,16,8,13
ALLEMAGNE,12,10,4
CHINE,9,4,2
```

[:material-download: `jo_beijing_2022.csv`](assets/jo_beijing_2022.csv){:download="jo_beijing_2022.csv"}


## Lecture du format CSV

Il existe deux méthodes de lecture de données CSV :

- la première lit chaque ligne sous forme d'un tableau indexé ;
- la seconde lit chaque ligne sous forme d'un dictionnaire

!!! example "Lecture de données CSV en mode tableau"

    ```python
    import csv

    fichier = open("jo_beijing_2022.csv") # (1)!
    lecteur_csv = csv.reader(fichier, delimiter=',') # (2)!
    
    for ligne in lecteur_csv: 
        print(ligne) # (3)! 

    fichier.close() # (4)!
    ```

    1. Ouverture du fichier `jo_beijing_2022.csv`
    2. Création d'un lecteur de fichier CSV dont le caractère `,` est utilisé pour séparer les champs
    3. Parcours de chaque ligne du fichier CSV. L'affichage dans la console sera :
       ```
       ['pays','or','argent','bronze']
       ['NORVÈGE', '16', '8', '13']
       ['ALLEMAGNE', '12', '10', '4']
       ...
       ```
    4. Fermeture du fichier `jo_beijing_2022.csv`

    Il est possible de stocker l'intégralité des lignes directement dans une variable en utilisant la fonction `list` :

    ```python
    import csv

    fichier = open("jo_beijing_2022.csv")
    tableau = list(csv.reader(fichier, delimiter=',')) # (1)!
    fichier.close()
    ```

    1. Lecture des données du fichier sous forme d'un **tableau doublement indexé**. La structure de la variable `table` sera :
       ```python
       [
          ['pays','or','argent','bronze']
          ['NORVÈGE', '16', '8', '13'],
          ['ALLEMAGNE', '12', '10', '4'],
          ...
       ]
       ```

!!! example "Lecture de données CSV en mode dictionnaire"

    ```python
    import csv                      

    fichier = open("jo_beijing_2022.csv")
    tableau = list(csv.DictReader(fichier, delimiter=',')) # (1)!
    fichier.close()
    ```

    1. Lecture des données du fichier sous forme d'un **tableau de dictionnaires**. La structure de la variable `table` sera :
       ```python
       [
          {'pays':'NORVÈGE', 'or':'16', 'argent':'8', 'bronze':'13'},
          {'pays':'ALLEMAGNE', 'or':'12', 'argent':'10', 'bronze':'4']},
          ...
       ]
       ```

## Parcours des données

En parcourant les données, il vous sera possible d'accéder aux données de chaque ligne et de mettre en oeuvre les
traitements de votre choix (affichage, recherche d'une valeur, calculs, ...)
Pour illustrer le parcours de données, affichons la liste des pays ayant obtenu au moins une médaille d'or.

!!! example "En mode tableau"

    ```python
    import csv
    
    fichier = open("jo_beijing_2022.csv")
    tableau = list(csv.reader(fichier, delimiter=','))
    fichier.close()
    
    # Parcours le tableau depuis l'indice 1 pour ignorer la ligne d'en-têtes
    for ligne in range(1, len(tableau)):
        # Le nombre de médailles d'or est en seconde colonne, donc d'indice 1
        # Conversion en int car toutes les données ont été lues par csv.reader() comme des chaînes
        if int(tableau[ligne][1]) > 0:
            print(tableau[ligne][0])
    ```

!!! example "En mode dictionnaire"

    ```python
    import csv
    
    fichier = open("jo_beijing_2022.csv")
    tableau = list(csv.DictReader(fichier, delimiter=','))
    fichier.close()
    
    for ligne in range(len(tableau)):
        if int(tableau[ligne]['or']) > 0:
            print(tableau[ligne]['pays'])
    ```

## Filtrage des données

Vous pourriez avoir besoin d'affiner les données en supprimant des lignes ou des colonnes superflues.
Pour illustrer le filtrage des données, nous allons créer une nouvelle liste ne contenant que les pays ayant obtenu au
moins une médaille d'or.
Nous ne conserverons comme colonnes que le nom du pays et le nombre de médailles d'or.

!!! example "En mode tableau"

    ```python
    tableau_filtre = []
    
    for ligne in range(1, len(tableau)):
        if int(tableau[ligne][1]) > 0:
            tableau_filtre.append([tableau[ligne][0], tableau[ligne][1]])
    ```

!!! example "En mode dictionnaire"

    ```python
    tableau_filtre = []
    
    for ligne in range(1, len(tableau)):
        if int(tableau[ligne]['or']) > 0:
            tableau_filtre.append({'pays': tableau[ligne]['pays'], 'or': tableau[ligne]['or']})
    ```

## Tri de données

Vous pourriez avoir besoin de trier les données en fonction d'une colonne et vouloir choisir si ce tri est croissant ou
décroissant.
Pour illustrer le tri des données, nous allons trier le tableau des données filtrées dans l'ordre décroissant des
médailles d'or.

!!! example "En mode tableau"

    ```python
    def trier_par_medaille(item):
        return int(item[1])
    
    tableau_filtre.sort(key=trier_par_medaille, reverse=True)
    ```

!!! example "En mode dictionnaire"

    ```python
    def trier_par_medaille(item):
        return int(item['or'])
    
    tableau_filtre.sort(key=trier_par_medaille, reverse=True)
    ```

## Écriture au format CSV

Nous souhaitons maintenant enregistrer le résultat de nos traitements dans un nouveau fichier CSV.

!!! example "En mode tableau"

    ```python
    fichier = open("medailles_or.csv", "w")
    
    w = csv.writer(fichier)
    w.writerow(['pays', 'or'])
    w.writerows(tableau_filtre)
    
    fichier.close()
    ```
    
    Téléchargement du code complet : [:material-download: mode_tableau.py](assets/mode_tableau.py){:download="mode_tableau.py"}


!!! example "En mode dictionnaire"

    ```python
    fichier = open("medailles_or.csv", "w")
    
    w = csv.DictWriter(fichier, fieldnames=['pays', 'or'])
    w.writeheader()
    w.writerows(tableau_filtre)
    
    fichier.close()
    ```

    Téléchargement du code complet : [:material-download: mode_dictionnaire.py](assets/mode_dictionnaire.py){:download="mode_dictionnaire.py"}