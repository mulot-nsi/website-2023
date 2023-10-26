---
title: Le langage CSS
description: Découverte du langage CSS
---

# Le langage CSS

## Introduction

L’activité « [:material-link: TP1 - Langage HTML](tp1-langage-html.md) » a consisté à utiliser le langage HTML pour définir le **contenu
et la structure** d'une page web.

Ces travaux pratiques ont pour objectif de vous faire découvrir la **mise en forme** d'une page web.
Pour cela, vous apprendrez à utiliser le langage CSS *(Cascading Style Sheets)* aussi appelé *feuilles de style* en français.

!!! target "Objectifs"

    - Comprendre le rôle du langage CSS
    - Savoir faire la distinction entre le langage HTML et le langage CSS
    - Comprendre la structure du langage CSS
    - Savoir ce qu'est un selecteur de type
    - Savoir ce qu'est un selecteur de classe
    - Savoir ce qu'est une propriété CSS

!!! danger "Travail à rendre"

    Les travaux réalisés dans le cadre de ce TP est à rendre en fin de séance selon les modalités suivantes.

## Préparation

### Espace de travail

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et
travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'**explorateur de fichiers**
        2. Accédez au dossier `Documents`
        3. Dans le dossier `Documents`, s'il n'y a pas de dossier nommé `SNT`, créez-le
        4. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le
        5. Dans le dossier `web`, créez le dossier `langage_css`

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans la **zone personnelle**, s'il n'y a pas de dossier nommé `SNT`, créez-le
        3. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le
        4. Dans le dossier `web`, créez le dossier `langage_css`

### Téléchargement des fichiers

Pour effectuer ce TP, il est nécessaire de télécharger certains fichiers :

