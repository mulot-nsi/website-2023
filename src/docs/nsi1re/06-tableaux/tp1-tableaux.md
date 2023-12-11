---
title: TP1 - Les tableaux
description: Manipulation de tableaux et premiers algorithmes
---

# Les tableaux

## Introduction

Vous avez jusqu'à présent travaillé uniquement avec les **types primitifs** du langage Python à savoir : les booléens, les entiers, les flottants et les chaînes de caractères.
Vous allez maintenant étudier votre premier **type construit** : les tableaux.

!!! info "Définition"
    
    Un type construit est un type de données capable de contenir plusieurs valeurs.

!!! danger "Important"

    Les productions réalisées dans le cadre de ce TP seront à rendre en fin de séance.

## Préparation

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et
travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers** 
           <span class="keys shortcut"><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>E</kbd></span>
        2. Dans le dossier `Document`, s'il n'y a pas de dossier nommé `NSI`, créez-le
        4. Dans le dossier `NSI`, s'il n'y a pas de dossier `chapitre_06`, créez-le
        5. Dans le dossier `chapitre_06` créez le dossier `tp1`

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans la **zone personnelle**, s'il n'y a pas de dossier `NSI`, créez-le
        3. Dans le dossier `NSI`, s'il n'y a pas de dossier `chapitre_06`, créez-le
        4. Dans le dossier `chapitre_06` créez le dossier `tp1`

### Téléchargement

Pour réaliser ces travaux pratiques, il est nécessaire de disposer de certains fichiers.

