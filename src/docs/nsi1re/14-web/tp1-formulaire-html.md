---
title: TP1 - Formulaire HTML
description: Création d'un formulaire HTML et transmission de données
---

# Formulaire HTML

## Introduction

Nous souhaitons mettre en œuvre une base de données des élèves suivant l'option NSI en classe de première.
Pour l'acquisition des données, nous faisons le choix de développer un formulaire web proposant les fonctionnalités suivantes :

- Saisie du nom de l'élève
- Saisie du prénom de l'élève
- Saisie de l'année scolaire
- Choix de la classe de l'élève, parmi la liste exhaustive des classes de première du lycée
- Indication des autres options suivies par l'élève, parmi la liste exhaustive des options disponibles au lycée
- Indication de la poursuite ou non de l'option en classe de Terminale

Les données du formulaire seront transmises à un script de traitement chargé de l'enregistrement des données *(persistance)*.
Voici le nom des paramètres attendus pour chaque champ :

| Libellé                | Attribut `name`  |
|:-----------------------|:-----------------|
| Nom de l'élève         | `nom`            |
| Prénom de l'élève      | `prenom`         |
| Année scolaire         | `annee_scolaire` |
| Classe                 | `classe`         |
| Autres options suivies | `options`        |
| Poursuite en terminale | `poursuite`      |

## Préparation

### Espace de travail

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et
travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers** 
           <span class="keys shortcut"><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>E</kbd></span>
        2. Dans le dossier `Document`, s'il n'y a pas de dossier nommé `NSI`, créez-le
        3. Dans le dossier `NSI`, s'il n'y a pas de dossier nommé `chapitre_14`, créez-le
        4. Dans le dossier `chapitre_14` créez le dossier `tp1_formulaire`

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans la **zone personnelle**, s'il n'y a pas de dossier `NSI`, créez-le
        3. Dans le dossier `NSI`, s'il n'y a pas de dossier nommé `chapitre_14`, créez-le
        4. Dans le dossier `chapitre_14` créez le dossier `tp1_formulaire`

### Téléchargement des fichiers

Pour réaliser ces travaux pratiques, il est nécessaire de disposer de certains fichiers.

