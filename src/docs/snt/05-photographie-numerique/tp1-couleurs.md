---
title: TP1 - Manipulation d'une image
description: Manipulation d'une image
---

import FileExplorer from "@site/src/components/FileExplorer";
import useBaseUrl from '@docusaurus/useBaseUrl';

# Manipulation d'une image

## Introduction

#### Objectif
Manipuler les pixels et les couleurs d'une image à l'aide du langage de programmation Python.

:::danger Travail à rendre
Un compte rendu est à transmettre en fin de séance :
- Créer un **document texte** en utilisant un logiciel de traitement de texte (LibreOffice Writer, Word, ...)
- Y intégrer les informations explicitement demandées dans chaque exercice
- L'envoyer via **Pronote** en exportant au préalable le compte rendu au **format PDF**
:::

#### Préparation

Afin de ne pas mélanger les productions entre les travaux pratiques, mettre à jour les dossiers SNT selon l'ordinateur utilisé :

<details>
    <summary>💻 Ordinateur portable</summary>

1. Lancer <FileExplorer/>
2. Se rendre dans le dossier **Mes documents**
3. Créer le dossier **SNT** s'il n'existe pas déjà (clic droit, *Nouveau > Dossier*)
4. Dans le dossier **SNT**, créer le dossier **Photographie**
5. Dans le dossier **Photographie**, créer le dossier **TP1 - Manipulation d'une image**

</details>

<details>
    <summary>🖥 Ordinateur fixe des salles informatiques</summary>

1. Depuis le bureau, cliquer sur l'icône intitulée **Zone personnelle**
2. Créer le dossier **SNT** s'il n'existe pas déjà (clic droit, *Nouveau > Dossier*)
3. Dans le dossier **SNT**, créer le dossier **Photographie**
4. Dans le dossier **Photographies**, créer le dossier **TP1 - Manipulation d'une image**

</details>




## Exercice 1 - Définition d'une image

#### Consigne de préparation

