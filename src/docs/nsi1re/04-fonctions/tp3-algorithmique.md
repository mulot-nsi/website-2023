---
title: Algorithmique
description: Introduction à l'algorithmique
---

# Algorithmique

## Introduction



## 🧠 Partie 3 - Algorithmique

### Exercice 5 - Carré ASCII

#### Objectif
Un algorithme est la description d'une suite d'étapes permettant d'obtenir un résultat à partir d'éléments fournis en entrée (*source : [CNIL](https://www.cnil.fr/fr/definition/algorithme)*).
Cet exercice a pour objectif de vous inciter à réfléchir aux algorithmes avant toute écriture de code.

Dans le cas présent, vous devez cerner la logique derrière la construction d'un carré de taille *n* à l'aide du caractère # et du caractère d'espacement.
Une fois la logique trouvée, vous devez être capable d'en déduire un algorithme et exprimer celui-ci en français en pseudo-code.

##### Exemple en français avec la multiplication (exercice 3) :
```
Initialiser une variable "total" à 0
Affecter y fois à total la valeur de total + x
Renvoyer total
```

##### Exemple en pseudo-code avec la multiplication (exercice 3) :
```
total ← 0
Répéter y fois :
  total ← total + x
renvoyer total
```

#### Consigne
Nous souhaitons disposer d'une fonction `afficher_carre` prenant un paramètre `n` un entier correspondant à la taille du carré.
Cette fonction une fois appelée avec une taille passée en argument, affiche un carré respectant cette taille dans la console Python.

```text
n=1   n=2    n=3      n=4
 #    # #   # # #   # # # #
      # #   #   #   #     #
            # # #   #     #
                    # # # #
```

- Enregistrer le code dans un fichier fichier `ex5_carree.py`
- Écrire dans la docstring l'algorithme permettant d'afficher un carré de taille $n$
- Écrire la fonction `afficher_carre`

### Exercice 6 - Triangle ASCII (bonus)

Sur le même principe que l'exercice 5, nous souhaitons disposer d'une fonction `afficher_triangle` prenant un paramètre `h` un entier correspondant à la hauteur du triangle.
Cette fonction une fois appelée avec une taille passée en argument, affiche un triangle respectant cette hauteur dans la console Python.

```text
h=1    h=2      h=3
 #      #        #
###    # #      # #
      #####    #   #
              #######
```

- Enregistrer le code dans un fichier fichier `ex5_carree.py`
- Écrire dans la docstring l'algorithme permettant d'afficher un triangle de hauteur `h`
- Écrire la fonction `afficher_triangle`