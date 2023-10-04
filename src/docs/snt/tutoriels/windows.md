---
title: Tutoriel - Windows
description: Quelques fonctionnalités du système d'exploitation Windows
---

# L'environnement Windows

## Introduction

Ce tutoriel a pour objectif d'améliorer votre maîtrise de certaines fonctionnalités du système d'exploitation Windows.

!!! success "Objectifs"

    - Savoir identifier sa version de Windows
    - Savoir utiliser l'explorateur de fichiers
    - Savoir faire une capture d'écran
    - Savoir convertir en PDF
    - Savoir créer un fichier ZIP

## Préparation

### Espace de travail

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et travaux pratiques.

!!! note "Organisation de l'espace travail"

    === "Ordinateur portable"

        1. Lancez l'**explorateur de fichiers**
        2. Accédez au dossier **Documents**
        3. Créez un dossier nommé **SNT** *(s'il n'existe pas déjà)*

    === "Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans votre zone personnelle, créez un dossier nommé **SNT** *(s'il n'existe pas déjà)*

### Version du système d'exploitation

Selon la version de votre système d'exploitation, la disponibilité ou l'accès à certaines fonctionnalités peut
sensiblement varier.
Il est donc essentiel de connaître la version du système d'exploitation exécuté par l'ordinateur que vous utilisez.

!!! info "Identification de la version de Windows"

    === "Méthode 1"

        *(Attention, cette méthode ne fonctionne pas sur les ordinateurs du lycée)*

        1. Appuyez sur <span class=keys><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>R</kbd></span>
        2. Écrivez *« winver »* dans le champ de saisie **Ouvrir**
        3. Cliquez sur **OK**

    === "Méthode 2"

        1. Lancez l'application **Invite de commandes**
        2. Écrivez *« winver »* et appuyez sur ++return++

!!! note "Mise en pratique"

    Si vous ne la connaissez pas déjà, récupérez la version de votre système d'exploitation en utilisant l'une des deux méthodes.
    Il vous faut simplement savoir si vous êtes sous **Windows 10** ou **Windows 11**.
    C'est important l'accès aux fonctionnalités varie selon que vous soyez sur l'une ou l'autre des versions.

## L'explorateur de fichiers

### Lancement de l'application

L'explorateur de fichiers est une application fournie avec le système d'exploitation pour gérer les fichiers et les
dossiers.
Elle aussi appelée **Explorateur Windows** (*Windows Explorer* en anglais). Il existe plusieurs façons de lancer cette
application :

!!! info "Méthodes de lancement de l'explorateur de fichiers"

    - Par l'**icône** :material-folder-outline: présente dans la barre des tâches ;
    - Par un clic droit sur le **menu démarrer** (icône :fontawesome-brands-windows:) puis **Explorateur de fichiers** ;
    - Par le **raccourci clavier** <span class=keys><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>E</kbd></span>.

Tout menu s'affichant par un clic droit est appelé **menu contextuel**. Il apparaît par exemple lorsque vous effectuez
un clic droit sur le Bureau, une zone vide d'une fenêtre ou un fichier. Il présente différentes fonctionnalités
comme : ouvrir, modifier, imprimer, copier, coller, ...

!!! note "Mise en pratique"

    1. Lancez l'explorateur de fichiers des **3 façons** possibles
    2. Testez le raccourci clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>N</kbd></span> depuis l'explorateur de fichiers.<br>
       Celui-ci permet d'ouvrir une nouvelle fenêtre de l'explorateur de fichiers.<br>
       *(vous pouvez ainsi comparer deux dossiers ou glisser des fichiers de l'un vers l'autre)*

### Création d'un dossier

!!! info "Méthodes de création d'un dossier"

    La création d'un dossier peut s'effectuer de deux manières :

    - Par un clic droit sur une zone vide puis **Nouveau dossier**
    - Par le raccourci clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>⇧ Maj</kbd><span>+</span><kbd>N</kbd></span>

!!! warning "Ne pas confondre les touches"

    La touche du clavier <span class=keys><kbd>⇧ Maj</kbd></span> appelée **majuscule** (*Shift* en anglais), se situe juste au-dessus de la touche <span class=keys><kbd>Ctrl</kbd></span>.<br>
    Ne la confondez pas avec la touche **verrouillage des majuscules** <span class=keys><kbd>:fontawesome-solid-lock:</kbd></span> (*Caps Lock* en anglais).

!!! note "Mise en pratique"

    1. Placez-vous dans votre dossier **SNT**
    2. Créez-y le dossier **Tutoriels** en utilisant le raccourci clavier

### Création d'un fichier texte

La création d'un fichier texte s'effectue depuis le menu contextuel par un clic droit sur une zone vide d'un dossier puis
**Nouveau ▸ Document texte**

