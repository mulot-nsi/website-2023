---
title: Le Web - TP1 Le langage HTML
description: Découverte du langage HTML
---

# Le langage HTML

## Introduction

Toutes les pages que vous pouvez consulter sur le Web sont construites à partir d'un même langage informatique :
le langage **HTML** *(pour HyperText Markup Language)*.
Dans le cadre de ces travaux pratiques, vous allez découvrir ce langage HTML et créer votre propre page.

!!! danger "Important"

    Ces travaux pratiques ont vocation à vous préparer au projet de chapitre consistant à créer un mini-site web.
    Suivez attentivement chaque consigne, lisez chaque explication et signalez toute incompréhension.

## Préparation

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et
travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'**explorateur de fichiers**
        2. Accédez au dossier **Documents**
        3. Créez un dossier nommé **SNT** *(s'il n'existe pas déjà)*
        4. Entrez dans le dossier **SNT** et créez-y le dossier **Web**

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans votre zone personnelle, créez un dossier nommé **SNT** *(s'il n'existe pas déjà)*
        4. Entrez dans le dossier **SNT** et créez-y le dossier **Web**

## Code source d'une page web

### Affichage du code source

En informatique, on appelle **code source** les instructions textuelles d'exécution d'un programme ou de création d'un
contenu.
Une page web est un contenu construit à partir d'un code source écrit en langage **HTML**.

Pour voir visualiser une page web, vous avez besoin d'un **navigateur web** *(Chrome, Firefox, ...)*.
C'est une application capable d'afficher une page web à partir de son code HTML. Mais à quoi ressemble du code HTML ?

!!! note "Mise en pratique"

    Il est possible de visualiser le code source de n'importe quelle page web directement depuis un navigateur web.

    1. Rendez-vous sur la page de démonstration : [demo.html](exemples/demo.html){:target="_blank"}
    2. Utilisez le raccourci clavier ++ctrl+u++
    3. Essayez de faire la distinction entre le contenu et le code permettant de structurer ce contenu

!!! info "Cours"

    En observant le code source, vous devriez avoir constaté que certaines portions de texte telles que `<body>`, `<p>` ou `<strong>` sont mises en valeur.
    Ces textes sont appelés **balise**. Ils constituent le langage HTML et permettent de définir et structurer le contenu d'une page web.

!!! example "Exemple - L'élément paragraphe"

    La balise `<p>` permet de définir un élément paragraphe.
    Il est donc possible de structurer un contenu sous forme d'un paragraphe en le délimitant :
    
    - par une balise ouvrante `<p>` *(début du paragraphe)* ; 
    - et une balise fermante `</p>` *(fin du paragraphe)*.
    
    === ":material-code-tags: Code"
        ```html
        <p>Ceci est un premier paragraphe</p>
        <p>Ceci est un second paragraphe</p>
        ``` 
    === ":material-application-outline: Affichage"
        Ceci est un premier paragraphe

        Ceci est un second paragraphe

!!! example "Exemple - L'élément important"

    La balise `<strong>` permet de signaler une portion de texte comme étant importante.
    Il est possible de structurer un contenu ainsi en le délimitant :

    - par une balise ouvrante `<strong>` *(début du texte important)* ; 
    - et une balise fermante `</stong>` *(fin du texte important)*.

    === ":material-code-tags: Code"
        ```html
        <p>
            Ceci est un premier paragraphe.
            Il est plus <strong>important</strong> que le second !
        </p>
        <p>Ceci est un second paragraphe.</p>
        ``` 
    === ":material-application-outline: Affichage"
        Ceci est un premier paragraphe.
        Il est plus **important** que le second !

        Ceci est un second paragraphe

    :material-alert: Vous noterez que les espaces et les sauts de ligne du code source ne sont pas pris en compte pour l'affichage.

### Inspection du code source

Il existe une autre façon de consulter le code source d'une page web en utilisant la fonction **inspecter** du
navigateur.
Celle-ci permet de retrouver le code HTML associée à une partie visible de la page ou inversement, de retrouver la zone
d'affichage correspondant à une portion du code source.

!!! note "Mise en pratique"

    1. Rendez-vous sur la page de démonstration : [demo.html](exemples/demo.html){:target="_blank"}
    2. Lancez l'inspecteur de code source en utilisant l'une des méthodes suivantes :
        - Faire un clic droit sur la page puis « Inspecter »
        - Utiliser le raccourci clavier ++ctrl+shift+i++
    3. Identifiez les balises permettant de constuire une liste à puces

## Création d'une page web

