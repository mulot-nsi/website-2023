---
sidebar_position: 2
sidebar_label: TP2 - Tests et algorithmique
description: Programmation défensive
slug: /nsi-1re/fonctions/tp2-tests-et-algorithmique
---

# Tests et algorithmique

## 🤖 Partie 1 - Automatisation des tests

### Exercice 1 - Module doctest

#### Objectif
Cet exercice a pour objectif de vous faire découvrir une technique d'automatisation des tests d'une fonction.
Vous utiliserez à cet effet le module [doctest](https://docs.python.org/fr/3.10/library/doctest.html) qui permet d'écrire des instructions de test directement dans la [docstring](https://peps.python.org/pep-0257/).

Pour expérimenter ce module, vous devrez écrire la fonction `salutation` qui prend en paramètre le code d'une langue au format [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1) qui renvoie la formule de salutation correspondant à celle-ci.
Vous ne prendrez en compte que les langues listées dans le tableau ci-après.
Si le code de la langue passé en argument n'est pas reconnu, le formule anglaise sera envoyée par défaut.

| Code ISO 639-1      | Formule |
|---------------------|---------|
| `en` *(par défaut)* | Hello   |
| `fr`                | Salut   |
| `es`                | Hola    |


#### Phase préparatoire
1. Créer le dossier `tp2_tests` dans votre dossier `NSI/chapitre_04`
2. Lancer le logiciel Thonny
3. Créer un nouveau fichier `CTRL+N`
3. Récupérer le code ci-dessous et l'enregistrer dans un fichier nommé `ex1_salutation.py`

```python
def salutation(langue):
    """
    Renvoie le formule de salutation propre une langue donnée.

    langue -- Chaîne au format ISO 639-1
    """
    pass
```

#### Première implémentation
Écrire à la place de `pass` le code de la fonction `salutation` en ne prenant en compte que les langues `fr` et `es` pour le moment. L'anglais sera pris en charge dans un second temps.
Vous effectuerez tous vos tests **uniquement** dans la console Python.
Le fichier `ex1_salutation.py` ne contiendra donc que la définition de la fonction `salutation` et rien d'autre.

Voici ce que vous devriez obtenir dans la console Python :

```
>>> salutation("fr")
'Salut'
>>> salutation("es")
'Hola'
```

:::tip Les raccourcis clavier
Pour plus d'efficacité, notamment en l'absence de souris, faites usage des raccourcis clavier proposés par Thonny.
Vous trouvez ci-dessous les plus utiles dans le cadre cet exercice.

- Enregistrer le script courant `Ctrl+S`
- Exécuter le script courant `F5`
- Placer le curseur dans l'éditeur `Alt+E`
- Placer le curseur dans la console `Alt+S`
- Récupérer les précédentes commandes saisies `flèche haut`
:::

#### Intégration des tests
Vous allez maintenant modifier le fichier `ex1_salutation.py` de façon à ajouter les tests.
Modifier la docstring en récupérant la nouvelle version ci-après. Vous constaterez que l'écriture des tests
consiste à simplement recopier ce que vous pourriez obtenir en effectuant les tests manuellement depuis la console Python.

```python
def salutation(langue):
    """
    Renvoie le formule de salutation propre une langue donnée.

    langue -- Chaîne au format ISO 639-1

    >>> salutation('fr')
    'Salut'
    >>> salutation('es')
    'Hola'
    >>> salutation('en')
    'Hello'
    >>> salutation('??')
    'Hello'
    """
```

Ajouter ensuite le code suivant d'appel à la bibliothèque doctest à la fin du fichier `ex1_salutation.py`.

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

#### Exécution des tests
Pour lancer les tests, exécuter simplement le programme. Vous devriez obtenir l'affichage console suivant :

```text
**********************************************************************
File "exercice1.py", line 12, in __main__.salutation
Failed example:
salutation('en')
Expected:
'Hello'
Got nothing
**********************************************************************
File "exercice1.py", line 14, in __main__.salutation
Failed example:
salutation('??')
Expected:
'Hello'
Got nothing
**********************************************************************
1 items had failures:
2 of   4 in __main__.salutation
***Test Failed*** 2 failures.
```

#### Implémentation complète
Terminer d'écrire le code de la fonction `salutation` en prenant en charge la langue anglaise, sans oublier de l'utiliser comme langue par défaut.
Si votre implémentation est correcte, l'exécution de votre programme ne devrait plus entrainer l'affichage de tests en erreur dans la console.

### Exercice 2 - Initiales

#### Objectif
Cet exercice a pour objectif de vous faire appliquer les concepts découverts dans le cadre de l'exercice précédent.
Vous devrez implémenter une fonction, en écrire la documentation et les tests.

#### Consigne
Écrire la fonction `initiales` prenant en paramètre un prénom et un nom et renvoyant les initiales en majuscule.
On ne prendra en compte que la première lettre du prénom et du nom même s'il s'agit d'un prénom composé ou de plusieurs noms.
Voici un exemple d'appel de la fonction depuis la console Python :

```text
>>> initiales("grace", "Hopper")
'GH'
```

- Enregistrer le code dans un fichier nommé `ex2_initiales.py`
- Écrire la documentation docstring
- Écrire les tests que vous jugerez pertinents au format doctest

:::tip Aide
- Vous pouvez obtenir le caractère en position *n* d'une variable `message` en utilisant l'expression `message[n]`.
  L'expression pour récupérer le premier caractère de `message` serait `message[0]` car la numérotation se fait à partir de zéro.

  ```
  >>> message = 'Bonjour'
  >>> message[0]
  'B'
  ```

- Vous pouvez obtenir la conversion en majuscule d'une variable `message` en utilisant l'expression `message.upper()`

  ```
  >>> message = 'Bonjour'
  >>> message.upper()
  'BONJOUR'
  ```
:::




## 🛡️ Partie 2 - Protection des fonctions

### Exercice 3 - Multiplication

#### Objectif
Cet exercice a pour objectif d'écrire une fonction dont l'algorithme mis en œuvre ne fonctionne correctement que si certaines conditions sont respectées.

#### Consigne
Écrire la fonction `multiplication` ayant pour paramètres `x` et `y` deux entiers positifs ou nuls.
Cette fonction renvoie le produit de `x` par `y`.
Vous ne devrez utiliser que l'opérateur `+` et une boucle en respectant l'algorithme décrit dans la docstring ci-dessous :

```python
def multiplication(x, y):
    """
    Renvoie la produit de x par y.

    x -- Entier positif non nul
    y -- Entier positif non nul

    Algorithme :
       total ← 0
       Répéter y fois :
          total ← total + x
       renvoyer total
    """
```

- Enregistrer le code dans un fichier fichier `ex3_multiplication.py`
- Écrire la documentation docstring
- Écrire les tests que vous jugerez pertinents au format doctest

#### Cas particuliers

Tester les appels de fonction ci-dessous dans la console Python :

```text
multiplication(2,-2)
multiplication(2, 1.1)
multiplication(1.1, 2)
```

Vous constaterez que malgré l'absence d'erreur, le résultat renvoyé par chacun des appels est faux.
En effet, l'algorithme n'est conçu pour ne fonctionner qu'avec des entiers positifs ou nuls.
Il faudrait protéger notre fonction de tout usage non conforme et ainsi éviter l'introduction d'erreurs au sein de programmes plus vastes.

#### Protection de la fonction

Pour protéger la fonction `multiplication`, nous allons utiliser des **assertions**.
Une assertion est une condition qui doit être vraie pour poursuivre l'exécution d'un programme.
L'exécution de la fonction `multiplication` ne doit être possible que si les conditions suivantes sur les paramètres (aussi appelées préconditions) sont respectées :

- `x` est un entier
- `x` est supérieur ou égal à 0
- `y` est un entier
- `y` est supérieur ou égal à 0

En Python, il est possible de définir des assertions à l'aide de l'instruction `assert`.
Voici l'équivalent Python des assertions listées pour la fonction `multiplication` :

```python
assert isinstance(x, int) # vaut vrai si x est de type int
assert x >= 0             # vaut vrai si x est positif ou nul
assert isinstance(y, int) # vaut vrai si y est de type int
assert y >= 0             # vaut vrai si y est positif ou nul
```

#### Modification de la fonction

Ajouter les assertions à la fonction `multiplication`.
Celles-ci doivent être les premières instructions de la fonction et sont à placer juste après la docstring.
Une fois les assertions en place, tester de nouveau les appels de fonction problématiques.
Vous devez obtenir des erreurs `AssertionError`.

```python
def multiplication(x, y):
    """
    Docstring
    """
    assert isinstance(x, int)
    assert x >= 0
    assert isinstance(y, int)
    assert y >= 0

    # Code
```

### Exercice 4 - Puissance

Selon le même principe que l'exercice 3, écrire la fonction `puissance` ayant pour paramètres `x` et `y` deux entiers positifs ou nuls.
Cette fonction renvoie la valeur de `x` élevé à la puissance `y`. Utiliser uniquement l'opérateur `*` et une boucle.

- Enregistrer le code dans un fichier fichier `ex4_puissance.py`
- Écrire la documentation docstring (description de la fonction et des paramètres)
- Écrire l'algorithme dans la doctring
- Écrire les tests que vous jugerez pertinents au format doctest
- Écrire les assertions

<!--
### Exercice 5 - Factorielle

Selon le même principe que l'exercice 3 et 4, écrire la fonction `factoriel` ayant pour paramètre `n` un entier positif ou nul.
Cette fonction renvoie la factorielle de `n`.

- Enregistrer le code dans un fichier fichier `ex5_factorielle.py`
- Écrire la documentation docstring (description de la fonction et des paramètres)
- Écrire l'algorithme dans la doctring
- Écrire les tests que vous jugerez pertinents au format doctest
- Écrire les assertions
-->

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