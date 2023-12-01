---
title: Le Web - Projet - Minisite web
description: Création d'un minisite web
---

# Minisite web

Ce projet a pour finalité la création d'un minisite web. Il peut être réalisé seul ou en équipe (3 élèves maximum).
Les contraintes techniques doivent être respectées et impliquent la présence de certaines balises.
Le site doit disposer d'un nombre minimum de pages, variable selon la taille de l'équipe :

<figure markdown>
| Taille   | Nombre de pages web                                |
|:---------|:---------------------------------------------------|
| 1 élève  | 2 pages minimum (1 page d'accueil et 1 sous-page)  |
| 2 élèves | 3 pages minimum (1 page d'accueil et 2 sous-pages) |
| 3 élèves | 4 pages minimum (1 page d'accueil et 3 sous-pages) |
</figure>

Vous êtes libres du choix du sujet traité par votre site sous réserve qu'il n'y ait aucune infraction à la loi.
Pour en savoir plus sur les infractions potentielles, consultez la page
[:material-link: Responsabilité des contenus publiés sur internet : quelles sont les règles ?](https://www.service-public.fr/particuliers/vosdroits/F32075)

!!! info "Un peu d'inspiration ?"

    Pour avoir un aperçu du travai attendu,
    vous pouvez consulter les minisites réalisés par les élèves des précédentes années à l'adresse :
    [:material-link: https://minisites.mulot-nsi.fr](https://minisites.mulot-nsi.fr/){:target="_blank"}



## Préparation

### Espace de travail

Vous allez créer les dossiers nécessaires à accueillir le projet de minisite.
Notez que ceux-ci ont probablement tous été déjà créés dans le cadre des travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers**
        2. Dans le dossier `Document`, s'il n'y a pas de dossier nommé `SNT`, créez-le
        3. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans la **zone personnelle**, s'il n'y a pas de dossier nommé `SNT`, créez-le
        3. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le

### Téléchargement des fichiers

Votre minisite ne sera pas construit à partir de zéro. Une version d'amorçage est disponible en téléchargement.
Il comporte une page d'accueil, une sous-page et quelques éléments mis en forme grâce à une feuille de style CSS
indépendante.

!!! note "Téléchargement du site d'amorçage"

    1. Téléchargez le fichier ZIP contenant les fichiers d'amorçe du projet : [:material-download: télécharger](assets/SNT02_PRJ_MINISITE.zip){:download="SNT02_PRJ_MINISITE.zip"}
    2. Ouvrez le fichier ZIP<br>*(le navigateur l'ouvre automatiquement ou cliquez sur le fichier téléchargé)*
    3. Sélectionnez le dossier `init`
    4. Copiez le dossier `init` <span class="shortcut">++ctrl+c++</span>
    5. Collez le dossier `init` dans le dossier `SNT\Web` <span class="shortcut">++ctrl+v++</span>
    6. Renommez le dossier `init` en « <em>nom</em>**_minisite** » où *nom* correspond au nom de famille de chaque élève écrit en
      **minuscules**.<br>
      Exemple : si le minisite était réalisé par **Tim Berners-Lee** et **Robert Cailliau**, le dossier s'intitulerait `berners_lee_cailliau_minisite`

### Fichiers d'amorce

Les fichiers fournis pour créer votre minisite sont les suivants :

| Fichier             | Description                                                              |
|:--------------------|:-------------------------------------------------------------------------|
| `index.html`        | contient le code HTML de la page d'accueil                               |
| `style.css`         | contient le code CSS de mise en forme                                    |
| `page-exemple.html` | contient le code HTML d'une sous-page. Il sera nécessaire de le renommer |

### Logiciels

Pour visualiser les pages, vous utiliserez un navigateur Web comme Chrome, Firefox ou Edge.
Le contenu des pages peut être modifié à l'aide de l'application **Bloc-notes** de Windows.
Ce n'est cependant pas l'application la plus ergonomique et on lui préfèrera le logiciel **Notepad++** dont voici les
instructions de téléchargement.

!!! note "Installation du logiciel Notepad++"

    1. Téléchargez [:material-download: Notepad++ v8.6 **version portable** (zip)](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.6/npp.8.6.portable.x64.zip)
    2. Rendez-vous dans le dossier `Téléchargenment`
    3. Faites un **clic-droit** sur `npp.8.6.portable.x64.zip` et choisir l'option **Extraire tout...**
    4. Supprimez le fichier `npp.8.6.portable.x64.zip`
    5. Lancez l'application `notepad++.exe` depuis le le dossier `npp.8.6.portable.x64`
    6. Passez l'application en français en allant dans **Settings** puis **Preferences...** et choisir *Français* au niveau du champ **Localization**

## Développement

### Ouverture des fichiers

Vous allez maintenant ouvrir les fichiers du projet avec **notepad++**

!!! note "Démarrage des développements"

    1. Lancez **Notepad++**
    2. Ouvrez les fichiers `index.html`, `page-exemple.html` et `style.css`
    3. Visualisez la page  `index.html` dans un navigateur
    4. Commencez votre minisite sur le thème de votre choix ! Vous êtes libres de tout modifier, effacer, ajouter...

### Page d'accueil

La page d'accueil de votre minisite correspond au fichier `index.html`.
Vous êtes libre de la modifier entièrement. Elle devra cependant contenir au minimum les éléments suivants :

!!! info "Balises obligatoires sur la page d'accueil"

    - Un titre de page (visible au niveau de l'onglet du navigateur et géré par la balise `#!html <title>`)
    - Un titre principal (balise `#!html <h1>`)
    - Au moins un paragraphe de texte (balise `#!html <p>`)
    - Un ou plusieurs liens vers d'autres pages de votre site (balise `#!html <a>`)
    - Un ou plusieurs liens vers des sites externes (balise `#!html <a>`)
    - Au moins une image (balise `#!html <img>`)
    - Indiquer le nom de chaque des auteurs de la page via la métadonnée `author`<br>
      (balise `#!html <meta name="author" content="nom des auteurs">` située dans `#!html <head>`)

!!! danger "Attention à la gestion des images"
    
    Les images doivent être locales. Vous devez les télécharger et les placer dans le même dossier que votre page web pour l'utiliser.
    Vous devez les renommer pour passer leur nom de fichier en minuscules.
    
    Pour insérer une image sur une page web, il suffira simplement d'écrire le nom du fichier dans l'attribut `src` de la balise `#!html <img>`. 

### Sous-pages

Les sous-pages correspondent au fichier `page-exemple.html` et à toutes les autres pages web que vous pourriez ajouter
et nommer librement.

!!! warning "Renommer et modifier les exemples"

    Attention, le fichier `page-exemple.html` est un exemple, vous devez le renommer et modifier son contenu.

Les sous-pages devront impérativement disposer des éléments suivants :

!!! info "Balises obligatoires sur les sous-pages"

    - Un titre de page (visible au niveau de l'onglet du navigateur et géré par la balise `#!html <title>`)
    - Un titre principal (balise `#!html <h1>`)
    - Un paragraphe de texte (balise `#!html <p>`)
    - D'un lien de retour vers la page d'accueil de votre site (balise `#!html <a href="index.html">...</a>`)
    - Indiquer le nom de chaque des auteurs de la page via la métadonnée `author`<br>
      (balise `#!html <meta name="author" content="nom des auteurs">` située dans `#!html <head>`)

### Mise en forme CSS

Les pages web sont associées au fichier `style.css` qui contient le code CSS permettant la mise en forme des éléments.
Pour rappel, l'association entre une page web et le fichier `style.css` s'effectue à l'aide d'une
balise `#!html  <link>` à placer à l'intérieur des balises `#!html  <head> ... </head>` :

```html

<head>
    ...
    <link href="style.css" rel="stylesheet">
    ...
</head>
```

### Enrichissement du site

Tout en conservant les minimums demandés, vous pouvez consulter les contenus suivants afin d'enrichir vos pages :

- [Apparence du texte](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3/8061298-changez-lapparence-du-texte){:target="_blank"}
- [Couleur et fond](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3/8061312-ajoutez-de-la-couleur-et-un-fond){:target="_blank"}
- [Bordures et ombres](https://openclassrooms.com/fr/courses/1603881-creez-votre-site-web-avec-html5-et-css3/8061337-creez-des-bordures-et-des-ombres){:target="_blank"}
- [Images](https://developer.mozilla.org/fr/docs/Learn/HTML/Multimedia_and_embedding/Images_in_HTML){:target="_blank"}

## Envoi du travail

### Création d'un fichier ZIP

Pour faciliter l'envoi de plusieurs fichiers et dossiers, il est possible de tous les regrouper dans un unique fichier
au format ZIP. Suivez les instructions selon l'ordinateur utilisé :

!!! info "Création d'un fichier ZIP"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers** 
          <span class="keys shortcut"><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>E</kbd></span>
        2. Accédez au dossier `SNT\web`
        3. Ajoutez le mot-clé **public** au dossier de votre minisite si vous souhaitez qu'il soit potentiellement mis en ligne.<br>
           Exemple: `berners_lee_cailliau_minisite` deviendrait `berners_lee_cailliau_minisite_public` 
        4. Effectuez un clic droit sur le dossier `xxx_minisite` afin d'afficher son menu contextuel
        5. Choisissez l'option :material-folder-zip-outline: **Compresser dans un fichier ZIP**

    === ":material-desktop-tower: Ordinateur fixe"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers**
        2. Depuis votre dossier personnel, accédez au dossier `SNT\web`
        3. Ajoutez le mot-clé **public** au dossier de votre minisite si vous souhaitez qu'il soit potentiellement mis en ligne.<br>
           Exemple: `berners_lee_cailliau_minisite` deviendrait `berners_lee_cailliau_minisite_public` 
        4. Effectuez un clic droit sur le dossier `xxx_minisite` afin d'afficher son menu contextuel
        5. Choisissez l'option **Envoyer vers ▸ Dossier compressé**

!!! danger "Attention au poids du fichier ZIP"

    Attention, votre fichier ZIP doit faire **4 Mo maximum** sans quoi il ne vous sera pas possible de le déposer sur Pronote.
    Vous devez donc être attentif au poids des médias (images, vidéos, sons) ajoutés à votre minisite.


### Envoi du fichier ZIP

Une fois votre fichier ZIP créé, vous pouvez le déposer sur Pronote.

!!! info "Dépot du travail sur Pronote"

    1. Connectez-vous à l'ENT : [:material-link: https://ent.iledefrance.fr](https://ent.iledefrance.fr){:target="_blank"}
    3. Accédez à l'application **Pronote**
    4. Depuis l'accueil, recherchez le devoir **SNT02 - PRJ - Mini-site web**
    5. Cliquez sur le bouton <span class="pronote-button">Déposer ma copie</span>
    6. Cliquez sur le bouton **Un seul fichier (*.pdf, *.doc, ...)**
    7. Déposez votre fichier ZIP

### Critères d'évaluation

!!! success "Livrable"

    - Déposé sur Pronote à l'heure
    - Envoyé sous forme d'un fichier ZIP
    - Nom du dossier du minisite correct

!!! success "Équipe"

    - Nom de chaque membre indiqué en méta-données des pages (indiqué même si vous travaillez seul)
    - Respect de la contrainte du nombre de pages

!!! success "Programmation"

    - Suppression des fichiers exemple (`earth.jpg` et `page-exemple.html`)
    - Nom de tout fichier en minuscules et sans accents
    - Qualité du code HTML
    - Qualité du code CSS
    - Investissement général 