Vous allez créer votre première page HTML. Pour cela, il est nécessaire d'utiliser un éditeur de texte tel que l'
application Bloc-notes sous Windows, Notepad++ ou Visual Studio Code.

Un **fichier texte** ne doit pas être confondu avec un document texte élaboré à partir de logiciels comme Microsoft Word
ou LibreOffice Writer.
Un fichier texte ne contient que des caractères sans aucune information de présentation *(par exemple la taille des
caractères, la couleur, ...)*.

### Création du fichier

2. Copier/coller le code HTML suivant :

```html
<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="author" content="Personne"/>
    <meta name="description" content="Ma toute première page HTML !"/>
    <title>Ma page !</title>
</head>
<body>
Bonjour, ceci est ma première page HTML
</body>
</html>
```

3. Activer le mode HTML depuis le menu via **Langage → H → HTML**
4. Enregistrer le fichier dans le dossier `langage_html` créé en début de TP en utilisant le raccourci clavier `CTRL+S`
   et en le nommant `page.html`
5. En utilisant l'Explorateur Windows, retrouver le fichier `page.html`
6. Double-cliquer sur le fichier `page.html`
7. Un navigateur Web doit s'ouvrir automatiquement et vous présenter son contenu

:::danger Cours
Les textes tels que `<title></title>` ou `<body></body>` sont appelés des **balises HTML**.
Les balises permettent de définir les **éléments structurant le contenu** d'un document HTML. Chaque élément joue un
rôle bien précis.
:::

## Gestion du texte

### Modification du titre de la page

La balise `<title></title>` permet de définir l'élément **titre** d'une page. Elle est contenue entre les
balises `<head></head>`
qui définissent l'élément **en-tête**. Ce dernier élément est utilisé pour préciser certaines caractéristiques et
informations concernant la page.
Aucune des données renseignées n'est directement visible pour l'internaute à l'exception du titre.

:::tip Explication
Les informations renseignées via les balises `<meta name="author" ...>` et `<meta name="description" ...>` sont par
exemple utilisées par
les moteurs de recherche *(Google, Bing, ...)* pour afficher les résumés de la page de résultats d'une recherche.
:::

#### 🛠 Modifier le titre d'une page

1. Retourner dans l'application **Notepad++** sans fermer le navigateur avec le raccourci clavier `ALT+Tab`
2. Retrouver le texte *"Ma page !"*. Il se situe au niveau des balises `<title></title>`.
3. Remplacer *"Ma page !"* par un autre texte quelconque
4. Enregistrer le fichier en utilisant le raccourci clavier `CTRL+S`
5. Retourner dans le navigateur avec le raccourci clavier `ALT+Tab`
6. **Actualiser** la page en appuyant sur `F5` ou par le raccourci clavier `CTRL+R`
7. Localiser l'endroit, dans tout le navigateur, où est affiché le titre (cherchez bien 🧐 !). Constatez-vous le
   changement ?

### Modification du corps de la page

La balise `<body></body>` permet de définir l'élément **corps** d'une page, c'est-à-dire le contenu visible dans le
navigateur Web.

#### 🛠 Saisir le corps d'une page et gérer les sauts de ligne

1. Remplacer **le contenu** entre les balises `<body></body>` (sans supprimer celles-ci) par cet extrait de *La Cigale
   et la Fourmi* de Jean de La Fontaine :

```
La Cigale, ayant chanté
Tout l'été,
Se trouva fort dépourvue
Quand la bise fut venue.
Pas un seul petit morceau
De mouche ou de vermisseau.
Elle alla crier famine
Chez la Fourmi sa voisine,
La priant de lui prêter
Quelque grain pour subsister
Jusqu'à la saison nouvelle.
```

2. Enregistrer votre fichier (`CTRL+S`)
3. Retourner dans le navigateur (`ALT+Tab`)
4. Actualiser la page (`F5` ou `CTRL+R`)
5. Qu'observez-vous ?

:::tip Explication
En HTML, les sauts de ligne présents dans le code source ne sont pas pris en compte, tout comme les espacements
multiples.
Tout saut de ligne doit être explicitement indiqué grâce à la balise `<br>`
:::

6. Ajouter la balise `<br>` à la fin de chaque ligne afin de correctement mettre en forme le texte

#### 🛠 Création de votre première page HTML

1. Lancer l'application **Notepad++**

<details>
<summary>📦 Instructions pour obtenir Notepad++ (si absent de votre ordinateur)</summary>

L'application Bloc-Notes de Windows n'est pas la plus pratique pour travailler sur du code HTML.
Il existe des applications plus appropriées dont les fonctionnalités facilitent grandement l'écriture du code.

#### 🛠 Télécharger et lancer Notepad++

