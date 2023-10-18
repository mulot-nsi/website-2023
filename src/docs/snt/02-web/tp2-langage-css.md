---
sidebar_position: 2
sidebar_label: TP2 - Le Langage CSS
slug: /snt/web/tp2-langage-css
description: Étude du langage CSS
---

# Le langage CSS

import FileExplorer from '@site/src/components/FileExplorer';

export const FichierHTML = () => <code>index.html</code>

export const FichierCSS = () => <code>style.css</code>

export const PracticeTitle = () => <>🛠 Mise en pratique</>

## 👨‍🏫 Introduction

### Objectif

Lors du [TP précédent](tp1-langage-html.md), nous avons utilisé le langage HTML (*HyperText Markup Language*) afin de définir le **contenu** et la **structure** d'un document web.
Cette fois-ci, l'objectif est de **mettre en forme** un document web déjà existant. Pour cela, nous allons utiliser le langage CSS (pour *Cascading Style Sheets* ou *feuilles de style en cascade* en français).

:::danger Travail à rendre
Le travail effectué dans le cadre de ce TP est à rendre en fin de séance selon les modalités suivantes :
- Envoyer **obligatoirement** vos fichiers sous forme d'une archive au format ZIP
- Effectuer le rendu **uniquement** depuis l'application **Exercices** de l'ENT, via l'exercice intitulé **[2TP2] Le langage CSS - Rendu**
:::

### Préparation

Afin de ne pas mélanger les productions entre les travaux pratiques, mettre à jour les dossiers SNT selon l'ordinateur utilisé :

<details>
    <summary>💻 Ordinateur portable</summary>

1. Lancer <FileExplorer />
2. Se rendre dans le dossier **Mes documents**
3. Créer le dossier **SNT** s'il n'existe pas déjà (clic droit, *Nouveau > Dossier*)
4. Dans le dossier **SNT**, créer le dossier **Web** s'il n'existe pas déjà
5. Dans le dossier **Web**, créer le dossier **langage_css**

</details>

<details>
    <summary>🖥 Ordinateur fixe des salles informatiques</summary>

1. Depuis le bureau, cliquer sur l'icône intitulée **Zone personnelle**
2. Créer le dossier **SNT** s'il n'existe pas déjà (clic droit, *Nouveau > Dossier*)
3. Dans le dossier **SNT**, créer le dossier **Web** s'il n'existe pas déjà
4. Dans le dossier **Web**, créer le dossier **langage_css**

</details>

### Téléchargement des fichiers
Pour effectuer ce TP, il est nécessaire de télécharger certains fichiers :