!!! note "Récupération des fichiers"

    1. Téléchargez le fichier ZIP contenant les fichiers nécessaires à ce TP : [:material-download: télécharger](assets/SNT02_TP2.zip){:download="SNT02_TP2.zip"}
    2. Ouvrez le fichier ZIP<br>*(le navigateur l'ouvre automatiquement ou cliquez sur le fichier téléchargé)*
    3. Sélectionnez tous les fichiers et dossiers - ++ctrl+a++
    4. Copiez tous les fichiers et dossiers - ++ctrl+c++
    5. Collez les fichiers dans le dossier `SNT\Web\langage_css` - ++ctrl+v++

## Application des styles

### Association d'un fichier CSS

Le fichier `index.html` correspond à la page web à mettre en forme.
L'ensemble des règles de mise en forme CSS sont écrites dans le fichier `style.css`.
Ce fichier est une **feuille de style**. Celle-ci est dite «&nbsp;externe&nbsp;» car les règles de mise en forme sont définies à l'extérieur de la page web.

!!! info "Culture numérique"

    Pour définir la mise en forme des éléments d'une page web, il existe plusieurs méthodes :

    - Utiliser l'attribut `style` des balises HTML ([:material-link: référence](https://developer.mozilla.org/fr/docs/Web/HTML/Global_attributes/style){:target="_blank"})
    - Utiliser la balise HTML `#!html <style></style>` sur la page à mettre en forme (*feuille de style interne*) ([:material-link: référence](https://developer.mozilla.org/fr/docs/Web/HTML/Element/style){:target="_blank"})
    - Utiliser un lien vers une ressource externe à la page à mettre en forme (*feuille de style externe*) ([:material-link: référence](https://developer.mozilla.org/fr/docs/Web/HTML/Element/link){:target="_blank"})

Dans le cadre de ces travaux pratiques, nous n'utiliserons que la méthode de la **feuille de style externe**.
Vous allez maintenant procéder à l'association d'une feuille de style à une page web :

!!! note "Visualisation de la page web à styliser"

    1. Lancez **l'explorateur de fichiers**
    2. Placez-vous dans le dossier `SNT\web\langage_css`
    3. Double-cliquez sur le fichier `index.html` afin de l'ouvrir dans un navigateur web
    4. Gardez le navigateur ouvert

!!! note "Association d'une feuille de style"

    4. Lancez l'application **Bloc-notes**
    5. Ouvrez le fichier `index.html` - ++ctrl+o++
    6. Cherchez les balises `#!html <head> ... </head>`
    7. Ajoutez le code HTML ci-dessous entre les balises `#!html <head> ... </head>` : 
       ``` html
       <link href="style.css" rel="stylesheet">
       ```
      Le code HTML de l'en-tête doit maintenant ressembler à ceci :
       ``` html hl_lines="4"
       <head>
           <meta charset="utf-8">
           <title>PMDb - Personal Movie Database</title>
           <link href="style.css" rel="stylesheet">
       </head>
       ```
    9. Enregistrez vos modifications - ++ctrl+s++
    10. Retournez dans le navigateur web
    11. Rafraichissez la page `index.html` - ++f5++ ou ++ctrl+r++<br> 
        *(des changements doivent être observables)*

!!! tip "Cours - La feuille de style"

    La page web `index.html` est maintenant reliée au fichier `style.css`.
    Le fichier `style.css` est appelé **feuille de style**.
    Celle-ci contient des règles de mise en forme écrites en **langage CSS**.

### Sélecteur de type

Nous allons étudier plus en détail la feuille de style `style.css` afin comprendre les principes et la syntaxe du langage CSS.

!!! note "Découverte du langage CSS"

    1. Retournez à l'application **Bloc-notes**
    2. Ouvrez le fichier `style.css` - ++ctrl+o++
    3. Le code présent au début de fichier doit être similaire à celui-ci :
    ``` css
    body {
        margin: 0;
        background-color: purple;
    }
    
    header {
        background-color: #121212;
        color: white;
        padding: 20px;
    }
    ```

!!! tip "Cours - Le langage CSS"

    Une feuille de styles contient un ensemble de **déclarations**. Chaque déclaration est constituée de deux parties :

    - Un **sélecteur**, qui permet de sélectionner la **balise** de l'élément à mettre en forme
    - Un **ensemble de règles** entre accolades `{ }`. Les règles permettent d'ajuster les **valeurs** des **propriétés** de mise en forme

    <figure markdown>
        ![selecteur_type](images/css_selecteur_type.png)
        <figcaption>Exemple de déclaration CSS ciblant la balise </em><code>body</code></figcaption>
    </figure>

    Dans le cas ci-dessus, il est question du **sélecteur** `body`.
    Il s'agit d'un **sélecteur de type**, c'est-à-dire qu'il permet de cibler la balise de type `<body>` qui se verra alors appliquer l'ensemble des règles définies (marge à 0 et couleur de fond à violet).

!!! note "Création d'un style"

    Nous allons déclarer un style CSS dont le sélecteur va cibler le balise `<h1>` correspondant au titre principale de notre document (*« Intouchable »*).

    1. Retourner dans l'application Notepad++
    2. Revenir au fichier <FichierCSS /> (si besoin, Menu *Fichier > Ouvrir* ou `CTRL+O`)
    3. **Ajouter** la déclaration CSS suivante (*vous pouvez l'ajouter n'importe où, mais si vous doutez, ajoutez-la en fin de fichier*) :

    ```css
    h1 {
        color: red;
    }
    ```

    4. **Enregistrer** le fichier `CTRL+S`
    5. Retourner dans le navigateur web
    6. Rafraichir la page (`F5` ou `CTRL+R`), un changement doit être observable au niveau du titre principal

### Sélecteur de classe

Avec le sélecteur de type, il n'est pas possible de choisir précisément l'élément sur lequel nous souhaitons appliquer
un style.
Pour résoudre ce problème, il existe un autre genre de sélecteur.

!!! note "Mise en pratique"

    1. Retourner dans l'application Notepad++
    2. Revenir au fichier <FichierCSS />
    3. **Rechercher** la déclaration CSS ayant pour sélecteur **.logo** :

    ```css
    .logo {
        background-color: #f5c518;
    
        ...
        justify-content: center
    ;
    }
    ```

    Le sélecteur `.logo` ne correspond à aucune balise HTML. Son nom est **précédé d'un point**.
    Ceci signifie qu'il est question d'un **sélecteur de classe**.
    Celui-ci cible les balises dont l'attribut `class` a pour valeur `logo`.

    <figure markdown>
        ![selecteur_type](images/css_selecteur_classe.png)
        <figcaption>Exemple de déclaration CSS ciblant les balises disposant de la classe </em><code>special</code></figcaption>
    </figure>

!!! note "Application du sélecteur"

    1. Retourner dans l'application Notepad++
    2. Revenir au fichier <FichierHTML />
    3. **Chercher** à proximité de la balise **ouvrante** `<body>` la ligne :
    ```html
    <a href="https://www.imdb.com/video/vi59285529">PMDb</a>
    ```
    4. **Ajouter** l'attribut `class="logo"` à cette balise `<a>`
    5. Votre code HTML doit maintenant ressembler à ceci :
    ```html
    <a class="logo" href="https://www.imdb.com/video/vi59285529">PMDb</a>
    ```
    6. Enregistrer les modifications `CTRL+S`
    7. Retourner dans le navigateur web
    8. Rafraichir la page (`F5` ou `CTRL+R`), un changement doit être observable tout en haut de la page

!!! info "Bilan"

    Pour qu'un style s'applique à une balise, il faut pouvoir la cibler finement.
    Pour cela, nous avons étudié deux sélecteurs :

    - les **sélecteurs de type** qui ciblent un type de balise précis
    - les **sélecteurs de classe** qui ciblent les balises dont l'attribut `class` a une valeur précise

## Propriétés CSS

### Gestion des couleurs

Les propriétés CSS `background-color` et `color` permettent d'ajuster respectivement la **couleur de fond** d'un élément
et la **couleur du texte** contenu par celui-ci.
Pour choisir une couleur, il est possible d'utiliser un **nom** (par exemple `red`) ou un **code hexadécimal** (par
exemple `#ff0000`).

Une liste de noms de couleurs est disponible sur [Wikipédia](https://fr.wikipedia.org/wiki/Couleur_du_Web).
Il est aussi possible d'obtenir le code hexadécimal de n'importe quelle couleur en utilisant
un [outil de gestion des couleurs](https://mdn.github.io/css-examples/tools/color-picker/).

!!! info "Propriétés CSS"

    | Propriété          | Description                         | Référence                                                                 |
    |--------------------|-------------------------------------|---------------------------------------------------------------------------|
    | `background-color` | Couleur d'arrière-plan d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/background-color) |
    | `color`            | Couleur du texte d'un élément       | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/color)            |

??? example "Exemple"

    Voici **un exemple** de déclaration CSS permettant de modifier la **couleur de fond** et la **couleur du texte** du
    contenu de la balise `body` (donc de tout le document HTML).
    Le texte entre `/* */` est un commentaire. Les commentaires permettent d'ajouter des précisions sans conséquence sur la

![css_selecteur_type.png](images%2Fcss_selecteur_type.png)  mise en forme CSS.

    ```css
    body {
        background-color: yellow; /* couleur de fond jaune  */
        color: #ffba00; /* couleur du texte jaune */
    }
    ```

!!! note "Mise en pratique"

    1. Retourner dans l'application Notepad++
    2. Revenir au fichier <FichierCSS />
    3. **Modifier** la déclaration CSS ciblant la balise `body` de façon à modifier uniquement la **couleur d'arrière-plan**
      de votre document HTML (*inspirez-vous de l'exemple d'utilisation*)
    4. **Ajouter** une nouvelle déclaration CSS ciblant la balise `h2` de façon à modifier la **couleur du texte** de chaque
      sous-titre (*inspirez-vous de l'exemple d'utilisation et de ce qui a été fait pour* `h1`)

### Gestion du texte

Les propriétés CSS `font-size` et `text-decoration` permettent respectivement d'ajuster la taille du texte et la
décoration du texte (soulignement).

!!! info "Propriétés CSS"

    | Propriété         | Description                  | Référence                                                                |
    |-------------------|------------------------------|--------------------------------------------------------------------------|
    | `font-size`       | Taille du texte d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/font-size)       |
    | `text-decoration` | Soulignement d'un élément    | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/text-decoration) |

??? example "Exemple"

    Voici **un exemple** de déclaration permettant de grossir et souligner le texte de toute balise de classe `super` (
    c'est-à-dire ayant l'attribut `class="super"`) :
    
    ```css
    .super {
        font-size: 150px; /* taille en pixels */
        text-decoration: underline; /* soulignement */
    }
    ```

!!! note "Mise en pratique"

    1. Retourner dans l'application Notepad++
    2. Revenir au fichier <FichierCSS />
    3. **Modifier** la déclaration CSS ciblant la balise `h1` de façon à grossir la **taille du texte** du titre principal
    4. **Modifier** la déclaration CSS ciblant la balise `h2` de façon à **souligner** les sous-titres

### Gestion des dimensions

Les propriétés CSS `width` et `height` permettent d'ajuster respectivement la largeur et la hauteur d'un élément.

!!! info "Propriétés CSS"

    | Propriété | Description          | Référence                                                       |
    |-----------|----------------------|-----------------------------------------------------------------|
    | `width`   | Largeur d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/width)  |
    | `height`  | Hauteur d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/height) |

??? example "Exemple"

    Voici ci-dessous un exemple de déclaration CSS permettant de fixer la largeur de tout élément de classe `icone` à 10
    pixels de large:
    
    ```css
    .icone {
        width: 10px; /* largeur de l'élément en pixels */
    }
    ```

#### <PracticeTitle />

1. Retourner dans l'application Notepad++
2. Revenir au fichier <FichierCSS />
3. **Ajouter** une déclaration CSS permettant de fixer la largeur (`width`) de tout élément de classe `affiche` à 150
   pixels de large.

<details>
    <summary>💡 Solution</summary>

Pour cela vous devez utiliser le sélecteur de classe `.affiche` et fixer la propriété `width` à `150px`.

```css
.affiche {
    width: 150px;
}
```

</details>

4. Enregistrer le fichier `CTRL+S`
5. Revenir au fichier <FichierHTML />
6. **Rechercher** la seule balise `<img>` présente dans le document et qui correspond à l'élément **image** de l'affiche
   du film
7. **Modifier** la balise pour lui ajouter la classe `affiche`

!!! success "Solution"

    Après modification, le code HTML de la balise `img` doit être similaire à ceci :

    ```html
    <img class="affiche" src="images/intouchable.jpg" alt="Affiche du film Intouchable"/>
    ```

8. **Enregistrer** le fichier `CTRL+S`
9. Retourner dans le navigateur web
10. Rafraichir la page, un changement doit être observable au niveau de l'affiche du film

### Expérimentation

Vous avez terminé et il reste plus de 5 minutes avant la fin de la séance ? Bravo !
Il vous reste encore beaucoup à découvrir et d'autres propriétés peuvent se révéler intéressantes :

| Propriété          | Description                       | Référence                                                                 |
|--------------------|-----------------------------------|---------------------------------------------------------------------------|
| `text-align`       | Alignement du texte               | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/text-align)       |
| `border`           | Bordure autour d'un élément       | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/border)           |
| `margin-bottom`    | Marge inférieure d'un élément     | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/margin-bottom)    |
| `background-image` | Image d'arrière-plan d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/background-image) |

#### <PracticeTitle />

Tester chacune de ces propriétés. Ne pas hésiter à s'inspirer des exemples interactifs présentés sur les pages de
référence.

## Envoi du travail

### Création du fichier ZIP

Pour faciliter le partage de plusieurs fichiers et dossiers, il est de regrouper l'ensemble dans un seul fichier au
format ZIP.
Lire les instructions selon l'ordinateur utilisés :

<details>
    <summary>💻 Ordinateur portable (Windows 11)</summary>

1. Lancer <FileExplorer />
2. Se rendre dans le dossier `SNT\Web`
3. Cliquer une seule fois avec le bouton **gauche** sur le dossier `langage_css` pour le sélectionner
4. Cliquer avec le bouton **droit** sur le dossier `langage_css`
5. Choisir l'option **Compresser dans le fichier ZIP**
6. Nommer le fichier *nom*_*prenom*_tp_css.zip

</details>

<details>
    <summary>🖥 Ordinateur fixe des salles informatiques (Windows 10)</summary>

1. Lancer <FileExplorer />
2. Se rendre dans le dossier `SNT\Web`
3. Cliquer une seule fois avec le bouton **gauche** sur le dossier `langage_css` pour le sélectionner
4. Cliquer avec le bouton **droit** sur le dossier `langage_css`
5. Choisir l'option **Envoyer vers** puis **Dossier compressé**
6. Nommer le fichier *nom*_*prenom*_tp_css.zip

</details>

### Transmission du fichier ZIP

1. Se connecter à l'ENT
2. Accéder à l'application **Exercices**
3. Cliquer sur l'exercice **[2TP2] Le langage CSS - Rendu**
4. Choisir le fichier ZIP créé précédemment pour envoi
5. Valider l'envoi du devoir