1. Téléchargez le fichier <a href={"pathname://" + useBaseUrl('/img/smiley.png')} download>smiley.png</a> *(et ne pas l'ouvrir)*
2. Lancez [Basthon](https://console.basthon.fr/?script=eJw9jU0KgzAUhPeB3OERNwpV6AG67EJwUXqDEJ_6wPzwTMD2Rp7DizVWcDfDfDNTFAXUdQ3PFdmQQbgfVoqBvYVX2wHZ4DlCa_WIUkhRQIcmJkboEwxkJkLO0D8lO8LjRBsf0JVqsTTjpwluVNXZfu-bSWHfWEfyDjCCHo6Z3IEeYdbQ79tAjo5YilnziIlvMOkUs8j7-aVZ6Jv_ApOL5YWoVV1c9QPsmkd1)
   &nbsp;*(👈 cliquez sur le lien afin de disposer automatiquement du code Python nécessaire à cet exercice)*
3. Dans Basthon, cliquez sur le bouton représentant un dossier et qui sert à importer un fichier
4. Importez le fichier **smiley.png** téléchargé précédemment<br />
   *(le fichier doit s'appeler "smiley" ou "smiley.png" et non "smiley (1)" ou autre)*

<details>
    <summary>Code Python</summary>

À n'utiliser que si vous souhaitez utiliser un autre interpréteur Python que Basthon.

```python
### --- Exercice 1 ---
from PIL import Image

# Lecture du fichier image
img = Image.open("smiley.png")

# Récupération et affichage de la définition
largeur, hauteur = img.size
print(largeur, "x", hauteur)
```

</details>


#### Consigne de travail

Une image numérique est composée de pixels.
Le pixel est un point coloré qui constitue le plus petit élément d'une image. Une des caractéristiques d'une image numérique est sa **définition**.
La définition d'une image correspond à sa dimension exprimée en pixels sous la forme *largeur* x *hauteur*.

1. Cliquez sur le bouton **Exécuter**
2. Lisez les dimensions de l'image
3. Reportez dans votre compte rendu les informations suivantes en ne faisant qu'une seule phrase :
    - Largeur en pixels
    - Hauteur en pixels
    - Nombre total de pixels que contient l'image *(à calculer)*




## Exercice 2 - Manipulation de pixels

#### Consigne de préparation

1. Téléchargez le fichier <a href={"pathname://" + useBaseUrl('/img/smiley.png')} download>smiley.png</a> *(c'est normalement déjà fait)*
2. Lancez **de nouveau** [Basthon](https://console.basthon.fr/?script=eJxtkE1OwzAQhfeWfIdRs4gtJVaIYMGiC0RZVEKCGyCTTJIR_glOQtMjcQ4uRkyKhGg3M7Lf8zfPkyQJ5HkODzOGiiqEMh45a4K38Lx_BLK9DyPsrW4xW9su6ANnnCXwNH1gGKeAUCOYlKLKGdkWtqtV-R6d2AyWDB5V79qNXF_eex9q79zXJw4g5uwoI6Lq9PuE4JEMZ7G-tHqqOlxw4qooMygLeRLq4GmM9zdFBte3J-wOh4Ec1BP0NKM5Y9ZL9N9s8RsqFrEElqumek9uFH9GZ9CQMdv01ejqLb1g-wly5oph7pqGFkL4vxw1dP4g5DfCAXXI)
   &nbsp;*(👈 cliquez sur le lien afin de disposer automatiquement du code Python nécessaire à cet exercice)*
3. Dans Basthon, cliquez sur le bouton représentant un dossier et qui sert à importer un fichier
4. Importez le fichier **smiley.png** téléchargé précédemment
5. Cliquez sur le bouton **Exécuter**
6. Cliquez sur le bouton représentant une image

<div style={{textAlign: 'Center', marginBottom: '2em'}}>
    <img style={{maxWidth: '75%'}} src={require('./assets/basthon_exercice2.png').default} alt="Exercice 2"/>
</div>

<details>
    <summary>Code Python</summary>

À n'utiliser que si vous souhaitez utiliser un autre interpréteur Python que Basthon.

```python
### --- Exercice 2 ---
from PIL import Image, ImageDraw

# Ouverture de l'image
img = Image.open("smiley.png")

# Coordonnées (x,y) de chaque oeil
oeil_gauche = (102, 20)
oeil_droit = (50, 49)

# Dessin du pixel de chaque oeil
draw = ImageDraw.Draw(img)
draw.point(oeil_gauche, fill='black')
draw.point(oeil_droit, fill='black')

# Afficher de l'image
img.show()
```

</details>

#### Consigne de travail
L'objectif de ce travail est de comprendre le système de coordonnées des pixels, c'est-à-dire où se trouve l'origine et comment sont orientés les axes X et Y:

1. Repérez deux pixels noirs isolés sur l'image *(ce sont les pixels représentant les yeux du smiley et ceux-ci sont mal placés)*
2. Modifiez les coordonnées des pixels afin de les placer correctement sur le smiley pour lui rendre ses yeux *(faire plusieurs petits essais pour comprendre comment fonctionnent les coordonnées)*
3. Complétez votre compte rendu en ajoutant les informations suivantes :
    - Les nouvelles coordonnées des yeux
    - La position de l'origine sur l'image, c'est-à-dire où se trouve le point de coordonnées `(0,0)` *(au centre de l'image ? en bas et au milieu ? en bas à gauche ? indiquez le bon endroit)*




## Exercice 3 - La couleur

#### Consigne de préparation

1. Lancez de nouveau [Basthon](https://console.basthon.fr/?script=eJxNjksLgzAQhO-C_2HAgwoqYvHYQytSBA_FU6-hrg_w0Sax_v1u1EIhJMzk29lxEIYh8kdeZUWW42SkbTVyHnEvSvTja5YaxShasi3bclCSYuo584cSk2ZVu8tE7CwDLXJDBD7CCNTsd-K90N-AIUjpzZG9ItCkJSEGaSRpaltHEs7w4gDm-PvqS9P0HNeSyR3cfi-1PQxvHaOJVs-tblc3gJfEPMyXH_za-QceqW5ePf8Lzl9KIw)
   &nbsp;*(👈 cliquez sur le lien afin de disposer automatiquement du code Python nécessaire à cet exercice)*
2. Cliquez sur le bouton **Exécuter**
3. Cliquez sur le bouton représentant une image

<details>
    <summary>Code Python</summary>

À n'utiliser que si vous souhaitez utiliser un autre interpréteur Python que Basthon.

```python
### --- Exercice 3 ---
from PIL import Image

# Les 3 composantes d'une couleur
# La valeur de chaque composante
# est comprise entre 0 et 255
couleur = (0, 0, 0)

# Affichage de l'image
image = Image.new('RGB', (200, 200), couleur)
image.show()
```

</details>


#### Consigne de travail

En informatique, les couleurs peuvent être représentées en faisant varier l'intensité de trois composantes.
Chaque intensité est codée sous forme d'une valeur entière comprise entre 0 et 255.

1. Testez `(255,0, 0)`, `(0, 255, 0)`, `(0, 0, 255)` et reportez les couleurs trouvées dans votre compte rendu
2. Complétez votre compte rendu en effectuant les tâches suivantes :
    - Trouvez et reportez le code couleur du blanc, du jaune et du magenta *(rose/violet vif)*
    - Recherchez sur le web le nombre de couleurs visibles par l'œil humain
    - Calculez le nombre total de couleurs possibles sachant que chacune des 3 intensités peut prendre 256 valeurs. Notez le calcul et la valeur trouvée dans le compte rendu
    - Comparez sur le nombre de couleurs qu'il est possible de générer avec le nombre de couleurs visibles par l'œil humain et conclure




## Exercice 4 - Manipulation d'une image

#### Consigne de préparation

1. Téléchargez le fichier <a href={"pathname://" + useBaseUrl('/img/fraise.jpg')} download>fraise.jpg</a>
2. Lancez de nouveau [Basthon](https://console.basthon.fr/?script=eJxtkU1qwzAQhfcG32GIF7VB9qqrQhaFdhFoaegNVHvsTJAlMbISpzfKOXKxyn-YptVmEG_eN0-aJEkgz3N47ZFLKhEeh2sc1Wxa2O_egFpruINdKxsUU3lheY6jOErgw5-QO88IFYJ6oEGNI2ob2E6thbGo003NkhwWR9tsssm5l1waz24wdsY7UOjAUo_K_WKVRhmt0QlQ1IQawAFfOPoOYm0YeiANLHWD6dKbPcURhDPIl1WeAIs4nAQ-b9fS29uVZUdGj5MlhGAKPUPlp0SrwRpHY-MW0l7AJVslFnAS8DXna7AbreniGJ-9zn2XmqxX_0xdu5YYYdYMv4eYimoqZ8ifsEMO6-9yiAU77-G5DoRD-Or7DRbuYM5p9gP2jKNd)
&nbsp;*(👈 cliquez sur le lien afin de disposer automatiquement du code Python nécessaire à cet exercice)*
3. Dans Basthon, cliquez sur le bouton représentant un dossier et qui sert à importer un fichier
4. Importez le fichier **fraise.jpg** téléchargé précédemment
5. Cliquez sur le bouton **Exécuter**
6. Cliquez sur le bouton représentant une image

<details>
    <summary>Code Python</summary>

À n'utiliser que si vous souhaitez utiliser un autre interpréteur Python que Basthon.

```python
### --- Exercice 4 ---
from PIL import Image, ImageDraw

# Ouverture de l'image
img = Image.open("fraise.jpg")

# Parcours de tous les pixels de l'image
colonnes, lignes = img.size
    for x in range(colonnes):
        for y in range(lignes):
            # Récupération de la couleur du pixel
            position = (x, y)
            r, v, b = img.getpixel(position)

            # Manipulation de la couleur
            couleur = (r, v, b)

            # Modification du pixel
            img.putpixel(position, couleur)

# Affichage de l'image
img.show()
```

</details>


#### Consigne de travail

L'ensemble des modifications demandées sont à effectuer uniquement au niveau de la ligne indiquée ci-dessous.
**Attention, veillez à conserver l'indentation des lignes** *(c'est-à-dire le même décalage vers la droite)*.

```python
# Manipulation de la couleur
couleur = (r, v, b)
```

Les points de 1 à 7 sont simplement à expérimenter. Les résultats des points 8 et 9 sont à reporter dans le compte rendu.

1. Modifiez les couleurs telles que : `couleur = (b, r, v)`
2. Modifiez les couleurs telles que : `couleur = (v, v, b)`
3. Supprimez la composante rouge : `couleur = (0, v, b)`
4. Supprimez la composante verte : `couleur = (r, 0, b)`
5. Supprimez la composante bleue : `couleur = (r, v, 0)`
6. Créez la version négative : `couleur = (255-r, 255-v, 255-b)`
7. Créez une image en noir et blanc en affectant aux 3 composantes le calcul de l'intensité moyenne : <br />`couleur = ((r+v+b)//3, (r+v+b)//3, (r+v+b)//3) `
8. Inventez votre propre "filtre" de couleurs et copier/coller votre "formule" et l'image générée dans votre compte rendu
9. Testez un traitement sur l'image de votre choix (au format jpg ou png) et copiez/collez l'image obtenue dans votre comte rendu

:::danger Envoi du travail
- Exportez votre compte rendu au **format PDF**
- Connectez-vous à **Pronote**
- L'envoyer en cliquant sur **Déposer ma copie**
:::