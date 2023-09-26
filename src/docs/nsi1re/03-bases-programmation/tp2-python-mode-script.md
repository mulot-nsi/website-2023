---
title: Chapitre 3 - Bases de la programmation - TP2 Python en mode script
description: Découverte du langage Python à travers son mode script
---

# Python en mode script

## Calculateur d'âge

### Étape 1 - Afficher l'âge

Écrire un programme Python qui, à partir d'une année de naissance, calcule l'âge d'un individu en 2022.

```
Indique ton année de naissance : 2000
Tu as 22 ans.
```


???info "Obtenir une saisie clavier"
    
    En Python, La fonction `input()` permet de lire des données saisies au clavier (*entrée standard* par défaut).
    Celles-ci sont renvoyée par la fonction sous forme d'une chaîne de caractères.

    ```
    >>> nom = input("Quel est ton nom ? ")
    Quel est ton nom ? Jean
    >>> nom
    'Jean'
    ```

    [Voir la documentation](https://docs.python.org/fr/3.8/library/functions.html#input)


???info "Afficher une chaîne de caractères à l'écran"

    En Python, la fonction `print()` permet d'afficher du texte à l'écran (*sortie standard* par défaut).
    Chaque argument transmis à la fonction est automatiquement converti en chaîne de caractères.
    Ils sont ensuite affiché à l'écran séparés par un caractère d'espacement.
    
    Voici un exemple d'appel de la fonction `print()` avec cinq arguments :
    
    ```
    >>> nom = "Jean"
    >>> age = 20
    >>> print("Bonjour", nom, "tu as", age, "ans")
    Bonjour Jean tu as 20 ans
    ```
    
    Voici un autre exemple d'appel avec un seul argument.
    Cette fois, nous avons construit nous-même le texte à afficher en utilisant la concaténation.
    Noter qu'il est nécessaire de convertir manuellement certaines données en chaîne de caractères grâce à la fonction `str()`
    
    ```
    >>> nom = "Jean"
    >>> age = 20
    >>> texte = "Bonjour " + nom + " tu as " + str(age) + " ans"
    >>> print(texte)
    Bonjour Jean tu as 20 ans
    ```
    
    [Voir la documentation](https://docs.python.org/fr/3.8/library/functions.html#print)

### Étape 2 - Préciser la majorité

#### Consigne

Modifier le programme précédent de manière à indiquer si l'individu est mineur ou majeur.
Si l'individu est mineur, afficher en supplément l'année à laquelle il deviendra majeur.

```
Indique ton année de naissance : 2000
Tu as 22 ans et tu es majeur(e)
```

```
Indique ton année de naissance : 2010
Tu as 12 ans et tu es mineur(e)
Tu seras majeur(e) en 2028
```

#### Documentation

<details>
<summary>💡 Utiliser les structures conditionnelles</summary>

Rappel de la syntaxe des structures conditionnelles en Python :

```python
if x > 0:
    texte = "x est strictement positif"
```

```python
if x > 0:
    texte = "x est strictement positif"
else:
    texte = "x est négatif ou nul"
```

```python
if x > 0:
    texte = "x est strictement positif"
elif x==0:
    texte = "x est nul"
else:
    texte = "x est strictement négatif"
```

[Voir le tutoriel](https://docs.python.org/fr/3.8/tutorial/controlflow.html#if-statements)<br/>
[Voir la documentation](https://docs.python.org/fr/3.8/library/functions.html#input)
</details>

### Étape 3 - Vérifier la saisie de l'utilisateur

#### Consigne

Le programme n'effectue actuellement aucune vérification de la saisie de l'utilisateur ce qui entrainer certains problèmes :

- la saisie d'une année supérieure à l'année en cours entraine l'affichage d'âges négatifs
- la saisie de valeurs non numériques provoque une anomalie

Modifier votre programme de façon à ce que le programme s'interrompt si :

- année saisie > 2022
- année saisie < 1900
- année saisie n'est pas une valeur numérique

```
Indique ton année de naissance : 2040
Erreur, saisir une année comprise entre 1900 et 2022
```

```
Indique ton année de naissance : 850
Erreur, saisir une année comprise entre 1900 et 2022
```

```
Indique ton année de naissance : hello
Erreur, saisir une année comprise entre 1900 et 2022
```


#### Documentation

<details>
<summary>💡 Vérifier si une chaîne ne contient que des caractères numériques (hors programme)</summary>

Avant de convertir une chaîne de caractères en un nombre (`int` ou `float`), il est possible de vérifier au préalable que celle-ci ne contienne uniquement des caractères numériques.
Ceci est possible grâce à la méthode `isdigit()` associée type `str`.

```
>>> "12".isdigit()
True
>>> "douze".isdigit()
False
>>> "-12".isdigit()
False
>>> "10.5".isdigit()
False
>>> nombre = "12"
>>> nombre.isdigit()
>>> True
```

[Voir la documentation](https://docs.python.org/fr/3.8/library/stdtypes.html?highlight=isdigit#str.isdigit)
</details>

<details>
<summary>💡 Interrompre l'exécution d'un programme (hors programme)</summary>

Si votre programme se trouve dans un état impropre à la poursuite de son exécution, vous pouvez en forcer la fin grâce à la fonction `exit()`.
Celle-ci prend optionnellement en argument une chaîne de caractères correspondant au message à afficher.

```python
x = int(input("Saisir un nombre différent de zéro : "))
if x == 0:
    exit("Erreur, x = 0")

print("10 /", x, "=", 10/x)
```

[Voir la documentation](https://docs.python.org/fr/3.8/library/sys.html#sys.exit)
</details>

## 🌊 Les états physiques de l'eau

Écrire un programme Python qui, à partir de la saisie d'une valeur de température, indique l'état de l'eau comme suit :

- gazeux si température >= 100
- liquide si température < 100 et > 0
- solide si température <= 0

```
Saisir une température : 120
L'eau est à l'état gazeux
```

```
Saisir une température : 10
L'eau est à l'état liquide
```

```
Saisir une température : -10
L'eau est à l'état solide
```

:::caution Attention
- Il n'est pas nécessaire de vérifier la saisie de l'utilisateur pour cet exercice
- Ne pas utiliser les opérateurs booléens `not`, `and` et `or`
:::

## 🔎 Le nombre secret

Nous souhaitons recréer en Python le jeu consistant à deviner un nombre choisi aléatoirement entre 0 et 100.

### Étape 1 - Obtenir une valeur aléatoire

#### Consigne
Écrire un programme stockant en mémoire un entier aléatoire compris entre 0 et 100 et l'affichant à l'écran.
La valeur choisie par l'ordinateur est affichée pour des raisons de débogage. Celle-ci devra être masquée une fois le développement du jeu terminé.

#### Documentation

<details>
<summary>💡 Obtenir un entier pseudo-aléatoire</summary>

Il est possible d'obtenir un entier aléatoire grâce à la fonction `randint()` du module `random`.
Ci-dessous, un exemple d'appel de la fonction `randint()` pour obtenir un entier aléatoire `N` tel que `1 <= N <= 6`.

```
>>> import random
>>> random.randint(1, 6)
4
>>> random.randint(1, 6)
1
>>> random.randint(1, 6)
2
>>> random.randint(1, 6)
6
```

[Voir la documentation](https://docs.python.org/fr/3.8/library/random.html?highlight=randint#random.randint)
</details>


### Étape 2 - Obtenir le choix du joueur

#### Consigne
Modifier le programme de manière à demander à l'utilisateur de saisir un nombre.
La saisie devra se répéter tant que le joueur n'a pas trouvé le nombre aléatoire conservé en mémoire.
Les indications *"Plus petit"* ou *"plus grand"* seront affichées après chaque saisie pour guider le joueur.

```
42
Saisir un nombre : 10
Plus grand
Saisir un nombre : 50
Plus petit
Saisir un nombre : 42
Bravo !
```

#### Documentation

<details>
<summary>💡 Les boucles non bornées</summary>

Rappel de la syntaxe Python des boucles `while`, ou boucles non bornées :

```python
# Affichage des entiers de 1 à 10.
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

[Voir le tutoriel](https://docs.python.org/fr/3.8/tutorial/introduction.html#first-steps-towards-programming)<br/>
[Voir la documentation](https://docs.python.org/fr/3.8/reference/compound_stmts.html?highlight=while#while)
</details>

### Étape 3 - Affiner les messages

#### Consigne
Modifier le programme de manière à apporter des indications supplémentaires à l'utilisateur s'il s'approche de l'entier à trouver :

- Si l'écart entre la valeur de l'utilisateur et celle à trouver est inférieure ou égale à 10, afficher *"tu chauffes !"*
- Si l'écart entre la valeur de l'utilisateur et celle à trouver est inférieure ou égale à 2, afficher *"tu brûles !"*

Le programme sera également modifié de manière à compter le nombre de tentatives et l'afficher à la fin du jeu.
Une fois, les développements terminés, ne plus afficher la valeur stockée en mémoire.

Voici un exemple d'exécution si le nombre à trouver est 42 :

```
Saisir un nombre : 10
Plus grand
Saisir un nombre : 60
Plus petit
Saisir un nombre : 50
Plus petit, tu chauffes !
Saisir un nombre : 40
Plus grand, tu brûles !
Saisir un nombre : 42
Bravo ! Tu as trouvé en 5 tentatives
```

<details>
<summary>💡 Obtenir la valeur absolue d'un nombre</summary>

La fonction Python permettant d'obtenir la valeur d'un nombre est `abs()`. Exemple :

```
>>> abs(-10)
10
>>> abs(10 - 12)
2
>>> abs(10 - 8)
2
```

[Voir la documentation](https://docs.python.org/fr/3.8/library/functions.html?highlight=abs#abs)
</details>