!!! note "Mise en pratique"

    1. Placez-vous dans votre dossier **Tutoriels**
    2. Cliquez avec le bouton droit pour ouvrir le menu contextuel
    3. Choisissez **Nouveau ▸ Document texte**
    4. Créez un nouveau document texte nommé **fable**
    5. Ouvrez le fichier **fable** avec l'application **Bloc-notes** (*double-cliquez sur le fichier*)
    6. Copiez <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>C</kbd></span> puis coller <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>V</kbd></span> le texte suivant :
       ```
       La Cigale, ayant chanté
       Tout l'été,
       Se trouva fort dépourvue
       Quand la bise fut venue
       ```
    7. Observez la présence du caractère `*` dans la barre de titre de l'application : `*fable`<br>
       Cela signifie que les modifications apportées au fichier n'ont pas encore été enregistrées.
    8. Enregistrez le fichier à l'aide du raccourci clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>S</kbd></span>

!!! warning "Sauvegardez régulièrement"

    Beaucoup d'utilisateurs débutants n'enregistrent leur travail qu'une fois celui-ci terminé.
    Sachez qu'une multitude d'événements ont pour conséquence le redémarrage ou l'extinction de votre ordinateur.
    Dans cette situation, tout le travail non sauvegardé est **irrémédiablement perdu**.

    Tout travail doit être enregistré **régulièrement** et cette opération est facilitée le raccourci
    clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>S</kbd></span>


### Copie d'un fichier

La fonction copier-coller existe sous l'explorateur de fichiers :

!!! note "Mise en pratique"

    1. Sélectionner le fichier **fable**
    2. Copier le fichier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>C</kbd></span>
    3. Coller le fichier au même endroit <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>V</kbd></span><br>
       Celui-ci est automatiquement nommé **fable - Copie**

### Extensions de fichiers

Par défaut, les extensions de fichiers (`.txt`, `.pdf`, ...) sont masquées par l'explorateur de fichier.
Ceci est bien souvent une source de confusion lorsqu'il s'agit de nommer ou renommer un fichier.
Voici comment la désactiver :

!!! info "Méthodes d'activation de l'affichage des extensions de noms de fichiers"

    === "Windows 11 (méthode 1)"

        - Lancez l'explorateur de fichiers
        - Cliquez sur **Afficher ▸ Afficher**
        - Activez l'option **Extensions de noms de fichiers**

    === "Windows 11 - (méthode 2)"

        - Lancez l'explorateur de fichiers
        - Cliquez sur **...** dans la barre d'outils
        - Cliquez sur **Options**
        - Cliquez sur l'onglet **Affichage**
        - Dans les paramètres avancés, décochez l'option **Masquer les extensions des fichiers dont le type est connu**
        - Cliquez sur **OK**

    === "Windows 10"

        - Lancez l'explorateur de fichiers
        - Cliquez sur l'onglet **Affichage**
        - Cochez la case **Extensions de noms de fichiers**

!!! note "Mise en pratique"

    Rendez visibles les extensions de fichier. Dans votre répertoire de travail, vous devriez voir apparaître les fichiers suivants :
    
    - `fable.txt`
    - `fable - Copie.txt`

### Renommage d'un fichier ou d'un dossier

Les fichiers et les dossiers peuvent être renommés de deux façons :

!!! info "Méthodes de renommage d'un fichier ou d'un dossier"

    - Par un clic droit sur l'élément à modifier pour afficher le menu contextuel, puis **Renommer**
    - Par un clic gauche sur l'élément à modifier pour le sélectionner, puis le **raccourci clavier** ++f2++

!!! note "Mise en pratique"

    Renommez le fichier **fable - Copie.txt** en **fable_v2.txt** en utilisant le raccourci clavier ++f2++

### Sélection de plusieurs fichiers ou dossiers

Les fichiers et dossiers peuvent être sélectionnés de plusieurs façons :

