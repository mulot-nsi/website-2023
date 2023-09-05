# Projet - Présentez-vous

!!! danger "Version provisoire"

    L'énoncé de projet est cours de remaniement


## Introduction

Ce projet a pour objectif la création d'une pages web pour vous présenter, ainsi qu'une page web pour présenter un ou plusieurs de vos centres d'intérêt.
Des **contraintes techniques** seront à respecter mais toute liberté est donnée quant centres d'intérêt que vous souhaitez présenter (dans les limites imposées par la [legislation française](https://www.demarches.interieur.gouv.fr/particuliers/responsabilite-contenus-publies-internet-quelles-regles)).
Vous serez évalués sur le respect des contraintes techniques et votre maîtrise des langages HTML et CSS.

!!! warning "Projet individuel"
    
    Vous pouvez partagez vos découvertes et astuces avec vos camarades cependant, ce travail reste individuel et il est interdit d'échanger du code.

## Consignes

### Pages imposées

Votre site web devra obligatoirement contenir 2 pages :

!!! info "Page de présentation"

    - C'est la page principale, elle est consacrée à vous présenter. 
    - Son fichier doit être nommé `index.html`
    - Contenu de la page
        - Nom, prénom
        - Une photo (vous-même ou un avatar)
        - Votre classe
        - Vos spécialités
        - Votre souhait d'études supérieures et/ou de métier
        - Vos centres d'intérêt
        - ...

!!! info "Page Centres d'intérêt"

    C'est une page dédiée à la présentation de l'auteur du site (vous), par exemple :

### Organisation des fichiers

L'arborescence des fichiers de votre site devra respecter l'organisation suivante :

```
nom_prenom_siteweb
├── css
│   └── style.css
├── images
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── index.html
└── page2.html
```

### Éléments HTML et propriétés CSS obligatoires

Vous êtes libres d'utiliser tous les éléments et propriétés CSS qui vous sembleront nécessaires.
Cependant, vous devrez obligatoirement faire usage des éléments et propriétés listés ci-après.

#### Éléments HTML

| Élément                      | Balises                                       | Commentaire                                                                                                                          |
|:-----------------------------|:----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| Titre niveau 1               | `<h1></h1>`                                   | Un seul par page.<br />Présent sur toutes les pages                                                                                  |
| Titre niveau 2 (sous-titre)  | `<h2></h2>`                                   |                                                                                                                                      |
| Paragraphe                   | `<p></p>`                                     |                                                                                                                                      |
| Fort                         | `<strong></strong>`                           |                                                                                                                                      |
| Emphase                      | `<em></em>`                                   |                                                                                                                                      |
| Image                        | `<img src="" alt="" />`                       | Ne pas oublier l'attribut `alt`.<br/>Pas d'images externes. Toutes les images doivent être enregistrées dans le répertoire `images`  |
| Lien hypertexte              | `<a href="url"></a>`                          | Penser à la navigation entre les pages.<br/>Vous devez avoir au moins un lien externe.                                               |
| Liste à puces (ou numérotée) | `<ul><li></li></ul>`<br/>`<ol><li></li></ol>` |                                                                                                                                      |
| Tableau                      | `<table></table>`                             |                                                                                                                                      |
| Titre                        | `<title></title>`                             | Présent sur toutes les pages                                                                                                         |
| Métadonnée description       | `<meta name="description" content="" />`      | Présent sur toutes les pages                                                                                                         |
| Liens vers ressource CSS     | `<link rel="stylesheet" href="" />`           | Présent sur toutes les pages                                                                                                         | 

#### Propriétés CSS

| Style / Sélecteur   | Propriété CSS | Commentaire                                                   |
|:--------------------|:--------------|:--------------------------------------------------------------|
| Couleur du texte    | `color`       |                                                               |
| Couleur du fond     | `background`  |                                                               |
| Alignement du texte | `text-align`  | Pratique pour centrer des images par exemple                  |
| Largeur             | `width`       | Usage facultatif mais pratique pour redimensionner les images |
| Sélecteur de balise | -             | Exemple : `h1 { ... }`                                        |
| Sélecteur de classe | -             | Exemple : `.ma-classe { ... }` (ne pas oublier le `.`)        |

## Envoi du projet

### Validation du code

Le code HTML de chaque page Web doit être indenté de façon à ce qu'on puisse bien identifier l'ouverture et la fermeture des balises.

Le code HTML devra être vérifié en chargeant chacune de vos pages sur le site [W3C Markup Validation Service](https://validator.w3.org/#validate_by_upload+with_options). Il ne devra comporter aucune erreur.

Le code CSS devra également être vérifié en le chargeant sur un autre site [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_upload).

### Rendu du projet

Vous déposerez dans l'ENT, selon la date indiquée par votre enseignant, une archive ZIP de votre dossier contenant l'ensemble des fichiers du site.
Pour rappel, le dossier à compresser sera nommé `nom_prenom_siteweb`. L'archive zip sera nommée `nom_prenom_siteweb.zip`.