1. Récupérer l'archive zip contenant les fichiers du TP : [📦 télécharger](assets/SNT02_TP2.zip){:download}
2. Ouvrir le fichier ZIP (le navigateur l'ouvre automatiquement ou au clic sur le fichier téléchargé)
3. Sélectionner tous les fichiers et dossiers `CTRL+A`
4. Copier `CTRL+C`
5. Coller `CTRL+V` les fichiers dans le dossier `SNT\Web\langage_css`

## ✍️ Partie 1 - Application des styles

### 1.1. Feuille de style externe

Le document web pour lequel nous allons définir le style réside dans le fichier <FichierHTML />.
L'ensemble du code CSS sera écrit dans un fichier déjà présent et nommé <FichierCSS />.
Ce fichier est une feuille de style dite externe car le code CSS se trouve à l'extérieur du fichier <FichierHTML />.

:::tip en savoir plus
Pour définir nos styles CSS, nous n'utiliserons qu'une seule des trois méthodes possibles :
- Utiliser l'attribut `style` des balises HTML ([référence](https://developer.mozilla.org/fr/docs/Web/HTML/Global_attributes/style))
- Utiliser la balise `<style></style>` (*feuille de style interne*) ([référence](https://developer.mozilla.org/fr/docs/Web/HTML/Element/style))
- Utiliser un lien vers une ressource externe (*feuille de style externe*) ([référence](https://developer.mozilla.org/fr/docs/Web/HTML/Element/link))
:::

#### <PracticeTitle />

1. Lancer <FileExplorer />
2. Se rendre dans le répertoire `SNT\Web\langage_css`
3. Double-cliquer sur le fichier <FichierHTML /> pour qu'il s'ouvre dans un navigateur web
4. Lancer l'application Notepad++
5. Ouvrir le fichier <FichierHTML /> depuis Notepad++ (Menu *Fichier > Ouvrir* ou `CTRL+O`)
7. **Chercher** les balises `<head> ... </head>`
8. **Ajouter** la balise `<link href="style.css" rel="stylesheet">` entre les balises `<head></head>`
9. Votre code HTML doit maintenant ressembler à ceci :
```html
<head>
    <meta charset="utf-8">
    <title>PMDb - Personal Movie Database</title>
    <link href="style.css" rel="stylesheet">
</head>
```
10. **Enregistrer** le fichier `CTRL+S`
11. **Retourner** dans le navigateur web
12. **Rafraichir** la page (`F5` ou `CTRL+R`). Des changements doivent être observables.

:::info Bilan
Le document web <FichierHTML /> est maintenant relié au fichier <FichierCSS />.
Le fichier  <FichierCSS /> est appelé **feuille de style**.
Il contient des instructions en **langage CSS** ayant pour finalité la **mise en forme** le document web.
:::

### 1.2. Sélecteur de type

Nous allons étudier plus en détail la feuille de style pour identifier le code CSS responsable des changements observés.

#### <PracticeTitle /> (1/2)

1. Retourner dans l'application Notepad++
2. Ouvrir le fichier <FichierCSS />
3. Vous devez voir en début de fichier du code similaire à celui-ci :

```css
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

#### 💡 Explications

Une feuille de styles contient un ensemble de **déclarations**.
Chaque déclaration est constituée de deux parties :

- Un **sélecteur**, qui permet de sélectionner **la balise** de l'élément à mettre en forme
- Un **ensemble de règles** entre des accolades `{ }`. Les règles permettent d'ajuster des **propriétés** de mise en forme

<div style={{textAlign:'Center', marginBottom:'2em'}}>
    <img
        src={require('./assets/css_selecteur_type.png').default}
        style={{border:'1px solid black', padding:'20px'}}
        alt="Syntaxe CSS"
    />
    <br />
    <em>Exemple de déclaration CSS ciblant la balise </em><code>body</code>
</div>

Dans le cas ci-dessus, il est question du **sélecteur** `body`.
Il s'agit d'un **sélecteur de type**, c'est-à-dire qu'il permet de cibler la balise de type `<body>` qui se verra alors appliquer l'ensemble des règles définies (marge à 0 et couleur de fond à violet).

#### <PracticeTitle /> (2/2)

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

### 1.3. Sélecteur de classe

Avec le sélecteur de type, il n'est pas possible de choisir précisément l'élément sur lequel nous souhaitons appliquer un style.
Pour résoudre ce problème, il existe un autre genre de sélecteur.

#### <PracticeTitle /> (1/2)

1. Retourner dans l'application Notepad++
2. Revenir au fichier <FichierCSS />
3. **Rechercher** la déclaration CSS ayant pour sélecteur **.logo** :

```css
.logo {
    background-color: #f5c518;
    ...
    justify-content: center;
}
```

Le sélecteur `.logo` ne correspond à aucune balise HTML. Son nom est **précédé d'un point**.
Ceci signifie qu'il est question d'un **sélecteur de classe**.
Celui-ci cible les balises dont l'attribut `class` a pour valeur `logo`.

<div style={{textAlign:'Center', marginBottom:'2em'}}>
    <img
        src={require('./assets/css_selecteur_classe.png').default}
        style={{border:'1px solid black', padding:'20px'}}
        alt="Syntaxe CSS"
    />
    <br />
    <em>Exemple de déclaration CSS ciblant les balises disposant de la classe </em><code>special</code>
</div>


#### <PracticeTitle /> (2/2)

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

:::info Bilan
Pour qu'un style s'applique à une balise, il faut pouvoir la cibler finement.
Pour cela, nous avons étudié deux sélecteurs :

- les **sélecteurs de type** qui ciblent un type de balise précis
- les **sélecteurs de classe** qui ciblent les balises dont l'attribut `class` a une valeur précise
:::

## 🌈 Partie 2 - Propriétés CSS

### 2.1. Gestion des couleurs

#### 💡 Principe

Les propriétés CSS `background-color` et `color` permettent d'ajuster respectivement la **couleur de fond** d'un élément et la **couleur du texte** contenu par celui-ci.
Pour choisir une couleur, il est possible d'utiliser un **nom** (par exemple `red`) ou un **code hexadécimal** (par exemple `#ff0000`).

Une liste de noms de couleurs est disponible sur [Wikipédia](https://fr.wikipedia.org/wiki/Couleur_du_Web).
Il est aussi possible d'obtenir le code hexadécimal de n'importe quelle couleur en utilisant un [outil de gestion des couleurs](https://mdn.github.io/css-examples/tools/color-picker/).

#### 📖 Propriétés CSS
| Propriété          | Description                         | Référence                                                                 |
|--------------------|-------------------------------------|---------------------------------------------------------------------------|
| `background-color` | Couleur d'arrière-plan d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/background-color) |
| `color`            | Couleur du texte d'un élément       | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/color)            |

<details>
    <summary>👨‍🏫 Exemple d'utilisation</summary>

Voici **un exemple** de déclaration CSS permettant de modifier la **couleur de fond** et la **couleur du texte** du contenu de la balise `body` (donc de tout le document HTML).
Le texte entre `/* */` est un commentaire. Les commentaires permettent d'ajouter des précisions sans conséquence sur la mise en forme CSS.

```css
body {
   background-color: yellow; /* couleur de fond jaune  */
   color: #ffba00;           /* couleur du texte jaune */
}
```

</details>

#### <PracticeTitle />

1. Retourner dans l'application Notepad++
2. Revenir au fichier <FichierCSS />
3. **Modifier** la déclaration CSS ciblant la balise `body` de façon à modifier uniquement la **couleur d'arrière-plan** de votre document HTML (*inspirez-vous de l'exemple d'utilisation*)
4. **Ajouter** une nouvelle déclaration CSS ciblant la balise `h2` de façon à modifier la **couleur du texte** de chaque sous-titre (*inspirez-vous de l'exemple d'utilisation et de ce qui a été fait pour* `h1`)




### 2.2. Gestion du texte

#### 💡 Principe
Les propriétés CSS `font-size` et `text-decoration` permettent respectivement d'ajuster la taille du texte et la décoration du texte (soulignement).

#### 📖 Propriétés CSS
| Propriété         | Description                   | Référence                                                                |
|-------------------|-------------------------------|--------------------------------------------------------------------------|
| `font-size`       | Taille du texte d'un élément  | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/font-size)       |
| `text-decoration` | Soulignement d'un élément     | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/text-decoration) |

<details>
    <summary>👨‍🏫 Exemple d'utilisation</summary>

Voici **un exemple** de déclaration permettant de grossir et souligner le texte de toute balise de classe `super` (c'est-à-dire ayant l'attribut `class="super"`) :

```css
.super {
    font-size: 150px;            /* taille en pixels */
    text-decoration: underline;  /* soulignement */
}
```

</details>


#### <PracticeTitle />

1. Retourner dans l'application Notepad++
2. Revenir au fichier <FichierCSS />
3. **Modifier** la déclaration CSS ciblant la balise `h1` de façon à grossir la **taille du texte** du titre principal
4. **Modifier** la déclaration CSS ciblant la balise `h2` de façon à **souligner** les sous-titres

### 2.3. Gestion des dimensions

#### 💡 Principe

Les propriétés CSS `width` et `height` permettent d'ajuster respectivement la largeur et la hauteur d'un élément.

#### 📖 Propriétés CSS
| Propriété | Description          | Référence                                                       |
|-----------|----------------------|-----------------------------------------------------------------|
| `width`   | Largeur d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/width)  |
| `height`  | Hauteur d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/height) |



<details>
    <summary>👨‍🏫 Exemple d'utilisation</summary>

Voici ci-dessous un exemple de déclaration CSS permettant de fixer la largeur de tout élément de classe `icone` à 10 pixels de large:

```css
.icone {
    width: 10px; /* largeur de l'élément en pixels */
}
```

</details>


#### <PracticeTitle />

1. Retourner dans l'application Notepad++
2. Revenir au fichier <FichierCSS />
3. **Ajouter** une déclaration CSS permettant de fixer la largeur (`width`) de tout élément de classe `affiche` à 150 pixels de large.

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
6. **Rechercher** la seule balise `<img>` présente dans le document et qui correspond à l'élément **image** de l'affiche du film
7. **Modifier** la balise pour lui ajouter la classe `affiche`

<details>
    <summary>💡 Solution</summary>

Après modification, le code HTML de la balise `img` doit être similaire à ceci :

```html
<img class="affiche" src="images/intouchable.jpg" alt="Affiche du film Intouchable" />
```

</details>

8. **Enregistrer** le fichier `CTRL+S`
9. Retourner dans le navigateur web
10. Rafraichir la page, un changement doit être observable au niveau de l'affiche du film


### 2.4 Expérimentation

Vous avez terminé et il reste plus de 5 minutes avant la fin de la séance ? Bravo !
Il vous reste encore beaucoup à découvrir et d'autres propriétés peuvent se révéler intéressantes :

| Propriété          | Description                       | Référence                                                                 |
|--------------------|-----------------------------------|---------------------------------------------------------------------------|
| `text-align`       | Alignement du texte               | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/text-align)       |
| `border`           | Bordure autour d'un élément       | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/border)           |
| `margin-bottom`    | Marge inférieure d'un élément     | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/margin-bottom)    |
| `background-image` | Image d'arrière-plan d'un élément | [Mozilla](https://developer.mozilla.org/fr/docs/Web/CSS/background-image) |

#### <PracticeTitle />

Tester chacune de ces propriétés. Ne pas hésiter à s'inspirer des exemples interactifs présentés sur les pages de référence.




## 📦 Envoi du travail

### Création du fichier ZIP

Pour faciliter le partage de plusieurs fichiers et dossiers, il est de regrouper l'ensemble dans un seul fichier au format ZIP.
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