1.
Télécharger [Notepad++ v8.4.6 version portable (zip)](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.6/npp.8.4.6.portable.x64.zip)
2. Se rendre dans le répertoire où le fichier téléchargé a été enregistré
3. Faire un **clic-droit** sur celui-ci et choisir l'option **Extraire tout...**
4. Lancer l'application depuis le dossier décompressé
5. Passer l'application en français en allant dans **Settings** puis **Preferences...** et choisir *Français* au niveau
   du champ **Localization**

</details>

## Structuration du texte

### Une nouvelle page

Vous allez maintenant créer une page dédiée à votre film préféré.

:::caution Pas de film préféré ?
À défaut d'avoir un film préféré, décrire le film *Intouchables*. C'est actuellement le 3<sup>ème</sup> film ayant
totalisé le plus d'entrées en France à ce jour avec 19 490 688 d'entrées.
:::

#### 🛠 Créer la nouvelle page HTML

1. Créer un nouveau fichier dans Notepad++
2. Copier/coller le code ci-dessous :

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Mon Film Préféré</title>
</head>

<body>
TITRE DU FILM

<p><img src="" alt=""></p>

<p><em>Ce document a été réalisé par PRENOM NOM</em></p>

Informations générales

<ul>
    <li>Année de Sortie :</li>
    <li>Réalisateur :</li>
    <li>Acteurs Principaux :</li>
    <li>Genre :</li>
</ul>

Résumé

Sources des informations et médias

</body>
</html>
```

3. Activer le mode HTML depuis le menu via **Langage -> H -> HTML**
4. Enregistrer immédiatement le fichier dans le dossier `langage_html` en le nommant `film.html`
5. Visualiser le fichier dans un navigateur

### Les éléments de titre

En HTML, il est possible de créer des éléments de titre au sein d'une page grâce aux balises suivantes :

- `<h1></h1>` *(titre)*,
- `<h2></h2>` *(sous-titre)*,
- `<h3></h3>` *(sous-sous-titre)*
- ...
- `<h6></h6>`

#### 🛠 Définir le titre principale

1. Définir le texte *TITRE DU FILM* en tant que titre principal de la page en l'englobant par des balises `<h1></h1>`

:::info Exemple

```html
<h1>TITRE DU FILM</h1>
```

:::

2. Enregistrer votre fichier et visualiser le résultat dans le navigateur après actualisation (`F5` ou `CTRL+R`)
3. Personnaliser le texte *"TITRE DU FILM"* par le nom du film choisi
4. Visualiser le résultat (toujours en enregistrant et actualisant)

#### 🛠 Définir les titres secondaires

1. Englober chacun des textes suivants par le couple de balises `<h2></h2>` :
    - Informations générales
    - Résumé
    - Sources d'information

:::info Exemple

```html
<h2>Informations générales</h2>
```

:::

2. Visualiser le résultat (toujours en enregistrant et actualisant)

### L'élément de haute importance

Vous allez compléter la section *Information générale* et utiliser une nouvelle balise pour mettre en valeur les
descripteurs *(Année de sortie, Réalisateur, ...)*.

#### 🛠 Mettre en valeur des portions de texte

1. Renseigner les informations générales du film choisi
2. Englober chacun des textes suivants par le couple de balises `<strong></strong>` :
    - Année de Sortie :
    - Réalisateur :
    - Acteurs Principaux :
    - Genre :

:::info Exemple

```html

<li><strong>Année de sortie : </strong> 2008</li>
```

:::

### L'élément paragraphe

Vous allez ajouter du contenu à la section *Résumé*. Sur papier, les longs textes sont structurés en paragraphes.
Il est possible de faire de même en HTML à l'aide de l'élément paragraphe défini par le couple de balise `<p></p>`.

#### 🛠 Ajouter le résumer du film

1. Retrouver un résumé de votre film
2. Copier/coller le texte trouvé *(vous êtes autorisés pour cette fois-ci, mais ça reste du plagiat et c'est interdit)*
3. Le structurer en paragraphes à l'aide de couples de balises `<p></p>`

:::info Exemples
Exemple de paragraphe très court.

```html
<p>Une seule ligne</p>
```

Les sauts de ligne n'étant pas significatifs, il est possible d'écrire ce même paragraphe comme ci-dessous.

```html
<p>
    Une seule ligne