!!! note "Récupération des fichiers"

    1. Téléchargez le fichier ZIP contenant les fichiers nécessaires : [:material-download: télécharger](assets/NSI1RE06_TP1.zip){:download="NSI1RE06_TP1.zip"}
    2. Ouvrez le fichier ZIP<br>*(si le navigateur ne l'ouvre automatiquement, cliquez sur le fichier téléchargé)*
    3. Sélectionnez tous les fichiers et dossiers  <span class="shortcut">++ctrl+a++</span>
    4. Copiez tous les fichiers et dossiers <span class="shortcut">++ctrl+c++</span>
    5. Collez les fichiers dans le dossier `NSI\chapitre_06\tp1` <span class="shortcut">++ctrl+v++</span>


## Découverte des tableaux

### 1.1. Expérimentation

Dans une [:material-link: console Python](https://console.basthon.fr/){:target="_blank"}, identifier les commandes permettant de répondre aux points listés ci-après.
Les **commandes** trouvées devront être reportées dans le fichier `ex11_console.py`.

!!! note "Instructions"

    1. Affectez à une variable nommée `premiers`, un tableau contenant les nombres premiers de 2 à 11 inclus
    2. Vérifiez le contenu de la variable `premiers`
    3. Récupérez la taille du tableau `premiers`
    4. Récupérez la première valeur du tableau `premiers`
    5. Récupérez la valeur d'indice 2 du tableau `premiers`
    6. Récupérez la valeur du 4<sup>ème</sup> élément du tableau `premiers`
    7. Récupérez la valeur du dernier élément du tableau `premiers` en utilisant la fonction `#!python len()`
    8. Affectez la valeur `#!python 101` au premier élément du tableau `premiers`

### 1.2. Génération d'un tableau

Vos observations et conclusions seront à rédiger sous forme de commentaires Python dans le fichier nommé `ex12_generation.py`.

!!! note "Instructions"

    Testez les deux expressions ci-dessous dans la console Python :

    ```python
    # Première expression
    [0] * 4
    
    # Seconde expression
    [0, 1] * 4
    ```

!!! question "Question"

    Quel est l'effet de l'opérateur `*` entre un tableau et un entier ?



### 1.3. Stockage en mémoire

Écrire dans le fichier `ex13_stockage.py` le programme Python correspondant aux instructions ci-dessous.
**Attention, n'exécuter le programme que lorsque cela est explicitement demandé**.

!!! note "Instructions"

    1. Affectez à une variable `v1` la chaîne de caractères `"A"`
    2. Affectez à une variable `v2` la variable `v1`
    3. Affectez la chaîne de caractères `#!python "B"` à la variable `v2`
    4. Affichez la valeur des variables `v1` et `v2` à l'aide d'un unique appel à la fonction `#!python print()`
    5. Ajoutez en commentaire la réponse à la **question 1**
    6. Exécutez le programme

!!! question "Question 1"
    
    Quelles valeurs anticipez-vous pour les variables `v1` et `v2` ?

!!! note "Instructions"

    1. Continuez le programme en affectant à une variable `t1` le tableau `#!python ['A', 'B', 'C']`
    2. Affectez à la variable `t2` la variable `t1`
    3. Affectez la chaîne de caractères `#!python "D"` au premier élément de la variable `t2`
    4. Affichez la valeur des variables `t1` et `t2` à l'aide d'un unique appel à la fonction `print()`
    5. Ajoutez en commentaire la réponse à la **question 2**
    6. Exécutez le programme

!!! question "Question 2"
    
    Quelles valeurs anticipez-vous pour les variables `t1` et `t2` ?


### 1.4. Visualisation de la mémoire

Vous n'arrivez pas à comprendre le résultat de l'exercice précédent ?
Afin de découvrir ce qui se déroule en mémoire, vous avez deux possibilités :

??? note "Python Tutor"

    1. Rendez-vous sur le site [www.pythontutor.com](https://pythontutor.com/python-debugger.html#mode=edit){:target="_blank"}
    2. Choisissez le langage Python
    3. Copier/coller le code ci-dessous :
        ```python
        v1 = "A"
        v2 = v1
        v2 = "B"
        
        t1 = ["A", "B", "C"]
        t2 = t1
        t2[0] = "D"
        ```

    4. Cliquez sur **Visualize Execution**
    5. Cliquez sur **Next** pour exécuter le programme pas-à-pas et observer l'évolution de la mémoire

??? note "Thonny"

    1. Copier/coller le code ci-dessous dans Thonny :
        ```python
        v1 = "A"
        v2 = v1
        v2 = "B"
        
        t1 = ["A", "B", "C"]
        t2 = t1
        t2[0] = "D"
        ```
    2. Affichez les fenêtres **Allocation mémoire** et **Variables**
    3. Lancez le programme et observez les adresses mémoire des variables `t1` et `t2`

!!! question "Question 4"

    Quelle explication donnez-vous maintenant au phénomène observé de l'exercice 1.3 ?
    Répondez par un commentaire à la fin du fichier `ex13_stockage.py`.




## Parcours des tableaux

### 2.1. Parcours simples

Soit trois tableaux `t1`, `t2` et `t3` :

```python
t1 = ['(\\(\\','(-.-)','c(")(")']
t2 = ["'___'","(0,0)","/)_)",' ""']
t3 = ["  __", "<(o )___", " ( ._> /", "  `---'"]
```

Nous souhaitons afficher le contenu de ces tableaux selon trois parcours différents :
le parcours par valeur, le parcours par indice à l'aide d'une boucle bornée et une boucle non bornée.
Le code devra être saisi dans le fichier `ex21_parcours.py`, les tableaux y sont déjà présents.

!!! note "Instructions"

    1. Affichez les valeurs du tableau `t1` en utilisant un **parcours par valeur**
    2. Affichez les valeurs du tableau `t2` en utilisant un parcours par indice à l'aide d'une **boucle bornée**
    3. Affichez les valeurs du tableau `t3` en utilisant un parcours par indice à l'aide d'une **boucle non bornée**

??? info "Parcours d'un tableau"

    === "Parcours par valeur"
        
        ```python
        for valeur in tableau :
            ...
        ```

    === "Parcours par indice (borné)"

        ```python
        for i in range(len(tableau)) :
            ...
        ```

    === "Parcours par indice (non borné)"

        ```python
        i = 0
        while i < len(tableau) :
            ...
            i = i + 1
        ```

### 2.2. Fonction somme

Nous souhaitons disposer de la fonction `somme` ayant pour paramètre un tableau d'entiers nommé `entiers`.
Cette fonction calcule et renvoie la somme des entiers du tableau.

```text
>>> somme([1, 2, 3])
6
```

!!! note "Instructions"

    1. Écrivez le code de la fonction dans le fichier `ex22_somme.py`
    2. Écrivez la *docstring* de la fonction
    3. Écrivez les *doctest* que vous jugerez pertinents
       *(voir [:material-link: Chapitre 4 - Programmation défensive](../04-fonctions/tp2-programmation-defensive.md){:target="_blank"})*
    4. Testez la fonction en utilisant uniquement les *doctests*


## Problème

Les exercices de cette partie sont liés. L'ensemble du code devra être écrit dans un seul et unique fichier.

### 3.1. Les températures
En région parisienne, les températures moyennes en degrés, de janvier à décembre 2021, étaient les suivantes :

!!! info "Températures"

    <figure>
        <table>
            <tr>
                <th style="min-width:0;text-align:center;">J</th>
                <th style="min-width:0;text-align:center;">F</th>
                <th style="min-width:0;text-align:center;">M</th>
                <th style="min-width:0;text-align:center;">A</th>
                <th style="min-width:0;text-align:center;">M</th>
                <th style="min-width:0;text-align:center;">J</th>
                <th style="min-width:0;text-align:center;">J</th>
                <th style="min-width:0;text-align:center;">A</th>
                <th style="min-width:0;text-align:center;">S</th>
                <th style="min-width:0;text-align:center;">O</th>
                <th style="min-width:0;text-align:center;">N</th>
                <th style="min-width:0;text-align:center;">D</th>
            </tr>
            <tr>
                <td style="min-width:0;text-align:center;">4,6</td>
                <td style="min-width:0;text-align:center;">6,5</td>
                <td style="min-width:0;text-align:center;">5,6</td>
                <td style="min-width:0;text-align:center;">10,0</td>
                <td style="min-width:0;text-align:center;">11,3</td>
                <td style="min-width:0;text-align:center;">14,4</td>
                <td style="min-width:0;text-align:center;">15,7</td>
                <td style="min-width:0;text-align:center;">17,6</td>
                <td style="min-width:0;text-align:center;">14,5</td>
                <td style="min-width:0;text-align:center;">10,3</td>
                <td style="min-width:0;text-align:center;">7,3</td>
                <td style="min-width:0;text-align:center;">5,2</td>
            <tr>
        </table>
    </figure>

Nous souhaitons étudier ces données en Python. Pour cela, les températures seront stockées sous forme d'un tableau de flottants.

!!! note "Instructions"

    1. Lancez Thonny
    2. Ouvrez le fichier `meteo.py`
    3. Complétez le tableau `temperatures_2021` avec l'ensemble des températures moyennes de 2021
    4. Lancez le programme et vérifiez le contenu de la variable `temperatures_2021`


### 3.2. Rapport des températures

Nous souhaitons afficher les températures à l'écran de la manière suivante :

```
Janvier : 4.6
Février : 6.5
...
Novembre : 7.3
Décembre : 5.2
```

<h4>Affichage des mois</h4>

!!! note "Instructions"
    1. Écrivez une fonction `rapport` ayant pour paramètre un tableau `temperatures`
    2. Ajoutez au corps de la fonction `rapport`, le tableau `mois` contenant le nom de chaque mois de l'année :
       ```python
       ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
       ```
    3. Ajoutez au corps de la fonction `rapport` le code nécessaire à l'affichage des mois de l'année
    4. Ajouter un appel à la fonction `rapport` avec pour argument le tableau des températures de l'année 2021
    5. Vérifiez le bon fonctionnement de l'ensemble

??? success "Résultat attendu"
    ```
    Janvier
    Février
    Mars
    Avril
    Mai
    Juin
    Juillet
    Août
    Septembre
    Octobre
    Novembre
    Décembre
    ```

<h4>Affichage des moyennes par mois</h4>

!!! note "Instructions"
    Modifiez la fonction `rapport` de façon à afficher la température moyenne en face de chaque mois.
    L'affichage doit être similaire à celui présenté en début d'exercice.

??? success "Résultat attendu"
    ```
    Janvier : 4.6
    Février : 6.5
    Mars : 5.6
    Avril : 10.0
    Mai : 11.3
    Juin : 14.4
    Juillet : 15.7
    Août : 17.6
    Septembre : 14.5 
    Octobre : 10.3
    Novembre : 7.3
    Décembre : 5.2
    ```

### 3.3. Moyenne annuelle

Nous souhaitons calculer la température moyenne annuelle. À cet effet, voici l'algorithme de calcul d'une moyenne à partir d'un tableau d'entiers ou de flottants :

```
Entrée : un tableau d'entiers ou de flottants tab
Sortie : le résultat du calcul de la moyenne

Début
 |  total ← 0
 |
 |  pour chaque valeur v du tableau tab faire
 |   |  total ← total + v
 |  fin pour chaque
 |
 |  renvoyer total / taille(tab)
Fin
```

!!! note "Instructions"

    1. Écrivez la fonction `moyenne` implémentant cet algorithme.
    2. Modifiez la fonction `rapport` pour à ajouter la ligne « Température moyenne annuelle : *t* » où *t* est la température moyenne renvoyée par la fonction `moyenne`

??? success "Résultat attendu"

    ```
    Janvier : 4.6
    Février : 6.5
    Mars : 5.6
    Avril : 10.0
    Mai : 11.3
    Juin : 14.4
    Juillet : 15.7
    Août : 17.6
    Septembre : 14.5 
    Octobre : 10.3
    Novembre : 7.3
    Décembre : 5.2
    Température moyenne annuelle : 10.249999999999998
    ```

### 3.4. Maximum

Nous souhaitons connaître la température moyenne la plus élevée sur l'année.
Pour cela, nous aurions besoin d'une fonction renvoyant le maximum (la plus grande valeur) d'un tableau dont l'algorithme reste à définir :

```
Entrée : un tableau d'entiers ou de flottants tab
Sortie : le maximum

Début
 |
 |  ?
 |
 |  renvoyer ?
Fin
```

!!! note "Instructions"

    - Écrivez un algorithme permettant de trouver la plus grande valeur d'un tableau non vide d'entiers ou de flottants
    - Écrivez une fonction `maximum` implémentant votre algorithme en ajoutant votre algorithme à la *docstring*
    - Modifiez la fonction rapport de façon à ajouter la ligne « Température moyenne maximale : *t* » où *t* est la température maximale renvoyée par la fonction `maximum`

??? success "Résultat attendu"

    ```
    Janvier : 4.6
    Février : 6.5
    Mars : 5.6
    Avril : 10.0
    Mai : 11.3
    Juin : 14.4
    Juillet : 15.7
    Août : 17.6
    Septembre : 14.5 
    Octobre : 10.3
    Novembre : 7.3
    Décembre : 5.2
    Température moyenne annuelle : 10.249999999999998
    Température moyenne maximale : 17.6
    ```


## Conclusion

### Envoi du travail

Suivez les instructions ci-dessous afin d'envoyer votre travail via Pronote.

!!! note "Dépôt d'une copie sur Pronote"

    1. Compressez votre dossier `NSI\chapitre_06\tp1` au format **ZIP**
    2. Connectez-vous à l'**ENT** : [https://ent.iledefrance.fr](https://ent.iledefrance.fr){:target="_blank"}
    3. Accédez à l'application **Pronote**
    4. Depuis l'accueil, recherchez le devoir **NSI1RE06 - TP1 - Tableaux**
    5. Cliquez sur le bouton **Déposer ma copie**{:style="display:inline-block;color:#4a1b7f;background-color:#ebdbff;padding:5px 20px;border-radius:10px;"}
    6. Cliquez sur le bouton **Un seul fichier (*.pdf, *.doc, ...)**
    7. Déposez votre fichier ZIP

### Bonus - Nombres premiers

Vous avez terminé les travaux pratiques ? Écrire la fonction `premiers` qui prend en paramètre un entier `n` et qui renvoie un tableau contenant les `n` premiers nombres premiers.

```
>>> premiers(5)
[2, 3, 5, 7, 11]
```