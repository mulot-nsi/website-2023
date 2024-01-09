---
title: Le langage CSS
description: Découverte du langage CSS
---

# La confidentialité

## Introduction

Ces travaux pratiques ont pour objectif de vous faire découvrir certains paramètres de configuration de votre navigateur
afin de modifier le moteur de recherche par défaut ou contrôler les cookies.

!!! warning "Attention"

    Ces travaux pratiques ont été conçus pour les navigateurs ci-dessous.
    Vous êtes libres d'utiliser tout autre navigateur cependant, vous devrez seul retrouver les fonctionnalités requises 
    dans les différents exercices

    - Le navigateur **Firefox** créé par [:material-link: Mozilla](https://www.mozilla.org/fr/){:target="_blank"}, une fondation sans but lucratif
    - Le navigateur **Chrome** créé par la société [:material-link: Google](https://about.google/intl/ALL_fr/)
    - Le navigateur **Edge** créé par la société Microsoft

## Préparation

### Espace de travail

Vous allez créer des dossiers afin de ne pas mélanger vos productions numériques entre vos différentes matières et
travaux pratiques.

!!! note "Organisation de l'espace travail"

    === ":material-laptop: Ordinateur portable"

        1. Lancez l'application <i class="icon file-explorer"></i> **Explorateur de fichiers**
        2. Dans le dossier `Document`, s'il n'y a pas de dossier nommé `SNT`, créez-le
        3. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le
        4. Dans le dossier `web`, créez le dossier `Confidentialité`

    === ":material-desktop-tower: Ordinateur fixe"

        1. Depuis le bureau, double-cliquez sur l'icône intitulée **Zone personnelle**
        2. Dans la **zone personnelle**, s'il n'y a pas de dossier nommé `SNT`, créez-le
        3. Dans le dossier `SNT`, s'il n'y a pas de dossier `web`, créez-le
        4. Dans le dossier `web`, créez le dossier `Confidentialité`

### Téléchargement des fichiers

Pour effectuer ce TP, il est nécessaire de télécharger certains fichiers :

!!! note "Récupération des fichiers"

    1. Téléchargez le document de comptre rendu : [:material-download: télécharger](assets/SNT02_TP_confidentialité.docx){:download="SNT02_TP_confidentialité.docx"}
    2. Déplacez le document dans le dossier `Confidentialité`
    3. Ouvrez le document afin de pouvoir répondre aux questions tout au long des travaux pratiques

## Les moteurs de recherche

### Identifier le moteur de recherche

Vous allez commencer par simplement faire le choix d'un navigateur web et effectuer une recherche.

!!! note "Instructions"
    
    1. Lancez le navigateur web de votre choix
    2. Effectuez une recherche quelconque depuis la barre d'adresse
    3. Répondes en questions suivante dans le compte rendu

!!! question "Questions"

    - Quel navigateur web utilisez-vous pour ces travaux pratiques ?
    - Avec quel moteur de recherche votre navigateur web a-t-il traité votre requête ?


### Changer de moteur de recherche

Il y a souvent confusion entre navigateur web et moteur de recherche.
Afin que vous puissiez faire clairement la distinction entre les deux, 
vous allez modifier le moteur de recherche utilisé par défaut par votre navigateur Web.

!!! note "Instructions"

    1. Accédez aux paramètres pour utliser Qwant comme moteur de recherche par défaut en utilisant l'aide ci-après
    2. Faites une recherche quelconque **depuis la barre d'adresse**. Cette fois-ci c'est Qwant qui doit avoir été appelé par votre navigateur web
    3. Faites une capture d'écran et ajoutez-là à votre compte rendu

!!! help "Aide - Changer de moteur de recherche pour Qwant"

    === ":material-firefox: Firefox"

        - Se rendre dans **Paramètres**
        - Se rendre dans **:material-magnify: Recherche**
        - Choisir **Qwant** pour **Moteur de recherche par défaut**

    === ":material-google-chrome: Chrome"

        <h5>Accès aux paramètres</h5>

        - Se rendre dans **:material-cog-outline: Paramètres**
        - Se rendre dans **:material-magnify: Moteur de recherche**<br>
          :material-alert: Qwant n'est pas proposé dans la liste des moteurs, il faut l'ajouter

        <h5>Ajout d'un nouveau moteur de recherche</h5>

        - Se rendre dans **Gérer les moteurs de recherche et la recherche sur les sites**
        - En face de **Recherche sur le site**, cliquer sur **Ajouter**
        - Saisir les informations suivantes :
        <table>
            <tbody>
                <tr><th>Moteur de recherche</th><td>`Qwant`</td></tr>
                <tr><th>Raccourci</th><td>`q`</td></tr>
                <tr><th>URL</th><td>`https://www.qwant.com/?q=%s`</td></tr>
            </tbody>
        </table>
        - Cliquer enfin sur :material-dots-vertical: en face de Qwant et choisir **utiliser par défaut**

    === ":material-microsoft-edge: Edge"
        
        - Se rendre dans **:material-cog-outline: Paramètres**
        - Se rendre dans **:material-lock-outline: Confidentialité, recherche et services**
        - Se rendre dans **Barre d'adresse et recherche** *(faire défiler jusqu'en bas pour voir l'entrée)*
        - Choisir **Qwant** pour **Moteur de recherche utilisé dans la barre d'adresses**

### Utilisation de vos données par les moteurs de recherche

Nous souhaitons comparer les moteurs de recherche Google et Qwant sur le respect de la vie privée.
Pour celà, vous allez lire des parties bien précises des règles de confidentialité élaborées par les entreprises 
propriétaires de ces moteurs. 

!!! info "Google - Règles de confidentialité"

    Se rendre sur la page [:material-link: Règles de confidentialité](https://policies.google.com/privacy?hl=fr#infocollect){:target="_blank"}
    et faire défiler le contenu pour lire les parties suivantes :

    - Infornations collectées par Google
        - Informations que nous collectons via nos services
            - Votre activité
            - Informations relatives à votre position géographique
        - Raisons pour laquelles nous collectons les informations
            - Proposer des services personnalisés, notamment en matière de contenu et d'annonces<br>*(les deux premiers paragraphes uniquement)* 

!!! info "Qwant - Politique de Confidentialité"

    Se rendre sur la page [:material-link: Politique de Confidentialité](https://about.qwant.com/legal/confidentialite/)
    et lire les parties suivantes :

    - Un moteur de recherche qui respecte votre vie privée
    - Un web ouvert et neutre à votre service
    - Une navigation sans publicité ciblée !
    - Vos données ne sont pas une monnaie d’échange
    - Une alternative made in France qui applique la législation européenne

!!! question "Questions"

    - **En résumant**, quelles sont les informations collectées par Google et comment le justifie-t-il ?
    - Quelle sont les données collectées par Qwant et comment le justifie-t-il ?
    - Quels avantages et inconvénients voyez-vous à utiliser l'un ou l'autre de ces moteurs de recherche ?

## Les cookies

Les cookies sont des informations que tout serveur web peut envoyer et stocker dans votre navigateur.
Des cookies peuvent être modifiés ou ajoutés directement par votre navigateur.
Les cookies sont renvoyés au serveur lors de chaque requête HTTP.

!!! question "Questions"

    - Selon vous, à quoi servent les cookies ?

### Les cookies techniques

Les cookies sont généralement mentionnés lorsqu'il est question de publicité. 
Cependant, ils se révèlent indispensables dans d'autres situations.

!!! note "Instructions"

    - Connectez-vous à l'ENT : [:material-link: https://ent.iledefrance.fr](https://ent.iledefrance.fr/)
    - Consultez les cookies déposés par l'ENT en suivant l'aide ci-dessous correspondant à votre navigateur 

!!! help "Aide - Consulter les cookies"

    === ":material-firefox: Firefox"

        - Cliquer avec le bouton droit n'importe où sur la page et choisir **Inpecter**
        - Se rendre sur l'onglet **Stockage**
        - Cliquer sur **Cookies**

    === ":material-google-chrome: Chrome"

        - Cliquer sur l'icône :material-tune-variant: à gauche de la barre d'adresse
        - Se rendre dans **:material-cookie-outline: Cookies et données des sites**
        - Se rendre dans **Gérer les données des sites sur l'appareil**

    === ":material-microsoft-edge: Edge"

        - Cliquer sur l'icône :material-lock-outline: à gauche de la barre d'adresse
        - Cliquer sur **Cookies (... en cours d'utilisation)**

Vous devez observer qu'un cookie a été déposé pour le domaine `ent.iledefrance.fr`.
Essayons de découvrir pour quelle raison en observant les conséquences de sa suppression.

!!! note "Instructions"

    - Revenez à la fenêtre de consultation des cookies
    - Supprimez tous les cookies du domaine `ent.iledefrance.fr`
    - Rechargez la page et répondre à la question ci-après

!!! question "Questions"

    - Quelle conséquence a eu la suppression des cookies ?
    - Quelle explication donneriez-vous à l'utilisation des cookies dans cette situation ?


### Les cookies tiers

!!! note "Instructions"

    - Rendez-vous sur [www.lemonde.fr](https://www.lemonde.fr)
    - Acceptez tous les cookies
    - Consultez les cookies présents sur le site

Vous devriez observer la présence de beaucoup plus de cookies. Vous êtes sur le site dont le nom de domaine est `monde.fr`.
Les cookies n'appartenant pas à ce domaine sont appelés des **cookies tiers**.
Ces cookies sont généralement utilisés pour suivre votre activité pour des raisons statistiques,
pour la personnalisation des contenus ou pour la publicité ciblée.

!!! question "Questions"

    Donnez un exemple de cookie tiers déposé sur le site web du journal Le Monde

### Contrôler les cookies

Vous pouvez contrôler la présence de ces cookies tiers de plusieurs façons :

- Les refuser lorsqu'un site vous présente sa fenêtre de **préférences sur les cookies**
- Supprimer tous les cookies d'un site précis
- Supprimer tous les cookies de votre navigateur
- Modification les paramètres relatifs à la confidentialité de votre navigateur

Vous allez modifier les paramètres de confidentialité de votre navigateur et observer les résultats sur le site 
[www.lemonde.fr](https://www.lemonde.fr).

!!! note "Instructions"

    - Modifiez les paramètres de confidentialité selon l'aide ci-après
    - Rafraichissez la page [www.lemonde.fr](https://www.lemonde.fr)
    - Consultez les cookies présents sur le site<br>
      (Si vous utilisez **Firefox** cliquez cette-fois sur le :materiel-shield-outline: de la barre d'adresse)
    - Répondez aux questions ci-après

!!! help "Aide - Modifier les paramètres de confidentialité"

    === ":material-firefox: Firefox"

        - Se rendre dans **Paramètres**
        - Se rendre dans **:material-lock-outline: Vie privée et sécurité**
        - Choisir **Stricte** comme **Protection renforcée contre le pistage**

    === ":material-google-chrome: Chrome"

        - Se rendre dans **:material-cog-outline: Paramètres**
        - Se rendre dans **:material-security: Confidentialité et sécurité**
        - Choisir de **Bloquer les cookies tiers** en tant que **comportement par défaut**

    === ":material-microsoft-edge: Edge"

        - Se rendre dans **:material-cog-outline: Paramètres**
        - Se rendre dans **:material-lock-outline: Confidentialité, recherche et services**
        - Choisir **Strict** comme **Protection contre le suivi**


!!! question "Questions"

    - Qu'observez-vous au niveau des cookies après avoir modifié les paramètres du navigateur ?
    - Souhaiteriez-vous être moins pisté par les sites web ? Si oui, pour quelle raison ?
    - La politique de confidentialité de Qwant évoque « une vision du Web sans bulle de filtre ».<br>
      Qu'est-ce qu'une **bulle de filtre** et voyez-vous un danger à ce phénomène ? 


## Envoi du document

### Export au format PDF

Exportez votre document vers le format PDF en suivant les instructions correspondant au logiciel de traitement de texte
utilisé.

!!! note "Export au format PDF"

    === "Word"

        - Enregistrer le document via la fonction **Enregistrer sous...**
        - Choisir le format de fichier **PDF** au lieu de *Document Word (.docx)*

    === "LibreOffice"

        - Cliquer sur l'entrée **Fichier** de la *barre de menus*
        - Choisir l'option **Exporter vers > Exporter directement au format PDF**

### Dépôt du travail

!!! note "Dépôt d'une copie sur Pronote"

    1. Connectez-vous à l'**ENT** : [https://ent.iledefrance.fr](https://ent.iledefrance.fr){:target="_blank"}
    2. Accédez à l'application **Pronote**
    3. Un *travail à faire* en SNT a été créé par votre enseignant. Il est identifiable sur la page d'accueil par un bouton :<br /> 
       **Déposer ma copie**{:style="display:inline-block;color:#4a1b7f;background-color:#ebdbff;padding:5px 20px;border-radius:10px;"}
    4. Cliquez sur le bouton **Déposer ma copie**
    5. Cliquez sur le bouton **Un seul fichier (*.pdf, *.doc, ...)**