!!! note "Récupération des fichiers"

    1. Téléchargez le fichier ZIP contenant les fichiers nécessaires : [:material-download: télécharger](assets/NSI1RE14_TP1.zip){:download="NSI1RE14_TP1.zip"}
    2. Ouvrez le fichier ZIP<br>*(si le navigateur ne l'ouvre automatiquement, cliquez sur le fichier téléchargé)*
    3. Sélectionnez tous les fichiers et dossiers  <span class="shortcut">++ctrl+a++</span>
    4. Copiez tous les fichiers et dossiers <span class="shortcut">++ctrl+c++</span>
    5. Collez les fichiers dans le dossier `NSI\chapitre_14\tp1_formulaire` <span class="shortcut">++ctrl+v++</span>

## Partie 1 - création du formulaire

<figure class="illustration" markdown>
![Formulaire une fois terminé](images/formulaire.png)
<em>Formulaire de saisie des informations d'un élève</em>
</figure>

### Formulaire

L'élément HTML `#!html <form>` représente un formulaire. Celui-ci contient des contrôles interactifs permettant à un utilisateur de fournir des informations.

!!! example "Exemple"

    ```html
    <form>
        ...
    </form>
    ```
    
    Pour en savoir plus, consultez la documentation sur le site [:material-link: mozilla.org](https://developer.mozilla.org/fr/docs/Web/HTML/Element/form){:target="_blank"}

!!! note "Instructions"

    1. Ouvrez le fichier `index.html`
    2. Créez y simplement les balises d'ouverture et de fermeture du formulaire qui accueillera l'ensemble des champs de saisie

### Champ de saisie

L'élément HTML `#!html <input>` est utilisé pour créer un contrôle interactif dans un formulaire web qui permet à l'utilisateur de saisir des données.
Les saisies possibles et le comportement de l'élément `#!html <input>` dépendent fortement de la valeur de son attribut `type`.

!!! example "Exemple"

    <p class="codepen" data-height="300" data-theme-id="light" data-default-tab="html,result" data-slug-hash="GRLeVPj" data-editable="true" data-user="mulot-nsi" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;"></p>

    Pour en savoir plus, consultez la documentation sur le site [:material-link: mozilla.org](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input){:target="_blank"}

!!! note "Instructions"

    1. Créez le champ de saisie du **nom de l’élève**
    2. Créez le champ de saisie du **prénom de l’élève**
    3. Créez le champ de saisie de **l'année scolaire**

!!! danger "Attention"
    
    Pensez à bien renseigner l'attribut `name`, en accord avec le tableau de la section **objectif**




### Liste d'options

L’élément HTML `#!html <select>` représente un contrôle qui fournit une liste d’options parmi lesquelles l’utilisateur pourra faire un choix.

!!! example "Exemple"

    <p class="codepen" data-height="300" data-theme-id="light" data-default-tab="html,result" data-slug-hash="MWRRggz" data-editable="true" data-user="mulot-nsi" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;"></p>

    Pour en savoir plus, consultez la documentation sur le site [:material-link: mozilla.org](https://developer.mozilla.org/fr/docs/Web/HTML/Element/select){:target="_blank"}

!!! note "Instructions"

    1. Créez le champ de sélection de la **classe de l’élève** en utilisant l'élément **liste de choix**.
    2. Pensez à bien renseigner l'attribut `name`, en accord avec le tableau de la section **objectif**





### Cases à cocher

#### Principe

L’élément `<input type="checkbox">` correspond à une case à cocher qui permet de sélectionner/déselectionner une valeur.

:::tip Documentation
Consulter la page **[&lt;input type="checkbox"&gt;](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input/checkbox)**
:::

#### Exemple

```html
<input type="checkbox" name="options" value="option1" />Libellé Option 1<br />
<input type="checkbox" name="options" value="option2" />Libellé Option 2
```

<div style={{"text-align":"center", marginBottom:"3em"}}>
<input type="checkbox" name="options" value={"option1"}/>Libellé option 1<br />
<input type="checkbox" name="options" value={"option2"}/>Libellé option 2
</div>

#### <PracticeTitle />
Créer le champ d’indication des **autres options suivies** par l’élève en utilisant plusieurs occurrences de l’élément **case à cocher**.

:::caution Attention
Ne pas oublier de renseigner correctement l'attribut `name`, en accord avec le tableau de la section **objectif**
:::





### Boutons radio

#### Principe
L’élément `<input type="radio">` correspond à un bouton radio qui permet de sélectionner une seule valeur parmi un groupe de valeurs.

:::tip Documentation
Consulter la page **[&lt;input type="radio"&gt;](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input/radio)**
:::

#### Exemple

```html
    <input type="radio" value="1" name="reponse">Oui
    <input type="radio" value="0" name="reponse">Non
```

<div style={{"text-align":"center", marginBottom:"3em"}}>
    <input type="radio" value="1" name="reponse" />Oui
    <input type="radio" value="0" name="reponse" />Non
</div>


#### <PracticeTitle />

Créer le champ d’indication de **poursuite de l’option** en utilisant plusieurs occurrences de l’élément **bouton radio**.

:::caution Attention
Ne pas oublier de renseigner correctement l'attribut `name`, en accord avec le tableau de la section **objectif**
:::








## Partie 2 - Transmission des données

### Bouton de soumission

#### Principe
Afin de pouvoir transmettre le formulaire pour traitement, celui-ci doit disposer d'un bouton d'envoi.
L'élément HTML permettant la création de ce bouton est `<input type="submit">`

:::tip Documentation
Consulter la page **[&lt;input type="submit"&gt;](https://developer.mozilla.org/fr/docs/Web/HTML/Element/input/submit)**
:::

#### Exemple

```html
    <input type="submit" value="Texte du bouton" />
```

<div style={{"text-align":"center", marginBottom:"3em"}}>
    <input type="submit" value="Texte du bouton" />
</div>

#### <PracticeTitle />

1. Créer le bouton d'envoi du formulaire
2. Cliquer sur le bouton d'envoi du formulaire. Qu'observez-vous ?


### Destination du formulaire

Il est possible de spécifier une URL à laquelle transmettre les données du formulaire.
Nous souhaiterions les transmettre à l'URL suivante :

<div style={{"text-align":"center"}}>
<code>https://europe-west1-mulot-nsi.cloudfunctions.net/handle-get</code>
</div>

#### <PracticeTitle />

1. Modifier l'attribut `action` du formulaire de façon à transmettre les données à l'URL indiquée
2. Saisir des données et envoyer le formulaire. Qu'observez-vous ?
3. Que se passe-t-il si vous modifiez les données directement depuis l'URL ?
4. Est-il sécurisé d'avoir les données visibles depuis l'URL ?


### Méthode de transmission du formulaire

Il existe une autre méthode de transmission des données du formulaire.

#### <PracticeTitle />
1. Modifier la balise ouvrante du formulaire comme suit **(attention l'URL de l'action change)** :

```html
<form method="POST" action="https://europe-west1-mulot-nsi.cloudfunctions.net/handle-post">
```

2. Saisir des données et envoyer le formulaire. Qu'observez-vous ?
3. Où sont les données selon vous ? Essayer de les retrouver en activant le **mode développeur** du navigateur et en consultant les échanges réseau.



<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>