</p>
```

Il est possible de définir plusieurs paragraphes à la suite.
Un passage à la ligne est automatiquement appliqué par le navigateur après chaque paragraphe.

```html
<p>Paragraphe 1</p>
<p>Paragraphe 2</p>
```

:::

### L'élément lien hypertexte

L'une des fonctionnalités révolutionnaires du Web est le **lien hypertexte**, c'est-à-dire la possibilité d'insérer un
lien vers une autre page située n'importe où sur le Web.
Un élément lien hypertexte se crée grâce au couple de balises `<a href=""></a>`. Vous constaterez une différence par
rapport aux autres balises déjà rencontrées par la présence de `href=""`.

Le texte `href=""` est un *attribut* de la balise `<a>`. Tout attribut a un nom (ici `href`) et une valeur (écrite entre
guillemets).
Les attributs permettent de transmettre des informations à une balise dont le fonctionnement se verra impacté.

L'attribut `href` permet d'indiquer l'URL du contenu vers lequel nous souhaitons faire pointer le lien hypertexte.
Le texte englobé par les balises `<a>` sera mis en valeur et rendu cliquable.

:::info Exemple
Voici un texte comportant un lien hypertexte vers le site de lycée. Le texte cliquable sera *site du lycée*.

```html
Rendez-vous sur le <a href="http://www.lyceebachelardchelles.fr"/>site du lycée</a>
```

Rendez-vous sur le [site du lycée](http://www.lyceebachelardchelles.fr)
:::

#### 🛠 Créer des liens hypertextes

1. Retrouver l'URL des pages où vous avez trouvé les informations concernant votre film
2. Ajouter dans la section *Sources* un paragraphe précisant les sites utilisés en insérant un lien vers chacun

### L'élément image

Il est possible d'insérer un élément image sur une page Web grâce à la balise `<img>`. Elle dispose des attributs
suivants :

- L'attribut `src` qui est le chemin ou l'URL d'une image
- L'attribut `alt` qui est un texte alternatif qui sera présenté par le navigateur si l'affichage de l'image se révèle
  impossible

:::info Exemple
Nous avons téléchargé un fichier image `image_800x600.jpg` que nous avons enregistré dans le même dossier que notre page
HTML.
Cette image représente l'affiche du film *Intouchable*. Voici ci-dessous le code de la balise `<img>` dans cette
situation.

```html
<img src="image_800x600.jpg" alt="Affiche du film Intouchables">
```

:::

#### 🛠 Insérer une image

1. Trouver sur le Web une image de l'affiche de votre film au format `.jpg` ou `.png`
2. **Télécharger** l'image et l'enregistrer dans le même répertoire que le fichier `film.html`
3. Modifier la balise `<img>` déjà présente dans la page en conséquence
4. Visualiser le résultat

## 🏁 Vous avez terminé ?

### Le langage CSS

Le langage HTML permet de structurer le contenu d'un document. Le langage CSS permet de mettre en forme ce contenu.
Vous allez cette fois ajouter un peu de couleur à votre page grâce au langage CSS. Pour cela :

1. Modifier **l'en-tête** du document en ajoutant l'élément style ci-dessous

```html

<head>
    <meta charset="utf-8">
    <title>Mon film préféré</title>
    <style>
        body {
            background-color: lightyellow
        }

        h1 {
            color: red;
            text-align: center;
        }

        h2 {
            color: green;
        }

        img {
            max-width: 200px;
        }
    </style>
</head>
```

2. Enregistrer le document et visualiser le résultat dans un navigateur
3. Consulter les pages suivantes pour découvrir d'autres propriétés CSS
    - [Formatage du texte](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605329-formatez-du-texte)
    - [Couleur et fond](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605551-ajoutez-de-la-couleur-et-un-fond)
    - [Bordures et ombres](https://openclassrooms.com/fr/courses/1603881-apprenez-a-creer-votre-site-web-avec-html5-et-css3/1605694-creez-des-bordures-et-des-ombres)

### Les métiers du Web

- Découvrir les métiers du Web sur le site de l'ONISEP :
    - [Intégrateur/trice web](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/integrateur-integratrice-web)
    - [Webdesigner](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/webdesigner)
    - [Web-ergonome](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/web-ergonome)
    - [Spécialiste de l'accessibilité numérique](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/specialiste-de-l-accessibilite-numerique)
    - [Traffic Manager](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/traffic-manager)
    - [Chef/fe de projet Web](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/chef-cheffe-de-projet-web-mobile)
    - [Webmestre](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/webmestre)
    - [Rédacteur/trice](https://www.onisep.fr/Ressources/Univers-Metier/Metiers/redacteur-redactrice-on-line)

:::info
Travaux pratiques inspirés de
l'activité [Écriture d'une page Web](http://portail.lyc-la-martiniere-diderot.ac-lyon.fr/srv20/co/AA1_Activite.html) du
lycée La Martinière Diderot à Lyon.
:::