!!! info "Méthodes de sélection"

    - En gardant pressé le bouton gauche de souris depuis une zone vide et en la faisant glisser de manière à ce qu'un carré de sélection apparaisse (*sélection d'éléments consécutifs*)
    - En cliquant du bouton gauche sur le premier élément souhaité pour le sélectionner, puis clic gauche sur le dernier tout en pressant la touche <span class=keys><kbd>⇧ Maj</kbd></span> (*sélection d'éléments consécutifs*)
    - En gardant enfoncée la touche <span class=keys><kbd>Ctrl</kbd></span> et en cliquant un à un sur les éléments à sélectionner. Cliquer à nouveau sur un élément permet de le désélectionner (*sélection d'éléments distincts*)
    - En utilisant le raccourci clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>A</kbd></span> (*sélection de tous les éléments*)

!!! note "Mise en pratique"

    Exercez-vous sur tous modes de sélection afin de bien saisir leur principe de fonctionnement.<br>
    **Attention**, il s'agit de simplement sélectionner les fichiers. Ne faites aucune autre action.

### Déplacement de fichiers ou dossiers

Le déplacement d'un élément peut se faire simplement via un glisser-déposer.
Dans certaines situations, il peut être plus pratique d'utiliser la fonction couper-coller <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>X</kbd></span> - <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>V</kbd></span>

!!! note "Mise en pratique"

    1. Retournez dans l'explorateur de fichiers
    2. Placez-vous dans le dossier **Tutoriels**
    3. Créez y le dossier **Fables** en utilisant le raccourci clavier <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>⇧ Maj</kbd><span>+</span><kbd>N</kbd></span>
    4. Sélectionnez tous les fichiers dont le nom commence par *« fable »*
    5. Coupez <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>X</kbd></span>
    6. Placez-vous dans le dossier **Fables**
    7. Collez <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>V</kbd></span>

## Les outils

### Capture d'écran

Il est parfois nécessaire de faire une capture d'une région ou de l'intégralité de l'écran.
Sous Windows, il existe plusieurs façons de procéder :

!!! info "Méthodes de capture d'écran"

    - Le raccourci clavier <span class=keys><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>⇧ Maj</kbd><span>+</span><kbd>S</kbd></span> *(enregistre dans le presse-papier)*
    - Le raccourci <span class=keys><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>impr.écran</kbd></span> *(enregistre dans le répertoire `Images\Captures d'écran`)*
    - L'application **Outil Capture d'écran** *(enregistre dans un fichier ou le presse-papier)*

!!! note "Mise en pratique"

    Toutes les captures d'écran demandées ci-après devront être effectuées en utilisant la méthode du raccourci clavier 
    <span class=keys><kbd>:fontawesome-brands-windows:</kbd><span>+</span><kbd>⇧ Maj</kbd><span>+</span><kbd>S</kbd></span> :
    
    1. Lancez l'application **Microsoft Word** ou **LibreOffice Writer**
    2. Faites une capture rectangulaire et coller dans le document
    3. Faites une capture de forme libre et coller dans le document
    4. Faites une capture de fenêtre et coller dans le document
    5. Faites une capture plein écran et coller dans le document
    6. Enregistrer le document <span class=keys><kbd>Ctrl</kbd><span>+</span><kbd>S</kbd></span> dans le dossier **Tutoriels** en le nommant **captures**

### Conversion PDF

La conversion d'un contenu au format en PDF s'effectue toujours depuis l'application où le contenu a été conçu.

??? info "Export PDF depuis Microsoft Word"

    - Enregistrez avant toute chose votre document au format **Document Word (*.docx)**<br>
      *(pour rappel, un fichier PDF n'est pas modifiable)*
    - Enregistrez de nouveau votre fichier via la fonction **Enregistrer sous...**
    - Choisissez le format de fichier **PDF**

??? info "Export PDF depuis LibreOffice Writer"

    - Enregistrez avant toute chose le fichier au format **Texte ODF (*.odt)**<br>
      *(pour rappel, un fichier PDF n'est pas modifiable)*
    - Cliquez sur l'entrée **Fichier** du menu
    - Choisissez l'option **Exporter vers ▸ Exporter directement au format PDF**

??? info "Export PDF depuis n'importe quelle application"

    - Trouvez et exécutez la fonction **Imprimer**
    - Sélectionnez l'imprimante **Microsoft print to PDF**

!!! note "Mise en pratique"

    1. Retournez dans l'explorateur de fichiers
    2. Ouvrez votre document **captures**
    3. Exportez-le au format PDF *(utiliser l'export PDF depuis Microsoft Word ou LibreOffice Writer)*
    4. Consultez la page d'accueil de [www.lemonde.fr](https://www.lemonde.fr)
    5. Exportez-la au format PDF *(utiliser l'export PDF depuis n'importe quelle application)*

### Création d'un fichier ZIP

Pour faciliter le partage de plusieurs fichiers et dossiers, il est possible de regrouper l'ensemble dans un seul fichier au format ZIP.
Voici les instructions selon la version du système d'exploitation de l'ordinateur utilisé :

!!! info "Méthodes de création d'un fichier ZIP"

    === "Windows 11"

        - Lancez l'explorateur de fichiers
        - Identifiez le dossier à compresser
        - Cliquez une seule fois avec le bouton gauche sur le dossier pour le sélectionner
        - Cliquez avec le bouton droit sur le dossier
        - Choisissez l'option **Compresser dans le fichier ZIP**
    
    === "Windows 10"

        - Lancez l'explorateur de fichiers
        - Identifiez le dossier à compresser
        - Cliquez une seule fois avec le bouton gauche sur le dossier pour le sélectionner
        - Cliquez avec le bouton droit sur le dossier
        - Choisissez l'option **Envoyer vers ▸ Dossier compressé**

!!! note "Mise en pratique"

    1. Retournez dans l'explorateur de fichiers
    2. Placez-vous dans le répertoire **SNT**
    3. Testez la compression sur le dossier **Tutoriels**